from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(text="/start")
async def bot_start(message: types.Message):
    await message.answer(f"Приветствую вас!")

@dp.message_handler(text="username")
async def bot_user_name(message: types.Message):
    await message.answer(f"{message.from_user.full_name}")

@dp.message_handler(text_startswith="id")
async def bot_user_id(message: types.Message):
    await message.answer(f"{message.from_user.id}")

@dp.message_handler(text_contains="1")
async def bot_user_in_1(message: types.Message):
    await message.answer(f"В вашем сообщение есть 1")