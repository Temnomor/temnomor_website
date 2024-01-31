import os
from dotenv import load_dotenv
from multiprocessing import cpu_count


load_dotenv()


PROJECT_NAME = 'TEMNOMOR WEBSITE'


SCHEDULE_BASE_URL = 'http://sh.mnokol.tyuiu.ru/shold/shedule/show_shedule.php?'

SCHEDULE_FORM_URL = 'http://sh.mnokol.tyuiu.ru/shold/index2.php'

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Upgrade-Insecure-Requests': '1',
    'Host': 'sh.mnokol.tyuiu.ru',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Safari/605.1.15',
    'Referer': 'http://sh.mnokol.tyuiu.ru/shold/index2.php',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
}


HOST_PORT = int(os.getenv('HOST_PORT', 8081))


TG_LOGGING_BOT_TOKEN = os.getenv('TG_LOGGING_BOT_TOKEN')
TG_LOGGING_CHAT_ID = int(os.getenv('TG_LOGGING_CHAT_ID'))

LOGGER_FORMAT_TELEGRAM_BOT = (
    f'{PROJECT_NAME}\n\n'
    '{level: <8}'
    '{time:DD.MM.YYYY HH:mm:ss}\n'
    '{name}:{function}:{line}\n\n'
    '{message}\n'
)

ADMINS_TELEGRAM_USERNAMES = os.getenv('ADMINS_TELEGRAM_USERNAMES')


SSL_KEYFILE_PATH = os.getenv('SSL_KEYFILE_PATH')
SSL_CERTFILE_PATH = os.getenv('SSL_CERTFILE_PATH')


OPTIONS = {
    'wsgi_app': 'main:main',

    'workers': cpu_count() * 2 + 1,

    'worker_class': 'uvicorn.workers.UvicornWorker',

    'bind': f'127.0.0.1:{HOST_PORT}',

    'forwarded_allow_ips': '*',

    'keyfile': SSL_KEYFILE_PATH,

    'certfile': SSL_CERTFILE_PATH,

    'preload_app': True
}
