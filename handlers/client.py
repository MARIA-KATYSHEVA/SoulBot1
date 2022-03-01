from aiogram import types, Dispatcher
from create_bot import bot, dp
import sqlite3 as sq
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db

# base = sq.connect('HyggoSoul1.db')
# cur = base.cursor()
#
# def sql_start():
#     global base, cur
#     base = sq.connect('HyggoSoul1.db')
#     cur = base.cursor()
#     if base:
#         print('Data base connected OK!')
#     base.execute('CREATE TABLE IF NOT EXISTS catalog(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
#     base.commit()



# @dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id,
                           'Привет!✋ Я - бот онлайн-магазин натуральных свечей и ароматов для дома Soul Hygge! \n Я всегда готов помочь! Выбери в меню интересующую тебя кнопку 👇',
                           reply_markup=kb_client)


# @dp.message_handler(commands=['🛍️Каталог'])
async def catalog(message: types.Message):
    # await bot.send_message(message.from_user.id, 'Здесь скоро появится каталог!', reply_markup=kb_client)
    await sqlite_db.sql_read(message)
# async def catalog(message: types.Message):
#     for ret in cur.execute('SELECT * FROM calatog').fetchall():
#         await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}', reply_markup=kb_client)

# # @dp.message_handler(commands=['🧭Расположение'])
# async def address(message: types.Message):
#     await bot.send_message(message.from_user.id, 'Здесь скоро появятся адреса!', reply_markup=kb_client)


# @dp.message_handler(commands=['🚚 Cпособы доставки'])
async def delivery(message: types.Message):
    await message.reaply("Выберите подходящий вариант!", reply_markup = kb_delivery)

@dp.callback_query_handler(text = ["Самовывоз", "Доставка_курьером"])
async def delivery(call:types.CallbackQuery):
    if call.data == "Cамовывоз":
         await call.message.answer("Адрес")
    if call.data == "Доставка_курьером":
        await call.message.answer("Условия")
    await call.answer()

# @dp.message_handler(commands=['💳 Cпособы оплаты'])
async def payment(message: types.Message):
    await bot.send_message(message.from_user.id,'Оплата производится картой или электронным кошельком на нашем сайте  https://soulhygge.ru/', reply_markup = kb_client)


# @dp.message_handler(commands=['Расположение'])
async def address(message: types.Message):
    await bot.send_message(message.from_user.id, 'SOÛL HYGGE Шоурум находится по адресу: ул. Садовая-Сухаревская 15с1')


def register_handlers_client(dp: Dispatcher) -> object:
    dp.register_message_handler(command_start, commands=['start', 'help'])
    # dp.register_message_handler(catalog, commands=['🛍️Каталог'])
    # dp.register_message_handler(address, commands=['🧭Расположение'])
    # dp.register_message_handler(delivery, commands=['🚚 Cпособы доставки'])
    # dp.register_message_handler(payment, commands=['💳 Cпособы оплаты'])
    dp.register_message_handler(catalog, commands=['Каталог'])
    dp.register_message_handler(address, commands=['Расположение'])
    dp.register_message_handler(delivery, commands=['Доставка'])
    dp.register_message_handler(payment, commands=['Оплата'])

# @dp.message_handler(commands=['Каталог'])
# async def parket_catalog_command(message: types.Message):
#     await sqlite_db.sql_read(message)