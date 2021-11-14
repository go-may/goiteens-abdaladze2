from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default import mainmenu
from loader import dp

@dp.message_handler(text="/start")
async def bot_start(message: types.Message):
    await message.answer(f"Приветствую вас!", reply_markup=mainmenu)
    await message.answer(f"Пожалуйста введите свое имя", reply_markup=mainmenu)

@dp.message_handler(text_contains="Мое имя:")
async def examination_user_name(message: types.Message):
    user_name = str(message.text).replace('Мое имя:', '')
    user_name = user_name[1:len(user_name)]
    if user_name == message.from_user.full_name:
        await message.answer(f"Все правильно ваше имя совпадает")
    else:
        await message.answer(f"Неправильно ваше имя не совпадает")

@dp.message_handler(text="id")
async def user_id(message: types.Message):
    await message.answer(f'Ваш id: "{message.from_user.id}"', reply=True)

@dp.message_handler(text="nickname")
async def user_nickname(message: types.Message):
    await message.answer(f'Ваш nickname: "{message.from_user.first_name}"', reply=True)

@dp.message_handler(text="fullname")
async def user_nickname(message: types.Message):
    await message.answer(f'Ваше полное имя: "{message.from_user.full_name}"', reply=True)

@dp.message_handler(text="name")
async def user_nickname(message: types.Message):
    await message.answer(f'Ваше имя: "{message.from_user.last_name}"', reply=True)

@dp.message_handler(content_types="contact")
async def user_phone(message: types.Message):
    await message.answer(f"Ваш телефон был успешно получен")

@dp.message_handler(content_types="location")
async def user_location(message: types.Message):
    await message.answer(f"Ваша геолокация была успешно получена")