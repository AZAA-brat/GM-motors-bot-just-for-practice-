from dotenv import load_dotenv
from aiogram import Dispatcher
import asyncio
import logging
from logging_config import setup_logger
load_dotenv()
from config import dp, bot
import handlers.start as start
import handlers.about as about
import database.storage as st

setup_logger()
dp.include_routers(start.router, about.router)
logger = logging.getLogger(__name__)

async def on_startup(dispatcher: Dispatcher) -> None:
    pool = st.create_pool()
    dispatcher["db_pool"] = pool
    await st.init_db(pool)


async def on_shutdown(dispatcher: Dispatcher) -> None:
    pool = dispatcher.workflow_data.get("db_pool")
    if pool is not None:
        await st.close_db(pool)

dp.startup.register(on_startup)
dp.shutdown.register(on_shutdown)

async def main():
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(
        main(),
        loop_factory=asyncio.SelectorEventLoop
    )

