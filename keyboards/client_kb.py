from aiogram import types

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, Message, CallbackQuery, FSMContext
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

kb_client = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, selective= True, one_time_keyboard=True)


kb_client.row(button1, button2).row(button3, button4)

back_message = '← Назад в меню'
def back_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add(back_message)

    return markup

@dp.message_handler(commands="Доставка")
async def cmd_samovivoz(message: Message, state: FSMContext):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(text="📦 Самовывоз", callback_data="Самовывоз"))
    keyboard.add(InlineKeyboardButton(text="🚗 Курьером по Москве", callback_data="Курьер"))
    keyboard.add(InlineKeyboardButton(text="🚚 За МКАД свыше 10 км", callback_data="МКАД"))
    keyboard.add(InlineKeyboardButton(text="🌍 Другие страны", callback_data="Страны"))
    await message.answer("⭐ Если свечи в наличии, отправка происходит на следующий рабочий день.\n⭐⭐ В период 10-31 декабря отправка может происходить через 3-5 дня с момента оплаты.\n\nВыберите подходящий вариант ↓", reply_markup=keyboard)

@dp.callback_query_handler(text="Самовывоз")
async def send_samovivoz(call: CallbackQuery):
    await call.message.answer('Шоурум SOÛL HYGGE находится по адресу: ул. Садовая-Сухаревская 15с1 (Есть бесплатная парковка)\n\nРежим работы: Пн-Вс с 11.30 до 20.30\n\nКак добраться по Яндекс Карте: (https://soulhygge.ru/kakdobratsya_showroom)', reply_markup=back_markup())

@dp.callback_query_handler(text="Курьер")
async def send_samovivoz(call: CallbackQuery):
    await call.message.answer('Время доставки: Пн-Вс с 11.30 до 21.00:\n\nДоставка производится по Москве внутри МКАД 2-3 дня — 350 ₽, за МКАД до 10 км 2-3 дня — 450 ₽', reply_markup=back_markup())

@dp.callback_query_handler(text="МКАД")
async def send_samovivoz(call: CallbackQuery):
    await call.message.answer('Доставка за МКАД свыше 10км и по России транспортной компанией СДЭК - 450₽ от 2 до 16 дней\n\nДоставка по РФ Почтой России - рассчитывается индивидуально', reply_markup=back_markup())

@dp.callback_query_handler(text="Страны")
async def send_samovivoz(call: CallbackQuery):
    await call.message.answer('Расчёт доставки в другие страны можно сделать на сайте Почта России: https://www.pochta.ru/parcels\n\nДоставка производится от 7 до 22 дней', reply_markup=back_markup())

@dp.message_handler(commands="Расположение")
async def cmd_points(message: Message, state: FSMContext):
    keyboard2 = InlineKeyboardMarkup()
    keyboard2.add(InlineKeyboardButton(text="📍 Москва", callback_data="Москва"))
    keyboard2.add(InlineKeyboardButton(text="📍 Мытищи", callback_data="Мытищи"))
    keyboard2.insert(InlineKeyboardButton(text="📍 Санкт-Петербург", callback_data="Санкт-Петербург"))
    keyboard2.add(InlineKeyboardButton(text="📍 Хабаровск", callback_data="Хабаровск"))
    keyboard2.insert(InlineKeyboardButton(text="📍 Тольятти", callback_data="Тольятти"))
    keyboard2.add(InlineKeyboardButton(text="📍 Казахстан", callback_data="Казахстан"))
    keyboard2.insert(InlineKeyboardButton(text="📍 Иркутск", callback_data="Иркутск"))
    keyboard2.add(InlineKeyboardButton(text="📍 Екатеринбург", callback_data="Екатеринбург"))
    keyboard2.insert(InlineKeyboardButton(text="📍 Якутия", callback_data="Якутия"))
    keyboard2.add(InlineKeyboardButton(text="📍 Петрозаводск", callback_data="Петрозаводск"))
    keyboard2.insert(InlineKeyboardButton(text="📍 Уссурийск", callback_data="Уссурийск"))
    await message.answer("В этом разделе представлены наши точки продаж ", reply_markup=keyboard2)

@dp.callback_query_handler(text="Москва")
async def cmd_points(call: CallbackQuery):
    await call.message.answer('Здесь будут добавлены адреса и карты для г. Москва')

@dp.callback_query_handler(text="Мытищи")
async def cmd_points(call: CallbackQuery):
    await call.message.answer('Здесь будут добавлены адреса и карты для г. Мытищи')

@dp.callback_query_handler(text="Санкт-Петербург")
async def cmd_points(call: CallbackQuery):
    await call.message.answer('Здесь будут добавлены адреса и карты для г. Санкт-Петербург')

@dp.callback_query_handler(text="Хабаровск")
async def cmd_points(call: CallbackQuery):
    await call.message.answer('Здесь будут добавлены адреса и карты для г. Хабаровск')

@dp.callback_query_handler(text="Казахстан")
async def cmd_points(call: CallbackQuery):
    await call.message.answer('Здесь будут добавлены адреса и карты для Казахстана')

@dp.callback_query_handler(text="Иркутск")
async def cmd_points(call: CallbackQuery):
    await call.message.answer('Здесь будут добавлены адреса и карты для г. Иркутск')

@dp.callback_query_handler(text="Екатеринбург")
async def cmd_points(call: CallbackQuery):
    await call.message.answer('Здесь будут добавлены адреса и карты для г. Екатеринбург')

@dp.callback_query_handler(text="Якутия")
async def cmd_points(call: CallbackQuery):
    await call.message.answer('Здесь будут добавлены адреса и карты для Якутии')

@dp.callback_query_handler(text="Петрозаводск")
async def cmd_points(call: CallbackQuery):
    await call.message.answer('Здесь будут добавлены адреса и карты для г. Петрозаводск')

@dp.callback_query_handler(text="Уссурийск")
async def cmd_points(call: CallbackQuery):
    await call.message.answer('Здесь будут добавлены адреса и карты для г. Уссурийск')


# @dp.message_handler(commands="Самовывоз", "Курьером по Москве","За МКАД свыше 10 км", "Другие страны")
# async def back_button(message: Message): #change foo name to normal
#    keyboard2 = InlineKeyboardMarkup()
#    keyboard2.add(InlineKeyboardButton(text="Назад", callback_data="Назад"))
#    await message.answer("Кнопка назад",reply_markup=keyboard2)
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



