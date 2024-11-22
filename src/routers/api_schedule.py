import asyncio
import os
import re
import time

import orjson
from aiofile import async_open
from aiohttp import ClientSession, ClientTimeout
from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from playwright.async_api import async_playwright

from exceptions import CollegeWebsiteError
from utils import get_random_useragent, SingleHttpHeadersConstants


router = APIRouter(prefix='/api')

templates = Jinja2Templates(directory='templates')


Seconds = int


regex = re.compile(
    r'<script.*?/script>|<link.*?>|<img.*?>|<style.*?/style>|<iframe.*?/iframe>|<embed.*?>',
    flags=re.MULTILINE | re.IGNORECASE | re.DOTALL)


async def playwright_get_html(url: str, timeout: Seconds):
    async with async_playwright() as context:
        browser = await context.webkit.launch()
        page = await browser.new_page()
        SingleHttpHeadersConstants().lecturers_headers['user-agent'] = get_random_useragent()
        await page.set_extra_http_headers(SingleHttpHeadersConstants().lecturers_headers)
        await page.goto('https://coworking.tyuiu.ru', timeout=timeout)
        await page.evaluate(
            f"""
            document.documentElement.innerHTML = document.documentElement.innerHTML + '<iframe name="new_frame" src="{url}"></iframe>';
            """
        )
        frame = page.frame(name='new_frame')
        while frame is None:
            await asyncio.sleep(1)
            frame = page.frame(name='new_frame')
        await frame.wait_for_load_state()
        html = r''.join(await frame.content())
        return regex.sub('', html)


async def make_html_request(
        url: str,
        referer_url: str,
        timeout: ClientTimeout,) -> str:
    updated_headers = {x: y for x, y in SingleHttpHeadersConstants().group_headers.items()}
    updated_headers['referer'] = referer_url
    updated_headers['user-agent'] = get_random_useragent()
    async with ClientSession(headers=updated_headers, timeout=timeout) as session:
        async with session.get(url, ssl=False) as response:
            html = r''.join(await response.text())
            return regex.sub('', html)


async def make_json_request(url: str) -> dict:
    async with ClientSession() as session:
        async with session.post(url, ssl=False) as response:
            return await response.json(loads=orjson.loads)


def add_tags_to_html(html: str) -> str:
    return html + (
        '<script defer src="{{ url_for("static", path="schedule/js/schedule.js") }}"></script>'
        '<link rel="stylesheet" href="{{ url_for("static", path="schedule/css/schedule.css") }}">')


async def dump_to_html_file(html: str, name: str):
    html = add_tags_to_html(html)
    async with async_open(f'templates/schedule/{name}.html', 'w') as file:
        await file.write(html)


def template_response(request: Request, name: str):
    return templates.TemplateResponse(
        request=request,
        name=f'/schedule/{name}.html'
    )


def file_modification_last_time(path: str):
    return time.time() - os.path.getmtime(path)


def cached_schedule_exists(filename: str, seconds: int) -> bool:
    path = f'templates/schedule/{filename}.html'
    if os.path.exists(path) and file_modification_last_time(path) < seconds:
        return True
    return False


def handle_timeout(request: Request, filename: str, html: str = None):
    if cached_schedule_exists(filename, 21600):
        return template_response(request, filename)
    else:
        raise CollegeWebsiteError(
            'Timeout exceeded and there is no cached schedule or it`s too old. Or "lenta_m" not in html'
            f'\n\nHTML:\n\n{html}')


async def get_schedule_for_group(
        request: Request,
        obj: str,
        api_endpoint: str,
        timeout: Seconds):

    api_url = f'{request.base_url}api/{api_endpoint}'
    json_dict = await make_json_request(api_url)
    json_dict_keys = json_dict.keys()

    if obj in json_dict_keys:
        obj_schedule_url = json_dict[obj]['schedule_url']
        obj_referer = json_dict[obj]['schedule_url'] #json_dict[obj]['referer']
        try:
            for _ in range(5):
                html = await make_html_request(
                    url=obj_schedule_url,
                    referer_url=obj_referer,
                    timeout=ClientTimeout(timeout)
                )
                if 'lenta_m' in html:
                    break
                await asyncio.sleep(1)

            if 'lenta_m' not in html:
                return handle_timeout(request, obj, html)

        except asyncio.TimeoutError:
            return handle_timeout(request, obj)

        await dump_to_html_file(html, obj)
        return template_response(request, obj)
    else:
        return RedirectResponse('/')


async def get_schedule_for_other(
    request: Request,
    obj: str,
    api_endpoint: str,
    timeout: Seconds,
    cache_since: int
):
    api_url = f'{request.base_url}api/{api_endpoint}'
    json_dict = await make_json_request(api_url)
    json_dict_keys = json_dict.keys()

    if obj in json_dict_keys:
        try:
            if cached_schedule_exists(obj, cache_since):
                return template_response(request, obj)

            for _ in range(5):
                html = await playwright_get_html(
                    url=json_dict.get(obj),
                    timeout=timeout
                )
                if 'lenta_m' in html:
                    break
                await asyncio.sleep(1)

            #html = await make_html_request(
            #    url=json_dict.get(obj),
            #    timeout=ClientTimeout(timeout),
            #    headers=SCHEDULE_LECTURERS_HEADERS??!
            #)

            if 'lenta_m' not in html:
                return handle_timeout(request, obj, html)

        except asyncio.TimeoutError:
            return handle_timeout(request, obj)

        await dump_to_html_file(html, obj)
        return template_response(request, obj)
    else:
        return RedirectResponse('/')


async def schedule_is_available() -> bool:
    ...


@router.get('/groups')
async def get_group_schedule(request: Request, group: str):
    return await get_schedule_for_group(
        request=request,
        obj=group,
        api_endpoint='getGroupsData',
        timeout=15
    )


@router.get('/lecturers')
async def get_lecturer_schedule(request: Request, lecturer: str):
    return await get_schedule_for_other(
        request=request,
        obj=lecturer,
        api_endpoint='getLecturersData',
        timeout=240000,
        cache_since=3600
    )


@router.get('/cabinets')
async def get_cabinet_schedule(request: Request, cabinet: str):
    return await get_schedule_for_other(
        request=request,
        obj=cabinet,
        api_endpoint='getCabinetsData',
        timeout=240000,
        cache_since=100
    )


@router.get('/academic_calendar')
async def get_academic_calendar_schedule(request: Request):
    return await get_schedule_for_other(
        request=request,
        obj='academic_calendar',
        api_endpoint='getAcademicCalendarData',
        timeout=240000,
        cache_since=86400
    )
