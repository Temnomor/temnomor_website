import os
from dotenv import load_dotenv


load_dotenv()


PROJECT_NAME = 'TEMNOMOR WEBSITE'


SCHEDULE_BASE_URL = 'http://sh.mnokol.tyuiu.ru/shs/all/open.php?'

SCHEDULE_FORMS_URLS = (
    'http://sh.mnokol.tyuiu.ru/shs/aies/sh.php',
    'http://sh.mnokol.tyuiu.ru/shs/mpn/sh.php',
    'http://sh.mnokol.tyuiu.ru/shs/ngo/sh.php',
    'http://sh.mnokol.tyuiu.ru/shs/sonh_po/sh.php',
    'http://sh.mnokol.tyuiu.ru/shs/zo/sh.php'
)


SCHEDULE_GROUP_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9,ru;q=0.8,tg;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Referer': '',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
}

SCHEDULE_FORM_HEADERS = {
    'Host': 'sh.mnokol.tyuiu.ru',
    'Referer': 'http://mnokol.tyuiu.ru/',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'no-cache',
    'Pragma': 'no-cache',
    'Accept-Language': 'en-US,en;q=0.9,ru;q=0.8,tg;q=0.7, en-US',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/605.1.15 (KHTML, like Gecko)',
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
