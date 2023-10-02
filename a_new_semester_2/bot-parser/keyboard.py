from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton

news = ReplyKeyboardMarkup(
    [
        [KeyboardButton(text='Політичні новини')],
        [KeyboardButton(text='Економічні новини')]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

choise = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(text='1', callback_data='1')],
        [InlineKeyboardButton(text='2', callback_data='2')]
    ],
    [
        [InlineKeyboardButton(text='Завершити перегляд', callback_data='0')]
    ]
)