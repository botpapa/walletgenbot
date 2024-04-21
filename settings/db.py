"""
Initializing connection with MongoDB
"""
import motor.motor_asyncio

from settings import config
from settings.logger import log
from settings.additional_loop import loop

if config.MONGODB_CONNECTION_URI is not None:
    client = motor.motor_asyncio.AsyncIOMotorClient(config.MONGODB_CONNECTION_URI)
    db = client[config.MONGODB_DATABASE_NAME]
    loop.run_until_complete(log.info(f'MongoDB [{config.MONGODB_DATABASE_NAME}] initialized'))
else:
    client, db = None, None
    loop.run_until_complete(log.warning(f'[service] MongoDB URI is not defined'))
