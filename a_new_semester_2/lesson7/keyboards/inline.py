from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

first = InlineKeyboardMarkup(
    inline_keyboard=[
        InlineKeyboardButton(text="Button 1", callback_data="second")
    ]
)