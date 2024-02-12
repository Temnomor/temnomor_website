import asyncio
from itertools import filterfalse
from typing import Iterable, Literal

import orjson
from aiofile import async_open
from bs4 import BeautifulSoup
from loguru import logger
from playwright.async_api import async_playwright

import constants


async def get_schedule_urls_html():
    async with async_playwright() as context:
        browser = await context.webkit.launch()
        page = await browser.new_page()
        for url in constants.SCHEDULE_FORMS_URLS:
            await page.set_extra_http_headers(constants.HEADERS)
            await page.goto(url)
            html = await page.content()
            yield html


def remove_spaces_from_iter(__iter: Iterable) -> filterfalse:
    return filterfalse(lambda x: str(x).isspace(), __iter)


async def parse_schedule_urls(
    html: str,
    to_parse: Literal['groups',
                      'preps',
                      'cabs',
                      'academic_calendar']) -> None:
    soup = BeautifulSoup(html, 'lxml')
    parsed_urls = {}
    match to_parse:
        case 'groups':
            groups_elements = remove_spaces_from_iter(soup.find_all('a', {'class': 'grlink'}))
            for group_element in groups_elements:
                if group_element.has_attr('href'):
                    url = group_element.attrs.get('href')
                    group_name = group_element.text
                    parsed_urls[group_name] = url
        case 'preps' | 'cabs' as _type:
            elements = remove_spaces_from_iter(soup.find(id=_type).children)
            element_with_information = soup.find(id='win_shed')
            blacklist = (',', '/', 'вакансия', 'преподаватели', '------', 'null', '0-дист')
            for element in elements:
                if not any(x in element.text.lower() for x in blacklist):
                    count = int(element_with_information.attrs.get('count'))
                    object_id = element.attrs.get('value')
                    object_name = element.text
                    url = f'{constants.SCHEDULE_BASE_URL}action=prep&prep={object_id}&vr=1&count={count}'
                    other_params = ''
                    for i in range(count):
                        schedule_attr = element_with_information.attrs.get(f'shedule{i}')
                        union_attr = element_with_information.attrs.get(f'union{i}')
                        year_attr = element_with_information.attrs.get(f'year{i}')
                        other_params += f'&shed[{i}]={schedule_attr}&union[{i}]={union_attr}&year[{i}]={year_attr}'
                    url += other_params
                    if _type == 'preps':
                        parsed_urls[object_name] = url
                    elif _type == 'cabs':
                        if not object_name.isspace():
                            url = url.replace('prep', 'cab', 1)
                            parsed_urls[object_name] = url
        case 'academic_calendar':
            element_with_information = soup.find(id='win_shed')
            count = int(element_with_information.attrs.get('count'))
            url = f'{constants.SCHEDULE_BASE_URL}action=show_graph&count={count}'
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
                      'preps',
                      'cabs',
                      'academic_calendar']):
    async with async_open(f'templates/schedule/links/{filename}.json', 'wb') as file:
        await file.write(orjson.dumps(parsed_urls, option=orjson.OPT_SORT_KEYS))


async def start_parsing_urls(
        sleep_delay: int | float = 3000,
        cabinets_not_found_skip: bool = True):

    logger.info('Starting parsing links')

    html = get_schedule_urls_html()

    all_parsed_urls = {}

    async for element in html:
        while not any(group in element for group in ('(9)', '(11)')):
            logger.warning('Groups not found in HTML! Trying again...')
            await asyncio.sleep(sleep_delay)
            html = get_schedule_urls_html()

        parsed_urls, filename = await parse_schedule_urls(element, to_parse='groups')
        all_parsed_urls |= parsed_urls

    await dump_parsed_urls_to_json_file(all_parsed_urls, filename)
    logger.success('The groups were successfully parsed')

    # while 'prep0' not in html:
    #     logger.warning('Lecturers not found in HTML! Trying again...')
    #     await asyncio.sleep(sleep_delay)
    #     html = await get_schedule_urls_html()

    # parsed_urls, filename = await parse_schedule_urls(html, to_parse='preps')
    # await dump_parsed_urls_to_json_file(parsed_urls, filename)
    # logger.success('The lecturers were successfully parsed')

    # parsed_urls, filename = await parse_schedule_urls(html, to_parse='academic_calendar')
    # await dump_parsed_urls_to_json_file(parsed_urls, filename)
    # logger.success('The academic calendar were successfully parsed')

    # while '13-212к' not in html:
    #     if cabinets_not_found_skip:
    #         return
    #     logger.warning('Cabinets not found in HTML! Trying again...')
    #     await asyncio.sleep(sleep_delay)
    #     html = await get_schedule_urls_html()

    # parsed_urls, filename = await parse_schedule_urls(html, to_parse='cabs')
    # await dump_parsed_urls_to_json_file(parsed_urls, filename)
    # logger.success('The cabinets were successfully parsed')
