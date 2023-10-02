import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from steps import *
from database import Database

TOKEN=''

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands="start")
async def start_process(message: types.Message):
    await message.answer("Welcome!\nI am a database bot!")
    await Registration.set_name.set()

@dp.message_handler(state=Registration.set_name) 
async def set_name(message: types.Message, state: FSM)
    async    with state.proxy() as data :
        data["name"] = message.text
    await message.answer("Nice!\nNow enter your age")
    await Registration.set_email.set()

@dp.message_handler(state=Registration.set_email)
async def set_email(message: types.Message, state: FSMContext)
    async with state.proxy() as data:
        name = data["name"]
        age = data["age"]
        email = message.text
    #await db.register_student(name, age, email)
   # await message.answer("You have been registered")
    await state.finish()





if __name__ == '__main__':
    executor.start_polling(dp)