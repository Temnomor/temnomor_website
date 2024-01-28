import asyncio
import os
import time

import orjson
from aiofile import async_open
from aiohttp import ClientSession, ClientTimeout
from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from playwright.async_api import async_playwright

from constants import HEADERS
from exceptions import CollegeWebsiteError


router = APIRouter(prefix='/api')

templates = Jinja2Templates(directory='templates')


Seconds = int


async def playwright_get_html(url: str, timeout: Seconds):
    async with async_playwright() as context:
        browser = await context.webkit.launch()
        page = await browser.new_page()
        await page.set_extra_http_headers(HEADERS)
        await page.goto(url, timeout=timeout)
        return await page.content()


async def make_html_request(
        url: str,
        timeout: ClientTimeout,
        headers: dict[str, str] = HEADERS) -> str:

    async with ClientSession(headers=headers, timeout=timeout) as session:
        async with session.get(url) as response:
            return r''.join(await response.text())


async def make_json_request(url: str) -> dict:
    async with ClientSession() as session:
        async with session.post(url) as response:
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


def handle_timeout(request: Request, filename: str):
    if cached_schedule_exists(filename, 21600):
        return template_response(request, filename)
    else:
        raise CollegeWebsiteError(
            "Timeout exceeded and there is no cached schedule or it's too old")


async def get_schedule_for_group(
        request: Request,
        obj: str,
        api_endpoint: str,
        timeout: Seconds):

    api_url = f'{request.base_url}api/{api_endpoint}'
    json_dict = await make_json_request(api_url)
    json_dict_keys = json_dict.keys()

    if obj in json_dict_keys:
        try:
            html = await make_html_request(
                json_dict.get(obj),
                ClientTimeout(timeout))

            if 'lenta_m' not in html:
                return handle_timeout(request, obj)

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
    timeout: Seconds
):
    api_url = f'{request.base_url}api/{api_endpoint}'
    json_dict = await make_json_request(api_url)
    json_dict_keys = json_dict.keys()

    if obj in json_dict_keys:
        try:
            if cached_schedule_exists(obj, 3600):
                return template_response(request, obj)

            html = await playwright_get_html(
                json_dict.get(obj),
                timeout)

            if 'lenta_m' not in html:
                return handle_timeout(request, obj)

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
        timeout=240000
    )


@router.get('/cabinets')
async def get_cabinet_schedule(request: Request, cabinet: str):
    return await get_schedule_for_other(
        request=request,
        obj=cabinet,
        api_endpoint='getCabinetsData',
        timeout=240000
    )


@router.get('/academic_calendar')
async def get_academic_calendar_schedule(request: Request):
    return await get_schedule_for_other(
        request=request,
        obj='academic_calendar',
        api_endpoint='getAcademicCalendarData',
        timeout=240000
    )
