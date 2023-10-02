import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from bs4 import BeautifulSoup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import requests
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup

def parse_default_news(date=None):
    links = []
    result = []
    if not date:
        response = requests.get("https://www.pravda.com.ua/news/")
        soup =  BeautifulSoup(response.content, "html.parser")

        headers = soup.select(".article_header > a")
        for link in headers[:3]:
            l = link.get("href")
            links.append(l)
load_dotenv()

TOKEN=os.getenv('TOKEN')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())
ADMINS = [5888056812]



def get_vacancies(vacancy_title: str):
    correct_title = vacancy_title.replace(' ', '+')
    url = f"https://www.work.ua/jobs-{correct_title}"
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'})
    print(response.status_code)
    soup = BeautifulSoup(response.content, 'html.parser')
    jobs_soup = soup.select('.job-link')
    result = []

    for job in jobs_soup:
        title = job.select_one('h2 > a').text
        releative_job_url = job.select_one('h2 > a').get('href')
        job_url = f'https://www.work.ua{releative_job_url}'
        company = job.select_one('.add-top-xs > span > b').text
        description = job.select_one('p').text.strip().replace('\n', '').replace('                           ', '').replace('\\xa0', '').replace('\u2060', '')
    
        job_obj = {
            "title": title,
            "url": job_url,
            "company": company,
            "description": description
        }
        print(job_obj)
        result.append(job_obj)
    return result



@dp.message_handler(commands=['start'])
async def country_info(message: types.Message):
    await bot.send_message(message.from_user.id, "This is your book:")
    second_wors = message.text.split()[1]
    country = {
    "1":{
    "Region":"Language Implementation Patterns: Techniques for Implementing Domain-Specific Languages",
    "Capital":"Terrence Parr",
    "Population":"Knowing how to create domain-specific languages (DSLs) can give you a huge productivity boost. Instead of writing code in a general-purpose programming language, you can first build a custom language tailored to make you efficient in a particular domain",
    "Size":"3.85",
    "Language":"2009",
    "Density":"https://www.goodreads.com/book/show/6770855-language-implementation-patterns",
    },
    "2":{
    "Region":"The Theory of Parsing, Translation, and Compiling Volume 1: Parsing",
    "Capital":"Alfred V. Aho, Jeffrey D. Ullman",
    "Population":"Empty",
    "Size":"3.81",
    "Language":"1972",
    "Density":"https://www.goodreads.com/book/show/1041619.The_Theory_of_Parsing_Translation_and_Compiling_Volume_1",
    },
    "3":{
    "Region":"The Theory of Parsing, Translation, and Compiling Part2",
    "Capital":"Alfred V. Aho, Jeffrey D. Ullman",
    "Population":"Empty",
    "Size":"3.54",
    "Language":"1973",
    "Density":"https://www.goodreads.com/book/show/112271.The_Theory_of_Parsing_Translation_and_Compiling",
    },
    "4":{
    "Region":"DSL Engineering: Designing, Implementing and Using Domain-Specific Languages",
    "Capital":"Markus Volter",
    "Population":"From introduction:This book is about creating domain-specific languages. It covers three main aspects: DSL design, DSL implementation and software engineering with DSLs. The book only looks at external DSLs and focuses mainly on textual syn-tax",
    "Size":"4.22",
    "Language":"2013",
    "Density":"https://www.goodreads.com/book/show/17287508-dsl-engineering",
    },
    "5":{
    "Region":"Parsing Techniques: A Practical Guide",
    "Capital":"Dick Grune, Ceriel J.H.Jacobs",
    "Population":"This second edition of Grune and Jacobs’ brilliant work presents new developments and discoveries that have been made in the field. Parsing, also referred to as syntax analysis, has been and continues to be an essential part of computer science and linguistics. Parsing techniques have grown considerably in importance, both in computer science, ie. advanced compilers often use general CF parsers, and computational linguistics where such parsers are the only option. They are used in a variety of software products including Web browsers, interpreters in computer devices, and data compression programs; and they are used extensively in linguistics",
    "Size":"4.29",
    "Language":"1973",
    "Density":"https://www.goodreads.com/book/show/112271.The_Theory_of_Parsing_Translation_and_Compiling",
    },
    "6":{
    "Region":"The Definitive ANTLR Reference: Building Domain-Specific Languages",
    "Capital":"Terence Parr",
    "Population":"ANTLR v3 is the most powerful, easy-to-use parser generator built to date, and represents the culmination of more than 15 years of research by Terence Parr. This book is the essential reference guide to using this completely rebuilt version of ANTLR, with its amazing new LL( ) parsing technology, tree construction facilities, StringTemplate code generation template engine, and sophisticated ANTLRWorks GUI development environment",
    "Size":"3.5",
    "Language":"2008",
    "Density":"https://www.goodreads.com/book/show/1063700.The_Definitive_ANTLR_Reference",
    },
    "7":{
    "Region":"The Functional Treatment of Parsing",
    "Capital":"Rene Leemakers",
    "Population":"Parsing technology traditionally consists of two branches, which correspond to the two main application areas of context-free grammars and their generalizations. Efficient deterministic parsing algorithms have been developed for parsing programming languages, and quite different algorithms are employed for analyzing natural language",
    "Size":"4.30",
    "Language":"2003",
    "Density":"https://www.goodreads.com/book/show/1756599.Parsing_Techniques",
    },
    }
    if second_wors in country.keys():
           name = country[second_wors]["Region"],
           capital = country[second_wors]["Capital"],
           population = country[second_wors]["Population"],
           size = country[second_wors]["Size"],
           language = country[second_wors]["Language"],
           desity = country[second_wors]["Density"],
           await bot.send_message(message.from_user.id, f"Name:{name},\n By:{capital},\n Description:{population},\n Ratting:{size},\n Year:{language},\n Url:{desity}")
    else:
        await bot.send_message("Book not found!")




async def set_default_commands(dp):
    await bot.set_my_commands(
        [
        types.BotCommand("start", "Запустити бота"),
        ]
    )






async def on_startup(dispatcher):
    await set_default_commands(dispatcher)



if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
