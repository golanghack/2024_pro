import asyncio
import os
from environs import Env 
env = Env()
env.read_env()
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

token = env('TOKEN')
logging.basicConfig(level=logging.INFO)
bot = Bot(token=token)
dp = Dispatcher()


@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    await message.answer('Wow')
    
async def main():
    await dp.start_polling(bot)
    
if __name__ == '__main__':
    asyncio.run(main())
    