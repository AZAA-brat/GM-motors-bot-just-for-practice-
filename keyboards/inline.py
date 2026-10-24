from keyboards.callbacks import LangCB
from aiogram import types
from aiogram.types import InlineKeyboardMarkup

lang_kb = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [types.InlineKeyboardButton(text="Özbekça 🇺🇿", callback_data=LangCB(language="uzbek").pack()),
         types.InlineKeyboardButton(text="English 🇬🇧", callback_data=LangCB(language="english").pack())],
        [types.InlineKeyboardButton(text="Русский 🇷🇺", callback_data=LangCB(language="russian").pack())]
    ]
)