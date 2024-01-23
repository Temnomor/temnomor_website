from fastapi.exceptions import RequestValidationError
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from loguru import logger
from exceptions import CollegeWebsiteError
from constants import ADMINS_TELEGRAM_USERNAMES


templates = Jinja2Templates(directory='templates')


async def handle_404_error(request: Request, _):
    blacklist = ('.css', '.js')
    if not any(word in str(request.url) for word in blacklist):
        logger.info(f'{request.url} not found. Redirecting to /')
    return RedirectResponse('/')


async def handle_500_error(request: Request, exc: Exception):
    logger.error(f'{ADMINS_TELEGRAM_USERNAMES}\n\nThere was an error on the Temnomor server. Code 500:')
    logger.exception(exc)
    return templates.TemplateResponse(
        request=request,
        name='error/500.html'
    )


async def handle_college_website_error(request: Request, exc: CollegeWebsiteError):
    logger.error(f'{ADMINS_TELEGRAM_USERNAMES}\n\nThere was an error on the college website:')
    logger.exception(exc)
    return templates.TemplateResponse(
        request=request,
        name='error/college_website_error.html'
    )


exception_handlers_dict = {404: handle_404_error,
                           405: handle_404_error,
                           RequestValidationError: handle_404_error,
                           500: handle_500_error,
                           CollegeWebsiteError: handle_college_website_error}
