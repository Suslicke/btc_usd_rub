import asyncio

from aiogram import Bot, Dispatcher, executor, types
from confing import token, user_id
from main import priceUSD, priceRUB
from aiogram.dispatcher.filters import Text

bot = Bot(token=token)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    start_buttons = ['Цена USD', 'Цена RUB']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)
    await message.answer('Цена биткоина', reply_markup=keyboard)


@dp.message_handler(Text(equals='Цена USD'))
async def get_price(message: types.Message):
    await message.answer(priceUSD)


@dp.message_handler(Text(equals='Цена RUB'))
async def get_price(message: types.Message):
    await message.answer(priceRUB)


async def news_every_minute():
    while True:
        await bot.send_message(user_id, priceUSD, disable_notification=False)
        await bot.send_message(user_id, priceRUB, disable_notification=False)

        await asyncio.sleep(604800)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(news_every_minute())
    executor.start_polling(dp)