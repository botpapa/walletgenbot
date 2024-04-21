"""
Setting up customized logging with connection to https://loggram.me cloud logging service
"""
import asyncio
import aiohttp
import logging

from settings import config


class Logger(logging.Logger):
    super(logging.Logger)

    async def debug(self, msg, *args, **kwargs):
        self._log(1, msg, args, **kwargs)
        asyncio.create_task(self._send_message(msg, 'debug'))

    async def info(self, msg, *args, **kwargs):
        self._log(2, msg, args, **kwargs)
        asyncio.create_task(self._send_message(msg, 'info'))

    async def warning(self, msg, *args, **kwargs):
        self._log(3, msg, args, **kwargs)
        asyncio.create_task(self._send_message(msg, 'warning'))

    async def error(self, msg, *args, **kwargs):
        self._log(4, msg, args, **kwargs)
        asyncio.create_task(self._send_message(msg, 'error'))

    @staticmethod
    async def _send_message(msg, level):
        """ Sending message to Loggram """

        if config.LOGGRAM_API_KEY is None:
            return

        try:
            async with aiohttp.ClientSession() as session:
                await session.post('https://loggram.me/api/sendLog',
                                   params={'api_key': config.LOGGRAM_API_KEY},
                                   json={'channel_id': config.LOGGRAM_CHANNEL_ID,
                                         'log': msg,
                                         'log_level': level},
                                   timeout=1)
        except: pass


log_format = '%(asctime)s | %(levelname)s | %(message)s'
formatter = logging.Formatter(log_format)
ch = logging.StreamHandler()
ch.setFormatter(formatter)

log = Logger('logger')
log.addHandler(ch)
