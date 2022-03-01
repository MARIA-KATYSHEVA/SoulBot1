from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, Message, CallbackQuery
from create_bot import dp
from random import randint

# button1 = KeyboardButton('🛍️Каталог')
# button2 = KeyboardButton('🧭Расположение')
# button3 = KeyboardButton('🚚 Cпособы доставки')
# button4 = KeyboardButton('💳 Cпособы оплаты')

# button1 = KeyboardButton(text="Каталог")
# button2 = KeyboardButton(text='Расположение')
# button3 = KeyboardButton(text='Доставка')
# button4 = KeyboardButton(text='Оплата')

button1 = "/Каталог"
button2 = '/Расположение'
button3 = '/Доставка'
button4 = '/Оплата'

kb_client = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
# kb_client.add(button1).add(button2).add(button3).add(button4)
kb_client.row(button1, button2).row(button3, button4)

@dp.message_handler(commands="Доставка")
async def cmd_samovivoz(message: Message): #change foo name to normal
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(text="Самовывоз", callback_data="Самовывоз"))
    keyboard.add(InlineKeyboardButton(text="Доставка курьером", callback_data="Курьер"))
    await message.answer("Выберите подходящий вариант", reply_markup=keyboard)

@dp.callback_query_handler(text="Самовывоз")
async def send_samovivoz(call: CallbackQuery):
    await call.message.answer('Самовывоз ул. Садовая-Сухаревская 15с1 (Есть бесплатная парковка) Как добраться, Яндекс Карта (https://soulhygge.ru/kakdobratsya_showroom) • Режим работы Пн-Вс с 11.30 до 20.30')

@dp.callback_query_handler(text="Курьер")
async def send_samovivoz(call: CallbackQuery):
    await call.message.answer('по Москве внутри МКАД 2-3 дня — 350₽, за МКАД до 10 км 2-3 дня — 450₽ Пн-Вс с 11.30 до 21.00')
# @dp.message_handler(commands="Доставка")
# async def cmd_inline_url(message: Message):
#     buttons = [
#         InlineKeyboardButton(text="GitHub", url="https://github.com"),
#         InlineKeyboardButton(text="Оф. канал Telegram", url="tg://resolve?domain=telegram")
#     ]
#     keyboard = InlineKeyboardMarkup(row_width=1)
#     keyboard.add(*buttons)
#     await message.answer("Выберите  подходящий вариант", reply_markup=keyboard)

del1 = InlineKeyboardButton(text="Самовывоз", callback_data="Самовывоз")
del2 = InlineKeyboardButton(text="Доставка", callback_data="Доставка_курьером")
kb_delivery = InlineKeyboardMarkup(row_width=2)
kb_delivery.add(del1, del2)
# # kb_client = ReplyKeyboardMarkup(resize_keyboard=True) # если хочу спрятать кнопки - аргумент one_time_keyboard=True

# Друг под другом
# kb_client.add(button1).add(button2).add(button3)
# button1, а под ним в одном ряду button2 и button3
# kb_client.add(button1).add(button2).insert(button3)
# все в ряд
# kb_client.add(button1).add(button2).add(button3).row(button4, button5)



