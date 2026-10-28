from aiogram import Router
from aiogram.filters import Command
from database.storage import get_user_language, ensure_user_language
from keyboards.inline import lang_kb
from utils.phrases import get_text

router = Router()
@router.message(Command("start"))
async def start_handler(message, db_pool):
    user_id = message.from_user.id
    await ensure_user_language(db_pool, user_id)
    language = await get_user_language(db_pool, user_id)
    keyboard = lang_kb
    await message.answer(get_text("start", language), reply_markup=keyboard)