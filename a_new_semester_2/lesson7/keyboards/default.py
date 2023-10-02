from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

colors = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Red'),
            KeyboardButton(text='Green'),
            KeyboardButton(text='Blue')
        ]
    ],
    one_time_keyboard=True
)