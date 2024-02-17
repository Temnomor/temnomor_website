import asyncio
from typing import Any

from aiohttp import ClientSession, ClientResponse

from constants import TG_LOGGING_BOT_TOKEN, TG_LOGGING_CHAT_ID


telegram_send_message_url = f'https://api.telegram.org/bot{TG_LOGGING_BOT_TOKEN}/sendMessage'


async def send_post_and_get_response(url: str, params: dict[str, Any]) -> ClientResponse:
    async with ClientSession() as session:
        async with session.post(url, params=params, ssl=False) as response:
            return response


async def send_message_to_admins_chat(
        message: str,
        chat_id: int | str = TG_LOGGING_CHAT_ID) -> None:

    params = {'chat_id': chat_id,
              'text': message}

    response = await send_post_and_get_response(telegram_send_message_url, params)
    while not response.ok:
        delay = int(response.headers.get('Retry-After', 60))
        await asyncio.sleep(delay)
        response = await send_post_and_get_response(telegram_send_message_url, params)


async def log_to_telegram_bot(
        log: Any | str,
        msg_length_limit: int = 4096) -> None:
    """
    sink for loguru
    """

    if len(log) > msg_length_limit:
        messages = (log[i:i + msg_length_limit] for i in range(0, len(log), msg_length_limit))
        for message in messages:
            await send_message_to_admins_chat(message)
    else:
        await send_message_to_admins_chat(log)
