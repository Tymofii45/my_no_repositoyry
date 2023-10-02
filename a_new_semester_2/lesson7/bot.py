import logging
from aiogram import types, Dispatcher, Bot, executor
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from keyboards.inline import first
from keyboards.default import keyboard
logging.basicConfig(logging.INFO, filename="log.txt")

bot = Bot("6295899496:AAHDDd8tmAxELvPlb5wdyUNwB_K-jkzbwRo")
dp = Dispatcher(bot, storage=MemoryStorage)

@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.answer(text="Hello")

@dp.message_handler(content_types="text")
async def echo(message: types.Message):
    await message.answer(text="Press this button!", reoly_markup=first)


@dp.callback_query_handler(text="second")
async def second_step(callback: types.CallbackQuery):
    await callback.message.answer("You have already pressed.")


@dp.message_handler(commands="choose_color")
async def choose_color(message:):


if __name__ == "__main__":
    executor.start_polling
