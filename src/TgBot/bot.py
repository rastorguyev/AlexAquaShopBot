
import logging

import requests as requests
from aiogram import Bot, Dispatcher, executor
from settings import settings


logging.basicConfig(level=logging.INFO)
bot = Bot(token=settings.bot_token)
dp = Dispatcher(bot)

if __name__ == "__main__":
    from Handlers import dp
    executor.start_polling(dp, skip_updates=True)
    u = bot.get_updates()
    print(u)