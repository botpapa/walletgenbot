"""
Configuration file with bot settings and API keys from third-party services
"""
import os
from dotenv import load_dotenv

# Loading env variables from .env file
load_dotenv('.env')

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
