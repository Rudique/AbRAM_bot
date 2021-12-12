from aiogram import executor

from loader import dp, db
import handlers
from utils.set_bot_commands import set_default_commands


async def on_startup(dp):

    try:
        db.create_table_users()
    except Exception as e:
        print(e)

    print(db.select_all_users())
    await set_default_commands(dp)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)

