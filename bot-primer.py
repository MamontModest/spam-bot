
import psycopg2
logging.basicConfig(level=logging.INFO)
bot = Bot(token="5698068722:AAHHYhhRj_uRFOOD8ngtVaPxlQH9yLI8XOQ")
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    connection = psycopg2.connect(user="postgres",
                                  # пароль, который указали при установке PostgreSQL
                                  password="data",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres_db")
    cursor = connection.cursor()
    cursor.execute("insert into kolesa (id,status) values(%s,%s)",[message.message_id,0])
    connection.commit()
    connection.close()
    name=message.from_user
    builder = types.InlineKeyboardMarkup()
    builder.add(types.InlineKeyboardButton(
        text="Оформить объявления",
        callback_data="1")
    )
    builder.add(types.InlineKeyboardButton(
        text="Архив объявлений",
        callback_data="2")
    )
    builder.add(types.InlineKeyboardButton(
        text="Список каналов",
        callback_data="3")
    )
    builder.add(types.InlineKeyboardButton(
        text="Связь с администратором",
        url="https://t.me/ad_mi_ni_st_ra_tor")
    )
    builder.add(types.InlineKeyboardButton(
        text="Узнать свою очередь",
        callback_data="4")
    )
    await message.answer(
        "Приветствуем, "+str(name.first_name)+" 📢С помощью этого бота Вы легко сможете разместить объявление о продаже своего авто, мотоцикла или колес/шин. \n\n  Чтобы составить объявление, перейдите в пункт 'Оформить объявление' и следуйте инструкции. Выберите интересующий пункт меню: ⬇️",
        reply_markup=builder
    )

@dp.callback_query_handler(text='0')
async def cmd_start(callback: types.CallbackQuery):
    builder = types.InlineKeyboardMarkup()
    builder.add(types.InlineKeyboardButton(
        text="Оформить объявления",
        callback_data="1")
    )
    builder.add(types.InlineKeyboardButton(
        text="Архив объявлений",
        callback_data="2")
    )
    builder.add(types.InlineKeyboardButton(
        text="Список каналов",
        callback_data="3")
    )
    builder.add(types.InlineKeyboardButton(
        text="Связь с администратором",
        url="https://t.me/ad_mi_ni_st_ra_tor")
    )
    builder.add(types.InlineKeyboardButton(
        text="Узнать свою очередь",
        callback_data="4")
    )
    await callback.message.answer(
                "Приветствуем, "+str(callback.message.from_user.first_name)+" 📢С помощью этого бота Вы легко сможете разместить объявление о продаже своего авто, мотоцикла или колес/шин. \n\n  Чтобы составить объявление, перейдите в пункт 'Оформить объявление' и следуйте инструкции. Выберите интересующий пункт меню: ⬇️",
        reply_markup=builder
    )

@dp.callback_query_handler(text="3")
async def send_random_value(callback: types.CallbackQuery):
    builder = types.InlineKeyboardMarkup()
    builder.add(types.InlineKeyboardButton(
        text="Московская область",
        url="https://t.me/auto_97")
    )
    builder.add(types.InlineKeyboardButton(
        text="Республика Татарстан",
        url="https://t.me/auto_16")
    )
    builder.add(types.InlineKeyboardButton(
        text="РСО-Алания",
        url="https://t.me/auto_15")
    )
    builder.add(types.InlineKeyboardButton(
        text="Нижегородская область",
        url="https://t.me/auto_52")
    )
    await callback.message.answer(
        "Ниже сылки на каналы , выберите канал",
        reply_markup=builder
    )


@dp.callback_query_handler(text="1")
async def cmd_start(callback: types.CallbackQuery):
    builder = types.InlineKeyboardMarkup()
    builder.add(types.InlineKeyboardButton(
        text="Автомобиль",
        callback_data="11")
    )
    builder.add(types.InlineKeyboardButton(
        text="Мотоцикл",
        callback_data="12")
    )
    builder.add(types.InlineKeyboardButton(
        text="Колеса/Шины",
        callback_data="13")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="14",)
    )

    await callback.message.answer(
        "Выберет раздел своего объявления",
        reply_markup=builder
    )

@dp.callback_query_handler(text="14")
async def cmd_start(callback: types.CallbackQuery):
    builder = types.InlineKeyboardMarkup()
    builder.add(types.InlineKeyboardButton(
        text="Оформить объявления",
        callback_data="1")
    )
    builder.add(types.InlineKeyboardButton(
        text="Архив объявлений",
        callback_data="2")
    )
    builder.add(types.InlineKeyboardButton(
        text="Список каналов",
        callback_data="3")
    )
    builder.add(types.InlineKeyboardButton(
        text="Связь с администратором",
        url="https://t.me/ad_mi_ni_st_ra_tor")
    )
    builder.add(types.InlineKeyboardButton(
        text="Узнать свою очередь",
        callback_data="5")
    )
    await callback.message.answer(
                        "Приветствуем, "+str(callback.message.from_user.first_name)+" 📢С помощью этого бота Вы легко сможете разместить объявление о продаже своего авто, мотоцикла или колес/шин. \n\n  Чтобы составить объявление, перейдите в пункт 'Оформить объявление' и следуйте инструкции. Выберите интересующий пункт меню: ⬇️",
        reply_markup=builder
    )

@dp.callback_query_handler(text="13")
async def cmd_start(callback: types.CallbackQuery):
    builder = types.InlineKeyboardMarkup()
    builder.add(types.InlineKeyboardButton(
        text="Колеса",
        callback_data="21")
    )
    builder.add(types.InlineKeyboardButton(
        text="Шины",
        callback_data="22")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="1")
    )
    await callback.message.answer(
    "📡Чтобы оформить пост, следуйте поэтапным инструкциям.\n   📌Выберите раздел:" ,
        reply_markup=builder
    )
@dp.callback_query_handler(text="21")
async def cmd_start(callback: types.CallbackQuery):
    builder = types.InlineKeyboardMarkup()
    connection = psycopg2.connect(user="postgres",
                                  # пароль, который указали при установке PostgreSQL
                                  password="data",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres_db")
    cursor = connection.cursor()

    cursor.execute("insert into kolesa (id,status) values(%s,%s)", [callback.message.message_id, 0])
    connection.commit()
    connection.close()
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="14")
    )
    await callback.message.answer(
    "📡Чтобы оформить пост, следуйте поэтапным инструкциям.\n   🖼Добавьте фото колес напродажу." ,
        reply_markup=builder
    )

@dp.message_handler(content_types="photo")
async def download_photo(message: types.Message):
    await bot.download_file_by_id(message.photo[-1].file_id,'text.jpeg')
    builder = types.InlineKeyboardMarkup()
    builder.add(types.InlineKeyboardButton(
        text="Б/У",
        callback_data="30")
    )
    builder.add(types.InlineKeyboardButton(
        text="Новое",
        callback_data="30")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="21")
    )
    await message.answer("🛠Укажите состояние колес.",reply_markup=builder)


@dp.callback_query_handler(text="30")
async def cmd_start(callback: types.CallbackQuery):
    builder = types.InlineKeyboardMarkup()
    builder.add(types.InlineKeyboardButton(
        text="Летние",
        callback_data="40")
    )
    builder.add(types.InlineKeyboardButton(
        text="Зимние",
        callback_data="40")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="21")
    )
    connection = psycopg2.connect(user="postgres",
                                  # пароль, который указали при установке PostgreSQL
                                  password="data",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres_db")
    cursor = connection.cursor()
    cursor.execute("update loxi set status=1 where id='2'")
    connection.commit()
    connection.close()
    await callback.message.answer(
    "☀️/❄️Укажите сезонность колес..\n  " ,
        reply_markup=builder
    )

@dp.callback_query_handler(text="40")
async def cmd_start(callback: types.CallbackQuery):
    builder = types.InlineKeyboardMarkup()
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="30")
    )
    await callback.message.answer(
    "🖊Укажите более подробную информацию о колёсах. \n\n  Например: Производитель, модель, диаметр, количество крепёжных отверстий и другое." ,
        reply_markup=builder
    )
@dp.callback_query_handler(text='80')
async  def opisanie2(callback:types.CallbackQuery):
    builder = types.InlineKeyboardMarkup()
    builder.add(types.InlineKeyboardButton(
        text="Рубль",
        callback_data="50")
    )
    builder.add(types.InlineKeyboardButton(
        text="Гривны",
        callback_data="50")
    )
    builder.add(types.InlineKeyboardButton(
        text="Тенге",
        callback_data="50")
    )
    builder.add(types.InlineKeyboardButton(
        text="Суммы",
        callback_data="50")
    )
    builder.add(types.InlineKeyboardButton(
        text="Доллар",
        callback_data="50")
    )
    builder.add(types.InlineKeyboardButton(
        text="Евро",
        callback_data="50")
    )
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="40")
    )
    await callback.message.answer(
        "💱Выберите валюту, в которой будет указана цена колес.",
        reply_markup=builder)
@dp.message_handler()
async  def opisanie(message:types.Message):
    connection = psycopg2.connect(user="postgres",
                                  # пароль, который указали при установке PostgreSQL
                                  password="data",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres_db")
    cursor = connection.cursor()
    cursor.execute("select status from loxi where id='2'")
    a = cursor.fetchall()
    status=a[0][0]
    if status==1:
        builder = types.InlineKeyboardMarkup()
        builder.add(types.InlineKeyboardButton(
            text="Рубль",
            callback_data="50")
        )
        builder.add(types.InlineKeyboardButton(
            text="Гривны",
            callback_data="50")
        )
        builder.add(types.InlineKeyboardButton(
            text="Тенге",
            callback_data="50")
        )
        builder.add(types.InlineKeyboardButton(
            text="Суммы",
            callback_data="50")
        )
        builder.add(types.InlineKeyboardButton(
            text="Доллар",
            callback_data="50")
        )
        builder.add(types.InlineKeyboardButton(
            text="Евро",
            callback_data="50")
        )
        builder.add(types.InlineKeyboardButton(
            text="Назад",
            callback_data="40")
        )
        cursor.execute("update loxi set status=2 where id='2'")
        connection.commit()
        connection.close()
        await message.answer(
            "💱Выберите валюту, в которой будет указана цена колес.",
            reply_markup=builder)

    if status == 2:
        builder = types.InlineKeyboardMarkup()
        builder.add(types.InlineKeyboardButton(
            text="Московская",
            callback_data="60"))
        builder.add(types.InlineKeyboardButton(
            text="Нижегородская",
            callback_data="60"))
        builder.add(types.InlineKeyboardButton(
            text="РСО",
            callback_data="60"))
        builder.add(types.InlineKeyboardButton(
            text="Татарстан",
            callback_data="60"))
        builder.add(types.InlineKeyboardButton(
            text="Назад",
            callback_data="50"))
        await message.answer(
            "🌍Укажите область/республику, в которой продаете колеса, используя кнопки:👇",
            reply_markup=builder
        )
        cursor.execute("update loxi set status=3 where id='2'")
        connection.commit()
        connection.close()
    if status==3:
        builder = types.InlineKeyboardMarkup()
        builder.add(types.InlineKeyboardButton(
            text="Назад",
            callback_data="60"))
        await message.answer(
            "📞Введите номер телефона: Например: +71231234567",
            reply_markup=builder
        )
        cursor.execute("update loxi set status=4 where id='2'")
        connection.commit()
        connection.close()
    if status==4:
        builder = types.InlineKeyboardMarkup()
        builder.add(types.InlineKeyboardButton(
            text="Д",
            callback_data="70"))
        builder.add(types.InlineKeyboardButton(
            text="Нет",
            callback_data="70"))
        builder.add(types.InlineKeyboardButton(
            text="Назад",
            callback_data="60"))
        await message.answer(
            "📲Добавить @username в объявление?",
            reply_markup=builder
        )
        cursor.execute("update loxi set status=1 where id='2'")
        connection.commit()
        connection.close()


@dp.callback_query_handler(text='50')
async def opisanie2(callback: types.CallbackQuery):
    builder = types.InlineKeyboardMarkup()
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="80"))
    connection = psycopg2.connect(user="postgres",
                                  # пароль, который указали при установке PostgreSQL
                                  password="data",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres_db")
    cursor = connection.cursor()
    cursor.execute("update loxi set status=2 where id='2'")
    connection.commit()
    connection.close()
    await callback.message.answer(
                "💲Укажите цену в выбранной валюте:",
                reply_markup=builder
        )
@dp.callback_query_handler(text='60')
async def opisanie2(callback: types.CallbackQuery):
    builder = types.InlineKeyboardMarkup()
    builder.add(types.InlineKeyboardButton(
        text="Назад",
        callback_data="50"))
    connection = psycopg2.connect(user="postgres",
                                  # пароль, который указали при установке PostgreSQL
                                  password="data",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres_db")
    cursor = connection.cursor()
    cursor.execute("update loxi set status=3 where id='2'")
    connection.commit()
    connection.close()
    await callback.message.answer(
                "🌍Введите место осмотра (город, поселок, деревня, пригород) выбранной области/республики.",
                reply_markup=builder
        )

@dp.callback_query_handler(text='70')
async def opisanie2(callback: types.CallbackQuery):
    await callback.message.answer('✅Ваше объявление готово!')
    builder = types.InlineKeyboardMarkup()
    builder.add(types.InlineKeyboardButton(
        text="Опубликовать ",
        callback_data="100"))
    builder.add(types.InlineKeyboardButton(
        text="Отменить ",
        callback_data="10000"))
    await callback.message.answer(
        "Опубликовать пост на канал?",
        reply_markup=builder
    )
@dp.callback_query_handler(text='100')
async def opisanie2(callback: types.CallbackQuery):
    builder = types.InlineKeyboardMarkup()
    builder.add(types.InlineKeyboardButton(
        text="🔄В главное меню ",
        callback_data="0"))
    await callback.message.answer(
        "✅Пост отправлен на проверку!   ⭐После проверки Вы получите уведомление об одобрении или отклонении поста.",
        reply_markup=builder
    )

























































































































async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())