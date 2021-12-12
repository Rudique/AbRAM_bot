from loader import dp
from aiogram import types
from aiogram.dispatcher.filters import Command
from utils.crypto_course import get_currency


@dp.message_handler(Command("course"))
async def course_command(message: types.Message):
    await dp.bot.delete_message(chat_id=message.from_user.id,
                                message_id=message.message_id)

    text = await get_currency()
    await dp.bot.send_message(chat_id=message.from_user.id,
                              text=text)


