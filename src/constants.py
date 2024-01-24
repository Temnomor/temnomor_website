import os
from dotenv import load_dotenv


load_dotenv()


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


HOST_PORT = int(os.getenv('HOST_PORT'))


TG_LOGGING_BOT_TOKEN = os.getenv('TG_LOGGING_BOT_TOKEN')
TG_LOGGING_CHAT_ID = int(os.getenv('TG_LOGGING_CHAT_ID'))


ADMINS_TELEGRAM_USERNAMES = os.getenv('ADMINS_TELEGRAM_USERNAMES')


SSL_KEYFILE_PATH = os.getenv('SSL_KEYFILE_PATH')
SSL_CERTFILE_PATH = os.getenv('SSL_CERTFILE_PATH')