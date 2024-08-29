import asyncio
import os
import shutil
from argparse import ArgumentParser
from typing import NoReturn

import uvicorn
from apscheduler.schedulers.asyncio import AsyncIOScheduler, BaseScheduler
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from loguru import logger

from constants import LOGGER_FORMAT_TELEGRAM_BOT
from exceptions import exception_handlers_dict
from routers import api_routers
from utils.logging_handler import log_to_telegram_bot
from utils.urls_parser import start_parsing_urls
from uvicorn_config import get_config


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
    config = get_config()
    server = uvicorn.Server(config)
    await server.serve()


@logger.catch
async def main() -> None:
    arg_parser = ArgumentParser()
    arg_parser.add_argument('-p', '--parse_links', action='store_true')
    args = arg_parser.parse_args()
    parse_links = args.parse_links

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

        if parse_links:
            logger.info('-p | --parse_links flag detected!')
            await start_parsing_urls()
        else:
            logger.info('Skipping first URL parsing')

        scheduler.start()
        logger.info('Scheduler started. Running server...')

        await run_server()
    finally:
        await clean_up(scheduler=scheduler)


if __name__ == '__main__':
    asyncio.run(main())
