from aiogram import Router
from aiogram.types import Message
import logging


router = Router()

logger = logging.getLogger(__name__)


@router.message()
async def echo_html(message: Message) -> None:
    await message.answer(
        text=message.html_text,
        reply_markup=message.reply_markup,
    )
