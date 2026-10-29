from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from utils.phrases import get_text
def first_reply(lang) :
    choice_kb = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text=get_text("test_drive", lang)),
         KeyboardButton(text=get_text("buy_a_car", lang))],
        [KeyboardButton(text=get_text("lookup", lang)),
         KeyboardButton(text=get_text("review", lang))],
        [KeyboardButton(text=get_text("request", lang)),
         KeyboardButton(text=get_text("about", lang))],
        [KeyboardButton(text=get_text("show_contacts", lang))]
    ],
        resize_keyboard=True
    )
    return choice_kb