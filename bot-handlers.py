import configparser
import logging
from aiogram import Bot, Dispatcher, types
import asyncio
import sqlite3
import time
from telethon import TelegramClient

logging.basicConfig(level=logging.INFO)
bot = Bot(token="5824231817:AAFPR3h9OpWU3UWEVyJ5FjxpyLeOZ7Rtm0w")
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    builder = types.InlineKeyboardMarkup()
    with open('status.txt','w') as inf:
        inf.write('None')
    builder.add(types.InlineKeyboardButton(
        text="Спарсить",
        callback_data="1")
    )
    builder.add(types.InlineKeyboardButton(
        text='добавить',
        callback_data='-1'))
    await message.answer(
        text="Выбирай-всегда start возвращает на этот этап", reply_markup=builder
    )


@dp.callback_query_handler(text='-1')
async def cmd_start(callback: types.CallbackQuery):
    await callback.message.answer("Введи сообщение - которое отправлять")




@dp.callback_query_handler(text='1')
async def cmd_start(callback: types.CallbackQuery):
    with open('status.txt', 'w') as inf:
        inf.write('1')
    await callback.message.answer('Введи сылку')


@dp.message_handler()
async def cmd_start(message: types.Message):
    with open('status.txt','r') as inf:
        status=inf.readline()
    if status=='1':
        con = sqlite3.connect("tutorial.db")
        cur = con.cursor()
        cur.execute("Insert into line values(?)",[message.text])
        con.commit()
        con.close()
        time.sleep(3)
        with open('status.txt', 'w') as inf:
            inf.write('None')
        await message.answer_document(open('status.txt','rb'))









async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
