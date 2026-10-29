from aiogram import Router, F
from database.storage import get_user_language
from utils.phrases import phrases, get_text

router = Router()
@router.message(F.text.in_(list(phrases["about"].values())))
async def about_page(message, db_pool):
    user_id = message.from_user.id
    language = await get_user_language(db_pool, user_id)
    await message.answer(get_text("about_explanation", language))


