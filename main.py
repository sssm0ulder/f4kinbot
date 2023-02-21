import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, types, F

from aiogram.filters import CommandStart, Command, StateFilter
from aiogram.fsm.context import FSMContext

from config import Config

from routers import (
    lang_router, 
    city_router, 
    area_router,
    service_router,
    price_router,
    girl_router,
    after_girl_router
)


async def main():
    config = Config.get_instance()

    bot = Bot(token=config.TOKEN)
    dp = Dispatcher()

    dp.include_router(after_girl_router)
    dp.include_router(lang_router)
    dp.include_router(city_router)
    dp.include_router(area_router)
    dp.include_router(service_router)
    dp.include_router(price_router)
    dp.include_router(girl_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
 