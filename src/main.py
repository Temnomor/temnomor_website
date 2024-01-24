import asyncio
import os
import shutil
from argparse import ArgumentParser
from typing import NoReturn

import uvicorn
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from loguru import logger

from constants import SSL_CERTFILE_PATH, SSL_KEYFILE_PATH
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


logger.add(sink=log_to_telegram_bot, level='INFO')


@app.get('/favicon.ico')
async def favicon():
    return FileResponse('static/favicon.ico')


@logger.catch
async def run_server() -> NoReturn:
    config = uvicorn.Config(
        'main:app',
        port=8000,
        log_level='info',
        workers=9,
        ssl_keyfile=SSL_KEYFILE_PATH,
        ssl_certfile=SSL_CERTFILE_PATH)

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

    try:
        if not os.path.exists('temp'):
            os.mkdir('temp')

        if not dont_parse_links:
            await start_parsing_urls()

        scheduler.start()
        logger.info('Scheduler started. Running server...')

        await run_server()
    finally:
        if scheduler and scheduler.running:
            scheduler.shutdown(wait=False)
        if os.path.exists('temp'):
            shutil.rmtree('temp', ignore_errors=True)

if __name__ == '__main__':
    asyncio.run(main())
