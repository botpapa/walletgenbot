"""
Initializing Telegram bot instance with aiogram
"""
from aiogram import Bot, Dispatcher

from settings import config
from settings.logger import log
from settings.additional_loop import loop


bot = Bot(token=config.TELEGRAM_BOT_TOKEN)
dispatcher = Dispatcher(bot=bot)

loop.run_until_complete(log.info('Bot has been initialized'))
