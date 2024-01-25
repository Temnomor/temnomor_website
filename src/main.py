import asyncio
import os
import shutil
from argparse import ArgumentParser
from typing import NoReturn, Awaitable, Iterable

import uvicorn
from apscheduler.schedulers.asyncio import AsyncIOScheduler, BaseScheduler
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from loguru import logger

from constants import SSL_CERTFILE_PATH, SSL_KEYFILE_PATH, HOST_PORT, LOGGER_FORMAT_TELEGRAM_BOT
from exceptions import exception_handlers_dict
from routers import api_routers
from utils.logging_handler import log_to_telegram_bot
from utils.urls_parser import start_parsing_urls


app = FastAPI(
    openapi_url=None,
    docs_url=None,
    redoc_url=None,
    debug=False
)

for router in api_routers:
    app.include_router(router)

app.mount('/static', StaticFiles(directory='static'), name='static')

app.exception_handlers = exception_handlers_dict


@app.get('/favicon.ico')
async def favicon():
    return FileResponse('static/favicon.ico')


@app.middleware('http')
async def logging_middleware(
        request: Request,
        call_next: Awaitable,
        blacklist: Iterable[str] = ('.css', '.js', '.png', '.ico')):

    response = await call_next(request)
    requested_url = request.url.path

    if not any(x in requested_url for x in blacklist):
        request_method = request.method
        status_code = response.status_code
        logger.info(f'Requested: {request_method} {requested_url}\nStatus: {status_code}')

    return response


@logger.catch
async def clean_up(scheduler: BaseScheduler = None):
    if scheduler and scheduler.running:
        scheduler.shutdown(wait=False)
        logger.info('Scheduler stopped')

    if os.path.exists('temp'):
        shutil.rmtree('temp', ignore_errors=True)
        logger.info('Folder "temp" was deleted')


@logger.catch
async def run_server() -> NoReturn:
    config = uvicorn.Config(
        'main:app',
        port=HOST_PORT,
        log_level='info',
        workers=9,
        forwarded_allow_ips='*',
        ssl_keyfile=SSL_KEYFILE_PATH,
        ssl_certfile=SSL_CERTFILE_PATH
        )

    server = uvicorn.Server(config)

    await server.serve()


@logger.catch
async def main() -> None:
    arg_parser = ArgumentParser()
    arg_parser.add_argument('-d', '--dont_parse_links', action='store_true')
    args = arg_parser.parse_args()
    dont_parse_links = args.dont_parse_links

    scheduler = AsyncIOScheduler()
    scheduler.add_job(start_parsing_urls, 'interval', hours=6)

    logger.add(
        sink=log_to_telegram_bot,
        level='INFO',
        format=LOGGER_FORMAT_TELEGRAM_BOT,
        backtrace=False)

    try:
        if not os.path.exists('temp'):
            os.mkdir('temp')

        if not dont_parse_links:
            await start_parsing_urls()
        else:
            logger.info('-d | --dont_parse_links flag detected! Skipping first URL parsing')

        scheduler.start()
        logger.info('Scheduler started. Running server...')

        await run_server()
    finally:
        await clean_up(scheduler=scheduler)


if __name__ == '__main__':
    asyncio.run(main())
