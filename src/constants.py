import os
from dotenv import load_dotenv


load_dotenv()


PROJECT_NAME = 'TEMNOMOR WEBSITE'


SCHEDULE_FORMS_URLS = (
    'https://coworking.tyuiu.ru/shs/aies_t/aies.php',
    'https://coworking.tyuiu.ru/shs/mpn_t/mpn.php',
    'https://coworking.tyuiu.ru/shs/ngo_t/ngo.php',
    'https://coworking.tyuiu.ru/shs/sonh_po_t/sonh_po.php',
    'https://coworking.tyuiu.ru/shs/zo_t/zo.php'
)


SCHEDULE_GROUP_HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Microsoft Edge";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0',
}

SCHEDULE_FORM_HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://coworking.tyuiu.ru/shs/shedule.php',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Microsoft Edge";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'iframe',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0',
}

SCHEDULE_LECTURERS_HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://coworking.tyuiu.ru/shs/prep/prep.php',
    'sec-ch-ua': '"Chromium";v="124", "Microsoft Edge";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'iframe',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0',
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
