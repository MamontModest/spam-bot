import logging
from aiogram import Bot, Dispatcher, types
import asyncio
import sqlite3
import time
from telethon import TelegramClient
import os

logging.basicConfig(level=logging.INFO)
bot = Bot(token="5824231817:AAFPR3h9OpWU3UWEVyJ5FjxpyLeOZ7Rtm0w")
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    if message.from_user.id in ['302131629',302131629,3727766,1890767310,'1890767310','3727766']:
        builder = types.InlineKeyboardMarkup()
        con = sqlite3.connect("tutorial.db")
        cur = con.cursor()
        cur.execute("select * from status where id=(?)",[message.from_user.id])
        if len(cur.fetchall())==0:
            cur.execute('insert into status values(?,0)', [message.from_user.id])
        else:
            cur.execute('UPDATE status SET status=0 WHERE id=(?)',[message.from_user.id])
        con.commit()
        con.close()
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
    else:
        await message.answer('Пошел нахуй тебя не приглашали ')
@dp.message_handler(commands=["statistick"])
async def cmd_start(message: types.Message):
    if message.from_user.id in ['302131629',302131629,3727766, 1890767310, '1890767310', '3727766']:
        await message.answer(text="Пока нихуя нет , завтра будет ссори)")
    else:
        await message.answer('Пошел нахуй тебя не приглашали ')

@dp.message_handler(commands=["add_to_channel"])
async def cmd_start(message: types.Message):
    if message.from_user.id in ['302131629',302131629,3727766, 1890767310, '1890767310', '3727766']:
        con = sqlite3.connect("tutorial.db")
        cur = con.cursor()
        cur.execute("delete  from spam where id_user=(?)", [message.from_user.id])
        cur.execute('UPDATE status SET status=-1 WHERE id=(?)', [message.from_user.id])
        con.commit()
        con.close()
        await message.answer("Введи сообщение - которое отправлять")
    else:
        await message.answer('Пошел нахуй тебя не приглашали ')
@dp.message_handler(commands=["pars_channel"])
async def cmd_start(message: types.Message):
    if message.from_user.id in ['302131629',302131629,3727766, 1890767310, '1890767310', '3727766']:
        con = sqlite3.connect("tutorial.db")
        cur = con.cursor()
        cur.execute('UPDATE status SET status=1 WHERE id=(?)',[message.from_user.id])
        con.commit()
        con.close()
        await message.answer('Введи ссылку')
    else:
        await message.answer('Пошел нахуй тебя не приглашали ')

@dp.message_handler(commands=["delete_invite_history"])
async def cmd_start(message: types.Message):
    if message.from_user.id in ['302131629',302131629,3727766, 1890767310, '1890767310', '3727766']:
        con = sqlite3.connect("tutorial.db")
        cur = con.cursor()
        cur.execute('delete from pars  WHERE id_creatot=(?)',[message.from_user.id])
        con.commit()
        con.close()
        await message.answer('Очистили стек инвайтинга')
    else:
        await message.answer('Пошел нахуй тебя не приглашали ')
@dp.message_handler(commands=["invite_spisok"])
async def cmd_start(message: types.Message):
    if message.from_user.id in ['302131629',302131629,3727766, 1890767310, '1890767310', '3727766']:
        con = sqlite3.connect("tutorial.db")
        cur = con.cursor()
        cur.execute('select * from pars  WHERE id_creatot=(?)',[message.from_user.id])
        object=cur.fetchall()
        con.close()
        with open ("Готовый таргет список.txt",'a') as inf:
            for i in object:
                inf.write(str(i)+'\n')
        await message.answer_document(open("Готовый таргет список.txt", 'rb'))
        os.remove("Готовый таргет список.txt")
    else:
        await message.answer('Пошел нахуй тебя не приглашали ')



@dp.callback_query_handler(text='stat')
async def cmd_start(callback: types.CallbackQuery):
    if callback.from_user.id in ['302131629',302131629,3727766, 1890767310, '1890767310', '3727766']:
        await callback.message.answer(text="Пока нихуя нет , завтра будет ссори)")
    else:
        await callback.message.answer('Пошел нахуй тебя не приглашали ')
@dp.callback_query_handler(text='add')
async def cmd_start(callback: types.CallbackQuery):
    if callback.from_user.id in ['302131629',302131629,3727766, 1890767310, '1890767310', '3727766']:
        con = sqlite3.connect("tutorial.db")
        cur = con.cursor()
        cur.execute("delete  from spam where id_user=(?)", [callback.from_user.id])
        cur.execute('UPDATE status SET status=-1 WHERE id=(?)', [callback.from_user.id])
        con.commit()
        await callback.message.answer("Введи сообщение - которое отправлять")
    else:
        await callback.message.answer('Пошел нахуй тебя не приглашали ')


@dp.callback_query_handler(text='pars')
async def cmd_start(callback: types.CallbackQuery):
    if callback.from_user.id in ['302131629',302131629,3727766, 1890767310, '1890767310', '3727766']:
        con = sqlite3.connect("tutorial.db")
        cur = con.cursor()
        cur.execute('UPDATE status SET status=1 WHERE id=(?)',[callback.from_user.id])
        con.commit()
        await callback.message.answer('Введи ссылку')
    else:
        await callback.message.answer('Пошел нахуй тебя не приглашали ')

@dp.message_handler(content_types=['document'])
async def cmd_start(message: types.Message):
    if message.from_user.id in ['302131629',302131629,3727766, 1890767310, '1890767310', '3727766']:
        if message.document.file_name[-3:]=='txt':
            await message.document.download(destination_file=message.document.file_name,make_dirs=True)
            with open(message.document.file_name)as inf :
                con = sqlite3.connect("tutorial.db")
                cur = con.cursor()
                cur.execute("select * from spam where id_user=(?)", [message.from_user.id])
                object=cur.fetchall()
                for line in inf:
                    cur.execute("insert into pars values(?,?,?,?)",[object[0][0],object[0][1],object[0][2],line.strip()])
                con.commit()
                await message.answer('Записал , ночью начнем работу'            )
            os.remove(message.document.file_name)
        else:
            await message.answer('Принимаем файлы только расширения txt')
    else:
        await message.answer('Пошел нахуй тебя не приглашали ')


@dp.message_handler()
async def cmd_start(message: types.Message):
    if message.from_user.id in ['302131629',302131629,3727766, 1890767310, '1890767310', '3727766']:
        try:
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
                    os.remove(message.text.split('/')[-1] + '.txt')
                except:
                    await message.answer('первая попытка , ожидай еще 4 минуты ')
                    time.sleep(240)
                    try:
                        await message.answer_document(open(message.text.split('/')[-1]+'.txt','rb'))
                        os.remove(message.text.split('/')[-1] + '.txt')
                    except:
                        await message.answer('последняя  попытка , ожидай еще 12 минут ')
                        time.sleep(720)
                        await message.answer_document(open(message.text.split('/')[-1]+'.txt','rb'))
                        os.remove(message.text.split('/')[-1] + '.txt')


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
                await message.answer(text='Скидывай файл в формате txt')


        except:
            con = sqlite3.connect("tutorial.db")
            cur = con.cursor()
            cur.execute("delete from  line where tg_kanal=(?)", [message.text])
            con.commit()
            con.close()
            await message.answer('Где-то возникла непредвиденная ошибка')
    else:
        await message.answer('Пошел нахуй тебя не приглашали ')










async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
