import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage


import os
from dotenv import load_dotenv

from untils import check_query
from parse import get_vacancies

load_dotenv()

TOKEN=os.getenv('TOKEN')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(f"Hello! Enter your requests: ")

@dp.message_handler(commands='text')
async def get_jobs(message: types.Message):
    if check_query(message.text):
        await message.answer('Please enter again your research with space')
    else:
        query = message.text.lower().strip
        vacancies = get_vacancies(query)
        for vacancy in vacancy:
            title = vacancy['title']
            company = vacancy['company']
            url = vacancy['url']
            description = vacancy['description']

            msg = f'Vacancy: {title}\nCompany: {company}\nDescription: {description}\nURL:{url}'
            await message.answer(text=msg, parse_mode='.html')


if __name__ == '__main__':
    executor.start_polling(dp)