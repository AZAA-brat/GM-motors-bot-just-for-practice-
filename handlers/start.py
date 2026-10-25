from aiogram import Router
from aiogram.filters import Command

from utils.phrases import get_text
from keyboards.inline import lang_kb

router = Router()
@router.message(Command("start"))
async def start_handler(message):
    await message.answer(get_text("intro", message.from_user.id), reply_markup=lang_kb)