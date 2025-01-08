import os

from dotenv import load_dotenv


load_dotenv()


PROJECT_NAME = 'TEMNOMOR WEBSITE'


SCHEDULE_FORMS_URLS = (
    'https://mnokol.tyuiu.ru/site/index.php?option=com_content&view=article&id=1583&Itemid=299',
    'https://mnokol.tyuiu.ru/site/index.php?option=com_content&view=article&id=1301&Itemid=300',
    'https://mnokol.tyuiu.ru/site/index.php?option=com_content&view=article&id=1300&Itemid=301',
    'https://mnokol.tyuiu.ru/site/index.php?option=com_content&view=article&id=1302&Itemid=302',
    'https://mnokol.tyuiu.ru/site/index.php?option=com_content&view=article&id=1584&Itemid=303'
)

GROUP_LIST_URL = 'https://mnokol.tyuiu.ru/site/index.php?option=com_content&view=article&id=1583&Itemid=299'

LECTURERS_LIST_URL = 'https://mnokol.tyuiu.ru/site/index.php?option=com_content&view=article&id=1247&Itemid=304'


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
