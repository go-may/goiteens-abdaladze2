from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

mainmenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="id"),
            KeyboardButton(text="nickname"),
        ],
        [
            KeyboardButton(text="fullname"),
            KeyboardButton(text="name"),
        ],
        [
            KeyboardButton(text="Phone", request_contact=True),
            KeyboardButton(text="Location", request_location=True),
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)