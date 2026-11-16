import asyncio, logging
from aiogram import Bot, Dispatcher
from config.settings import token
from handlers.start import rt as start
dp = Dispatcher()

async def main():
    bot = Bot(token)

    dp.include_router(start)

    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
