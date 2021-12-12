import asyncio
from .crypto_course import get_currency
from loader import dp, db


async def cycle_of_notification(time, chat_id):
    course = await get_currency()
    # qw = db.select_user(id=chat_id)
    # print(qw)
    setting_time = db.select_user(id=chat_id)[3]
    await dp.bot.send_message(chat_id=chat_id,
                              text=f"Настроен период отправки {time} мин, "
                                   f"с этого момента каждые {time} мин "
                                   f"я буду присылать курс BTC, ETH и DOGE\n"
                                   f"Актуальный курс:\n"
                                   f"{course}")
    while True:
        await asyncio.sleep(60*int(time))
        changed_time, time_of_changing = db.select_user(id=chat_id)[2], db.select_user(id=chat_id)[3]

        if int(time) == changed_time and setting_time != time_of_changing:
            break
        elif int(time) != changed_time:
            break

        course = await get_currency()
        await dp.bot.send_message(chat_id=chat_id, text=course)

