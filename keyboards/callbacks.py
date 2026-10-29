from aiogram.filters.callback_data import CallbackData

LANG_MAP = {
    "uzbek": "uz",
    "english": "en",
    "russian": "ru",
}

class LangCB(CallbackData, prefix="language"):
    language: str
