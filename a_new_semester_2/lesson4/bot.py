import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN=os.getenv("TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage)


@dp.messsage_handler(text="Hello")
async def greeting(message: types.Message):
    name = message.from_user.full_name
    await message.answer(f"Hello {name}. \nMy name is Geralt")

@dp.message_handler(commands=["info"])
async def user_info(message: types.Message):
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    username = message.fron_user.username
    telegram_id = message.from_id
    lang = message.from_user.language_code

    await message.answer(f"ID: {telegram_id}\nFIRST NAME:{first_name}\nLAST NAME:{last_name}\nUSERNAME:{username}\nLang: {lang}")

@dp.messsage_handler(content_types=types.ContentTypes)
async def echo_stiker(message:types.Message):
    await message.answer_sticker(message.sticker.file_id)


@dp.message_handler(content_types="text")
async def echo(message: types.Message):
    if message.text == "Weather":
        await message.answer("bebebebe")
    else:
        await message.answer(message.text)
    


if __name__ == "__main__":
    executor.start_polling