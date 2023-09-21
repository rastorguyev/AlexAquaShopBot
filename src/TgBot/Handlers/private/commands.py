import requests
from aiogram import types
from aiogram.types.web_app_info import WebAppInfo

#from TgBot.Keyboards import ikb_tasks, ikb_new_task, ikb_start, ikb_task_client, ikb_task_manager, kb
from TgBot.bot import dp, bot


@dp.message_handler(commands=['start'], commands_prefix='/', chat_type=types.ChatType.PRIVATE)
async def start(message: types.Message):
    #await message.answer(message.from_user.id)
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть магазин', web_app=WebAppInfo(url='http://serverforyou.ru:8081')))
    await message.answer('Hello!',  reply_markup=markup)