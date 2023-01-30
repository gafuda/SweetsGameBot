from aiogram import types
from loader import dp
from random import *

total = 150
bot_tern = 0
max_ = 28
draw = randint(1, 3)


@dp.message_handler(commands=['start', 'старт'])
async def mes_start(message: types.Message):
    print(message)
    await message.answer(f'Привет! Я бот для игры в конфеты.  '
                         f'/set 3453 - чтобы задать количество конфет после окончания игры')


@dp.message_handler(commands=['set'])
async def mes_help(message: types.Message):
    global total
    count = message.text.split()[1]
    if count.isdigit():
        total = int(count)
        await message.answer(f'Конфет теперь {count}')


@dp.message_handler()
async def mes_all(message: types.Message):
    global total
    if message.text.isdigit() and int(message.text) < max_:
        total -= int(message.text)
        if total <= 0:
            await message.answer('Умничка,  ты победил!')
            total = 150
        else:
            await message.answer(f'{message.from_user.first_name} взял {message.text} конфет. '
                                 f'На столе осталось {total}')
            global bot_tern
            bot_tern = randint(1, 29)
            total -= int(bot_tern)
            await message.answer(f'Я забираю {bot_tern} конфет.'
                                 f'На столе осталось {total}')
            if total <= 0:
                await message.answer('Победил бот!')
                total = 150
    else:
        await message.answer('Введи число не больше 28 конфет!')
