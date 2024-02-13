import os
from dotenv import load_dotenv


load_dotenv()


PROJECT_NAME = 'TEMNOMOR WEBSITE'


SCHEDULE_BASE_URL = 'http://sh.mnokol.tyuiu.ru/shs/all/open.php?'

SCHEDULE_FORMS_URLS = (
    'http://77.242.109.185/aies/sh.php',
    'http://77.242.109.185/mpn/sh.php',
    'http://77.242.109.185/ngo/sh.php',
    'http://77.242.109.185/sonh_po/sh.php',
    'http://77.242.109.185/zo/sh.php'
)


SCHEDULE_GROUP_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9,ru;q=0.8,tg;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Referer': 'http://77.242.109.185/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
}

SCHEDULE_FORM_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9,ru;q=0.8,tg;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Referer': 'http://mnokol.tyuiu.ru/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
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
