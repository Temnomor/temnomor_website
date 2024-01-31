import asyncio
import os
import shutil
from argparse import ArgumentParser

from apscheduler.schedulers.asyncio import AsyncIOScheduler, BaseScheduler
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from loguru import logger

from gunicorn.app.base import BaseApplication
from constants import LOGGER_FORMAT_TELEGRAM_BOT, OPTIONS
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


class StandaloneApplication(BaseApplication):

    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super().__init__()

    def load_config(self):
        config = {key: value for key, value in self.options.items()
                  if key in self.cfg.settings and value is not None}
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application


@logger.catch
async def clean_up(scheduler: BaseScheduler = None):
    if scheduler and scheduler.running:
        scheduler.shutdown(wait=False)
        logger.info('Scheduler stopped')

    if os.path.exists('temp'):
        shutil.rmtree('temp', ignore_errors=True)
        logger.info('Folder "temp" was deleted')


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

        StandaloneApplication(app=app, options=OPTIONS).run()

    finally:
        await clean_up(scheduler=scheduler)


if __name__ == '__main__':
    asyncio.run(main())
