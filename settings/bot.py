"""
Initializing Telegram bot instance with aiogram
"""
from aiogram import Bot, Dispatcher
from settings import config


bot = Bot(token=config.TELEGRAM_BOT_TOKEN)
dispatcher = Dispatcher(bot=bot)
