import asyncio, logging
from aiogram import Bot, Dispatcher
from config.settings import token
from handlers.start import rt as start
from handlers.mashina import rt as mashinalar
from handlers.tozalash import router
from handlers.photo import router as photo
from handlers.all import rt as all
dp = Dispatcher()

async def main():
    bot = Bot(token)
    dp.include_router(router)
    dp.include_router(start)
    dp.include_router(mashinalar)
    dp.include_router(photo)
    dp.include_router(all)

    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
