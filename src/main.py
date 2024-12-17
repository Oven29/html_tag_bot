from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio

from src import config
from src import handlers
from src.utils.setup import logging_setup, dir_setup


async def start_bot() -> None:
    "Run bot"
    # creating instances bot and dispatcher
    bot = Bot(
        token=config.BOT_TOKEN,
    )
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_routers(
        handlers.main.router,
    )
    # getting info about bot
    config.BOT_USERNAME = (await bot.get_me()).username
    # starting bot polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


def run() -> None:
    "Start project"
    dir_setup()
    logging_setup()
    asyncio.run(start_bot())
