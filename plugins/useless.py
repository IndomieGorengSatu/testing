from bot import Bot
from pyrogram.types import Message
from pyrogram import filters
from config import  USER_REPLY_TEXT
from datetime import datetime
from helper_func import get_readable_time


@Bot.on_message(filters.private)
async def useless(_,message: Message):
    if USER_REPLY_TEXT:
        await message.reply(USER_REPLY_TEXT)
