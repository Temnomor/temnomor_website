import asyncio
from typing import Any

from aiohttp import ClientSession

from constants import TG_LOGGING_BOT_TOKEN, TG_LOGGING_CHAT_ID


telegram_send_message_url = f'https://api.telegram.org/bot{TG_LOGGING_BOT_TOKEN}/sendMessage'


async def send_message_to_admins_chat(
        message: str,
        chat_id: int | str = TG_LOGGING_CHAT_ID) -> None:

    params = {'chat_id': chat_id,
              'text': message}

    async with ClientSession() as session:
        await session.post(telegram_send_message_url, params=params)


async def log_to_telegram_bot(log: Any | str) -> None:
    if len(log) > 4096:
        messages = (log[i:i + 4096] for i in range(0, len(log), 4096))
        for message in messages:
            await send_message_to_admins_chat(message)
            await asyncio.sleep(10)
    else:
        await send_message_to_admins_chat(log)
