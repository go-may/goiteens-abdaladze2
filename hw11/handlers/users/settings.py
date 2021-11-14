from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandSettings, CommandPrivacy

from loader import dp


@dp.message_handler(CommandSettings())
async def bot_help(message: types.Message):
    await message.answer(f"Добро пожаловать {message.from_user.full_name} вы в настройках")


@dp.message_handler(CommandPrivacy())
async def bot_help(message: types.Message):
    await message.answer(f"Политика конфидитеальности")