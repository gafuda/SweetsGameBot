from aiogram import types
from loader import dp

total = 150


@dp.message_handler(commands=['start', 'старт'])
async def mes_start(message: types.Message):
    print(message)
    await message.answer(f'Привет! Я бот для игры в конфеты. Я умею: '
                         f'/set 3453 - для выбора количества конфет (по окончании игры, например'
                         f'/set 3453 - для выбора количества конфет (по окончании игры, например')


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
    if message.text.isdigit():
        total -= int(message.text)
        if total <= 0:
            await message.answer('Победа!')
            total = 150
        else:
            await message.answer(f'{message.from_user.first_name} взял {message.text} конфет. '
                                 f'На столе осталось {total}')


