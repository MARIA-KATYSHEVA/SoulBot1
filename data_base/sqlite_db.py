import sqlite3 as sq
import create_bot
from create_bot import bot, dp
import base64


def sql_start():
    global base, cur
    base = sq.connect('HyggoSoul3.db')
    cur = base.cursor()
    if base:
        print('Data base connected OK!')
    base.execute('CREATE TABLE IF NOT EXISTS catalog(img TEXT, name TEXT PRIMARY KEY, type TEXT, price TEXT)')
    base.commit()


# Эта функция будет вносить изменения в базу данных
async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO catalog VALUES (?, ?, ?, ?)', tuple(data.values()))
        base.commit()

async def sql_read(message):
    for ret in cur.execute('SELECT * FROM catalog').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nЦена {ret[-1]} ₽')

async def sql_read2(message):
    return cur.execute('SELECT * FROM catalog').fetchall()

async def sql_delete_command(data):
    return cur.execute('DELETE FROM catalog WHERE name ==?',(data,))
    base.commit()

async def natural_canldes(message):
    for ret in cur.execute("SELECT * FROM catalog WHERE type = 'Натуральные_свечи'").fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nЦена {ret[-1]} ₽')

async def diffuzers(message):
    for ret in cur.execute("SELECT * FROM catalog WHERE type = 'Диффузоры'").fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nЦена {ret[-1]} ₽')