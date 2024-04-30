import asyncio
from itertools import filterfalse
from typing import Iterable, Literal

import orjson
from aiofile import async_open
from bs4 import BeautifulSoup
from loguru import logger
import re
from playwright.async_api import async_playwright
from urllib.parse import urlencode

import constants


async def get_schedule_urls_html(urls: list[str] = constants.SCHEDULE_FORMS_URLS):
    async with async_playwright() as context:
        browser = await context.webkit.launch()
        page = await browser.new_page()
        for url in urls:
            await page.set_extra_http_headers(constants.SCHEDULE_FORM_HEADERS)
            await page.goto('https://mnokol.tyuiu.ru/site/', timeout=0)
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
            html = await frame.content()
            yield html, url


def remove_spaces_from_iter(__iter: Iterable) -> filterfalse:
    return filterfalse(lambda x: str(x).isspace(), __iter)


async def parse_schedule_urls(
    html: str,
    to_parse: Literal['groups',
                      'preps',
                      'academic_calendar'],
    group_base_url: str = None
) -> None:
    soup = BeautifulSoup(html, 'lxml')
    parsed_urls = {}
    match to_parse:
        case 'groups':
            groups_elements = remove_spaces_from_iter(soup.find_all('option'))
            for group_element in groups_elements:
                if group_element.has_attr('sid'):
                    base_url = re.sub(r'(?<=\/)[a-z_]+(?=\.php)', 'sh', group_base_url) + '?'
                    union = group_element.attrs.get('union')
                    sid = group_element.attrs.get('sid')
                    gr = group_element.attrs.get('value')
                    year = group_element.attrs.get('year')
                    group_name = group_element.text
                    
                    query_params = urlencode(
                        {
                            'action': 'group',
                            'union': union,
                            'sid': sid,
                            'gr': gr,
                            'year': year,
                            'vr': 1
                        }
                    )
                    final_url = base_url + query_params
                    parsed_urls[group_name] = final_url
        case 'preps':
            elements = remove_spaces_from_iter(soup.find(id='preps').children)
            element_with_information = soup.find(id='win_shed')
            for element in elements:
                count = int(element_with_information.attrs.get('count'))
                object_id = element.attrs.get('value')
                object_name = element.text
                base_url = re.sub(r'(?<=\/)[a-z_]+(?=\.php)', 'sh', group_base_url) + '?'
                url = f'{base_url}action=prep&prep={object_id}&vr=1&count={count}'
                other_params = ''
                for i in range(count):
                    schedule_attr = element_with_information.attrs.get(f'shedule{i}')
                    union_attr = element_with_information.attrs.get(f'union{i}')
                    year_attr = element_with_information.attrs.get(f'year{i}')
                    other_params += f'&shed[{i}]={schedule_attr}&union[{i}]={union_attr}&year[{i}]={year_attr}'
                url += other_params
                parsed_urls[object_name] = url
        case 'academic_calendar':
            element_with_information = soup.find(id='win_shed')
            count = int(element_with_information.attrs.get('count'))
            #url = f'{constants.SCHEDULE_BASE_URL}act!#!#ion=show_graph&count={count}'
            other_params = ''
            for i in range(count):
                schedule_attr = element_with_information.attrs.get(f'shedule{i}')
                union_attr = element_with_information.attrs.get(f'union{i}')
                other_params += f'&shed[{i}]={schedule_attr}&union[{i}]={union_attr}'
            url += other_params
            parsed_urls['academic_calendar'] = url

    return parsed_urls, to_parse


async def dump_parsed_urls_to_json_file(
    parsed_urls: list[dict],
    filename: Literal['groups',
                      'preps'
                      'academic_calendar']
):
    async with async_open(f'templates/schedule/links/{filename}.json', 'wb') as file:
        await file.write(orjson.dumps(parsed_urls, option=orjson.OPT_SORT_KEYS))


async def start_parsing_urls(sleep_delay: int | float = 3000):

    logger.info('Starting parsing links')

    gen = get_schedule_urls_html()

    all_parsed_urls = {}

    async for html, url in gen:
        while not any(group in html for group in ('(9)', '(11)')):
            logger.warning('Groups not found in HTML! Trying again...')
            await asyncio.sleep(sleep_delay)
            gen = get_schedule_urls_html()

        parsed_urls, filename = await parse_schedule_urls(
            html=html,
            to_parse='groups',
            group_base_url=url
        )
        all_parsed_urls |= parsed_urls

    await dump_parsed_urls_to_json_file(all_parsed_urls, filename)
    logger.success('The groups were successfully parsed')

    gen = get_schedule_urls_html(['https://coworking.tyuiu.ru/shs/prep/prep.php'])
    async for html, url in gen:
        while 'prep0' not in html:
            logger.warning('Lecturers not found in HTML! Trying again...')
            await asyncio.sleep(sleep_delay)
            gen = await get_schedule_urls_html()

        parsed_urls, filename = await parse_schedule_urls(
            html=html,
            to_parse='preps',
            group_base_url=url
        )
        await dump_parsed_urls_to_json_file(parsed_urls, filename)
        logger.success('The lecturers were successfully parsed')

    # parsed_urls, filename = await parse_schedule_urls(html, to_parse='academic_calendar')
    # await dump_parsed_urls_to_json_file(parsed_urls, filename)
    # logger.success('The academic calendar were successfully parsed')
