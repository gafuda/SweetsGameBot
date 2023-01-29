from aiogram import executor
from handlers import dp


async def on_start(_):  # позволяет выполнять запрос "параллельно" - отправить запрос и идти дальше, не дожидаясь ответа
    print('Бот запущен')


executor.start_polling(dp, skip_updates=True, on_startup=on_start)  # чтобы принимать сообщения только тогда когда бот
# Запущен. On_startup запускает функцию скипа при запуске

