from fastapi.exceptions import RequestValidationError
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from loguru import logger
from starlette.datastructures import QueryParams
from exceptions import CollegeWebsiteError
from urllib.parse import unquote
from constants import ADMINS_TELEGRAM_USERNAMES


templates = Jinja2Templates(directory='templates')


def to_url(
        request_method: str,
        reuqest_path: str,
        params: QueryParams):

    return unquote(f'{request_method} {reuqest_path}?{params}')


async def handle_404_error(*_):
    response = '<script>window.location.href = "/";</script>'
    return HTMLResponse(response, status_code=404)


async def handle_500_error(request: Request, exc: Exception):
    requested_path = request.url.path
    params = request.query_params
    request_method = request.method

    url = to_url(request_method, requested_path, params)

    logger.exception((
        f'{ADMINS_TELEGRAM_USERNAMES}\n\nThere was an error on the Temnomor server. '
        f'Code 500.\n\nURL: {url}\n\n'
        f'{exc}'
    ))

    return templates.TemplateResponse(
        request=request,
        name='error/500.html',
        status_code=500
    )


async def handle_college_website_error(request: Request, exc: CollegeWebsiteError):
    requested_path = request.url.path
    params = request.query_params
    request_method = request.method

    url = to_url(request_method, requested_path, params)

    logger.exception((
        f'{ADMINS_TELEGRAM_USERNAMES}\n\nThere was an error on the college website:\n\n'
        f'URL: {url}\n\n'
        f'{exc}'
    ))

    return templates.TemplateResponse(
        request=request,
        name='error/college_website_error.html'
    )


exception_handlers_dict = {404: handle_404_error,
                           405: handle_404_error,
                           RequestValidationError: handle_404_error,
                           500: handle_500_error,
                           CollegeWebsiteError: handle_college_website_error}
