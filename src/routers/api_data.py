from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse, FileResponse
from aiofile import async_open
from playwright.async_api import async_playwright
import os
import orjson


router = APIRouter(prefix='/api')


async def json_response(json_filename: str) -> JSONResponse:
    path = f'templates/schedule/links/{json_filename}'
    if os.path.exists(path):
        async with async_open(path, 'r') as file:
            json_ = await file.read()
        return JSONResponse(content=orjson.loads(json_))
    else:
        return JSONResponse(content={})


async def take_screenshot(url: str, path: str):
    async with async_playwright() as context:
        browser = await context.chromium.launch()
        page = await browser.new_page()
        await page.goto(url)
        await page.screenshot(path=path, full_page=True)
        await browser.close()


@router.post('/getGroupsData')
async def get_groups_data():
    return await json_response('groups.json')


@router.post('/getLecturersData')
async def get_lecturers_data():
    return await json_response('preps.json')


@router.post('/getCabinetsData')
async def get_cabinets_data():
    return await json_response('cabs.json')


@router.post('/getAcademicCalendarData')
async def get_academic_calendar_data():
    return await json_response('academic_calendar.json')


@router.post('/getLecturersFullNameData')
async def get_lecturers_fullname_data():
    return await json_response('lecturers_fullname.json')


@router.api_route('/getScreenshot', methods=('GET', 'POST'))
async def get_screenshot(request: Request, group: str):
    path = f'temp/{group}.png'
    await take_screenshot(
        url=f'{request.base_url}api/groups?group={group}',
        path=path)
    return FileResponse(path=path)
