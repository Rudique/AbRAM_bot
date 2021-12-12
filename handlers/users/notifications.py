from loader import dp, db
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from keyboards.inline import set_time_keyboard
from utils.notifications_by_time import cycle_of_notification
from datetime import datetime


@dp.message_handler(Command("notifications"), state=None)
async def notification_command(message: types.Message, state: FSMContext):

    await dp.bot.delete_message(chat_id=message.from_user.id,
                                message_id=message.message_id)

    await message.answer(text="Выберите период отправки оповещений",
                         reply_markup=set_time_keyboard)

    await state.set_state('SetNotification')


@dp.callback_query_handler(state='SetNotification')
async def set_time(callback: types.CallbackQuery, state: FSMContext):
    time = callback.data
    setting_time = str(datetime.now())[11:19]
    db.update_notification(time=time, setting_time=setting_time, id=callback.from_user.id)

    await dp.bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)
    await state.finish()
    await cycle_of_notification(time=time, chat_id=callback.from_user.id)



