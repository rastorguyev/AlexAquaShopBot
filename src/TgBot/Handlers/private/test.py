from aiogram import types

from TgBot.bot import dp, bot


@dp.message_handler(commands=['user_id'], commands_prefix='/', chat_type=types.ChatType.PRIVATE)
async def user_id(message: types.Message):
    await message.answer(message.from_user.id)