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
    con = sqlite3.connect("tutorial.db")
    cur = con.cursor()
    cur.execute("select * from status where id=(?)",[message.from_user.id])
    if len(cur.fetchall())==0:
        cur.execute('insert into status values(?,0)', [message.from_user.id])
    else:
        cur.execute('UPDATE status SET status=0 WHERE id=(?)',[message.from_user.id])
    con.commit()
    builder.add(types.InlineKeyboardButton(
        text="Спарсить",
        callback_data="pars")
    )
    builder.add(types.InlineKeyboardButton(
        text='Таргет-инвайт',
        callback_data='add'))
    builder.add(types.InlineKeyboardButton(
        text='СТАТА',
        callback_data='stat'))
    await message.answer(
        text="Выбирай-всегда start возвращает на этот этап", reply_markup=builder
    )
@dp.message_handler(commands=["statistick"])
async def cmd_start(message: types.Message):
    await message.answer(text="Пока нихуя нет , завтра будет ссори)")
@dp.message_handler(commands=["add_to_channel"])
async def cmd_start(message: types.Message):
    con = sqlite3.connect("tutorial.db")
    cur = con.cursor()
    cur.execute("delete  from spam where id_user=(?)", [message.from_user.id])
    cur.execute('UPDATE status SET status=-1 WHERE id=(?)', [message.from_user.id])
    con.commit()
    await message.answer("Введи сообщение - которое отправлять")

@dp.message_handler(commands=["pars_channel"])
async def cmd_start(message: types.Message):
    con = sqlite3.connect("tutorial.db")
    cur = con.cursor()
    cur.execute('UPDATE status SET status=1 WHERE id=(?)',[message.from_user.id])
    con.commit()
    await message.answer('Введи ссылку')



@dp.callback_query_handler(text='stat')
async def cmd_start(callback: types.CallbackQuery):
    await callback.message.answer(text="Пока нихуя нет , завтра будет ссори)")
@dp.callback_query_handler(text='add')
async def cmd_start(callback: types.CallbackQuery):
    con = sqlite3.connect("tutorial.db")
    cur = con.cursor()
    cur.execute("delete  from spam where id_user=(?)", [callback.from_user.id])
    cur.execute('UPDATE status SET status=-1 WHERE id=(?)', [callback.from_user.id])
    con.commit()
    await callback.message.answer("Введи сообщение - которое отправлять")


@dp.callback_query_handler(text='pars')
async def cmd_start(callback: types.CallbackQuery):
    con = sqlite3.connect("tutorial.db")
    cur = con.cursor()
    cur.execute('UPDATE status SET status=1 WHERE id=(?)',[callback.from_user.id])
    con.commit()
    await callback.message.answer('Введи ссылку')


@dp.message_handler()
async def cmd_start(message: types.Message):
    con = sqlite3.connect("tutorial.db")
    cur = con.cursor()
    cur.execute("select * from status where id=(?)", [message.from_user.id])
    status=cur.fetchall()[0][1]


    if status==1:
        con = sqlite3.connect("tutorial.db")
        cur = con.cursor()
        cur.execute("Insert into line values(?)",[message.text])
        con.commit()
        con.close()
        await message.answer('первая попытка , ожидай 2 минуты ')
        time.sleep(120)
        try:
            await message.answer_document(open(message.text.split('/')[-1]+'.txt','rb'))
        except:
            await message.answer('первая попытка , ожидай еще 4 минуты ')
            time.sleep(240)
            try:
                await message.answer_document(open(message.text.split('/')[-1]+'.txt','rb'))
            except:
                await message.answer('последняя  попытка , ожидай еще 12 минут ')
                time.sleep(720)
                await message.answer_document(open(message.text.split('/')[-1]+'.txt','rb'))


    elif status==-1:
        con = sqlite3.connect("tutorial.db")
        cur = con.cursor()
        cur.execute('insert into  spam  values(?,?,0)', [message.from_user.id,message.text])
        cur.execute('UPDATE status SET status=-10 WHERE id=(?)', [message.from_user.id])
        con.commit()
        await message.answer('Прошу ссылку на инвайт ')
    elif status==-10:
        con = sqlite3.connect("tutorial.db")
        cur = con.cursor()
        cur.execute('UPDATE spam SET tg_kanal=? WHERE id_user=?',[message.text,message.from_user.id])
        con.commit()
        cur.execute("select * from spam where id_user=(?)", [message.from_user.id])
        objects=cur.fetchall()
        await message.answer(text='Сообщение  :   '+objects[0][1])
        await message.answer(text='Таргет-канал  :   ' + objects[0][2])










async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
