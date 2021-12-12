from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("notifications", "Установить интервал оповещений"),
            #types.BotCommand("reminder", "Установить напоминание"),
            types.BotCommand("course", "Актуальный курс крипты")
        ]
    )