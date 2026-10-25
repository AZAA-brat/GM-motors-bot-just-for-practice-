from dotenv import load_dotenv
import asyncio
import logging
from logging_config import setup_logger
load_dotenv()
from config import dp, bot
import handlers.start as start

setup_logger()
dp.include_routers(start.router)
logger = logging.getLogger(__name__)

async def main():
    await dp.start_polling(bot)
if __name__ == '__main__':
    asyncio.run(main())

