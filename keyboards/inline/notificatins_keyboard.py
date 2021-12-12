from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


inline_btn1 = InlineKeyboardButton('15мин', callback_data='15')
inline_btn2 = InlineKeyboardButton('30мин', callback_data='30')
inline_btn3 = InlineKeyboardButton('45мин', callback_data='45')
inline_btn4 = InlineKeyboardButton('1час', callback_data='60')
inline_btn5 = InlineKeyboardButton('1.5часа', callback_data='90')
inline_btn6 = InlineKeyboardButton('2часа', callback_data='120')
set_time_keyboard = InlineKeyboardMarkup().add(inline_btn1,
                                               inline_btn2,
                                               inline_btn3,
                                               inline_btn4,
                                               inline_btn5,
                                               inline_btn6)