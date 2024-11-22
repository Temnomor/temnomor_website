import asyncio
from functools import partial
from typing import Self

from loguru import logger
from playwright.async_api import Request, async_playwright

from constants import GROUP_LIST_URL, LECTURERS_LIST_URL
from utils import get_random_useragent
from utils.singleton import ABCSingleton


class HttpHeadersConstants:
    def __init__(self) -> None:
        self.group_list_headers: dict[str, str] = None
        self.group_headers: dict[str, str] = None
        self.lecturers_headers: dict[str, str] = None

    async def _retrieve_and_set_request_headers(
        self,
        request: Request,
        substring: str,
        variable_to_set: str
    ):
        if substring in request.url:
            request_headers = await request.all_headers()
            human_readable_variable_name = variable_to_set.replace('_', ' ')
            if request_headers:
                request_headers['user-agent'] = get_random_useragent()
                setattr(self, variable_to_set, request_headers)
                logger.success(f'{human_readable_variable_name} has setted.')
            else:
                logger.critical(f'{human_readable_variable_name} not found!')

    async def set_group_list_headers(self):
        async with async_playwright() as playwright:
            browser = await playwright.chromium.launch()
            page = await browser.new_page()
            retrieve_and_set_group_list_headers = partial(
                self._retrieve_and_set_request_headers,
                substring='aies.php',
                variable_to_set='group_list_headers'
            )
            page.on('request', retrieve_and_set_group_list_headers)
            await page.goto(GROUP_LIST_URL)
    
    async def set_group_headers(self):
        async with async_playwright() as playwright:
            browser = await playwright.chromium.launch()
            page = await browser.new_page()
            await page.goto(GROUP_LIST_URL)
            frame = page.frames[-1]
            await frame.select_option('#groups', index=3)
            retrieve_and_set_group_headers = partial(
                self._retrieve_and_set_request_headers,
                substring='action=group&',
                variable_to_set='group_headers'
            )
            page.on('request', retrieve_and_set_group_headers)
            await frame.evaluate(
                '''
                    var gr=$('#groups').val();
                    var bs=$('#groups option:selected').attr('bs');
                    var union=$('#groups option:selected').attr('union');
                    var sid=$('#groups option:selected').attr('sid');
                    var y=$('#groups option:selected').attr('year');
                    var varshed = $('#varshed').attr('checked')?1:0;
                    window.location.href = "../all_t/sh.php?action=group&union="+union+"&sid="+sid+"&gr="+gr+"&year="+y+"&vr="+varshed;
                '''
            )
            while self.group_headers is None:
                await asyncio.sleep(1)
    
    async def set_lecturers_headers(self):
        async with async_playwright() as playwright:
            browser = await playwright.chromium.launch()
            page = await browser.new_page()
            await page.goto(LECTURERS_LIST_URL)
            frame = page.frames[-1]
            await frame.select_option('#preps', index=3)
            retrieve_and_set_lecturers_headers = partial(
                self._retrieve_and_set_request_headers,
                substring='action=prep&',
                variable_to_set='lecturers_headers'
            )
            page.on('request', retrieve_and_set_lecturers_headers)
            await frame.evaluate(
                '''
                    var xid=$('#preps').val();
                    var count=$('#win_shed').attr('count');
                    var str='';
                    var varshed = $('#varshed').attr('checked')?1:0;
                    for (var i=0;i<count;i++){			
                        str=str+'&shed['+i+']='+$('#win_shed').attr('shedule'+i)+'&union['+i+']='+$('#win_shed').attr('union'+i)+'&year['+i+']='+$('#win_shed').attr('year'+i);
                    }
                    window.location.href = "../all_t/sh.php?action=prep&prep="+xid+"&vr="+varshed+"&count="+count+str; 
                '''
            )
            while self.lecturers_headers is None:
                await asyncio.sleep(1)


class SingleHttpHeadersConstants(HttpHeadersConstants, ABCSingleton):
    pass
