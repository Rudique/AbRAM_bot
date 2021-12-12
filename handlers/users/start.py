import sqlite3
import logging

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await dp.bot.delete_message(chat_id=message.from_user.id,
                                message_id=message.message_id)

    await message.answer(f"Шалом, {message.from_user.full_name}!\n"
                         f"Я криптобот АбRAM и я информирую о самом"
                         f" кошерном курсе BTC, ETH и DOGE\n"
                         f"Список комманд бота:\n"
                         f"/notifications - Установить интервал оповещений\n"
                         #f"/reminder - Установить напоминание\n"
                         f"/course - Актуальный курс крипты\n"
                         )
    try:
        db.add_user(id=message.from_user.id,
                    name=message.from_user.full_name)
    except sqlite3.IntegrityError as err:
        print(err)
