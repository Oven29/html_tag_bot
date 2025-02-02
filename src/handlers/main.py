from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
import logging


router = Router()

logger = logging.getLogger(__name__)


@router.message(Command('web_app'))
async def web_app(message: Message) -> None:
    _, web_app_url = message.text.split()

    await message.answer(
        text='Web app',
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text='Open web app',
                        web_app=WebAppInfo(url=web_app_url),
                    )
                ],
            ],
        ),
    )


@router.message()
async def echo_html(message: Message) -> None:
    await message.answer(
        text=message.html_text,
        reply_markup=message.reply_markup,
    )
