from aiogram import types, Dispatcher
from create_bot import bot, dp
import sqlite3 as sq

from data_base.sqlite_db import natural_canldes
from keyboards import kb_client, kb_delivery
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
                           'Привет!✋\n\nРады привествовать Вас в онлайн-магазине натуральных свечей и ароматов для дома Soul Hygge!\n\nВыбери в меню интересующую тебя кнопку 👇',
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

async def natural(message: types.Message):
    # await bot.send_message(message.from_user.id, 'Здесь отображется категория Натуральные_свечи!', reply_markup=kb_client)
    await sqlite_db.natural_canldes(message)

async def diff(message: types.Message):
    # await bot.send_message(message.from_user.id, 'Здесь отображется категория Диффузоры!', reply_markup=kb_client)
    await sqlite_db.diffuzers(message)

# @dp.message_handler(commands=['🚚 Cпособы доставки'])
async def delivery(message: types.Message):
    await message.reply("Выберите подходящий вариант ↓", reply_markup = kb_delivery)


@dp.callback_query_handler(text = ["📦 Самовывоз", "🚗 Курьером по Москве", "🚚 За МКАД свыше 10 км", "🌍 Другие страны"])
async def delivery(call:types.CallbackQuery):
    if call.data == "📦 Самовывоз":
         await call.message.answer("")
    if call.data == "🚗 Курьером по Москве":
        await call.message.answer("")
    if call.data == "🚚 За МКАД свыше 10 км":
        await call.message.answer("")
    if call.data == "🌍 Другие страны":
        await call.message.answer("Условия")
    await call.answer()

async def delivery(message: types.Message):
    await message.reply("Выберите подходящий вариант ↓", reply_markup = kb_delivery)


# @dp.callback_query_handler(text = ["Натуральные свечи", "Диффузеры"])
# async def catalog(call:types.CallbackQuery):
#    if call.data == "Натуральные свечи":
#         await call.message.answer("Натуральные свечи")
#    if call.data == "Диффузоры":
#        await call.message.answer("Диффузоры")
#    await call.answer()


# @dp.message_handler(commands=['💳 Cпособы оплаты'])
async def payment(message: types.Message):
    await bot.send_message(message.from_user.id,'Оплата производится картой или электронным кошельком на нашем сайте  https://soulhygge.ru/', reply_markup = kb_client)

@dp.callback_query_handler(text = ["📍 Москва", "📍 Мытищи", "📍 Санкт-Петербург", "📍 Хабаровск", "📍 Тольятти", "📍 Казахстан", "📍 Иркутск", "📍 Екатеринбург", "📍 Якутия", "📍 Петрозаводск", "📍 Уссурийск"])
async def delivery(call:types.CallbackQuery):
    if call.data == "📍 Москва":
         await call.message.answer("")
    if call.data == "📍 Мытищи":
        await call.message.answer("")
    if call.data == "📍 Санкт-Петербург":
        await call.message.answer("")
    if call.data == "📍 Хабаровск":
        await call.message.answer("")
    if call.data == "📍 Тольятти":
        await call.message.answer("")
    if call.data == "📍 Казахстан":
        await call.message.answer("")
    if call.data == "📍 Иркутск":
        await call.message.answer("")
    if call.data == "📍 Екатеринбург":
        await call.message.answer("")
    if call.data == "📍 Якутия":
        await call.message.answer("")
    if call.data == "📍 Петрозаводск":
        await call.message.answer("")
    if call.data == "📍 Уссурийск":
        await call.message.answer("")
    await call.answer()

# @dp.message_handler(commands=['Расположение'])
async def address(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите Ваш город ↓', reply_markup = kb_delivery)


def register_handlers_client(dp: Dispatcher) -> object:
    dp.register_message_handler(command_start, commands=['start', 'help'])
    # dp.register_message_handler(catalog, commands=['🛍️Каталог'])
    # dp.register_message_handler(address, commands=['🧭Расположение'])
    # dp.register_message_handler(delivery, commands=['🚚 Cпособы доставки'])
    # dp.register_message_handler(payment, commands=['💳 Cпособы оплаты'])
    dp.register_message_handler(catalog, commands=['Каталог'])
    dp.register_message_handler(natural_canldes, commands=['Natural'])
    dp.register_message_handler(diff, commands=['Diffuser'])
    dp.register_message_handler(address, commands=['Расположение'])
    dp.register_message_handler(delivery, commands=['Доставка'])
    dp.register_message_handler(payment, commands=['Оплата'])

# @dp.message_handler(commands=['Каталог'])
# async def parket_catalog_command(message: types.Message):
#     await sqlite_db.sql_read(message)