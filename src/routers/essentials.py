from fastapi import APIRouter
from fastapi.responses import FileResponse


router = APIRouter()


@router.api_route('/favicon.ico', methods=('GET', 'POST'))
async def favicon_ico():
    return FileResponse('static/favicon.ico')


@router.api_route('/favicon.png', methods=('GET', 'POST'))
async def favicon_png():
    return FileResponse('static/favicon.png')


@router.api_route('/robots.txt', methods=('GET', 'POST'))
async def robots_txt():
    return FileResponse('static/robots.txt')
