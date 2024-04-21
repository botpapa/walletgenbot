"""
Configuration file with bot settings and API keys from third-party services
"""
import os
from dotenv import load_dotenv

# Loading env variables from .env file
load_dotenv('.env')

# Obligatory variables
PROJECT_NAME = os.environ.get('PROJECT_NAME', 'MyProject')
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

# Optional variables
MONGODB_CONNECTION_URI = os.getenv('MONGODB_CONNECTION_STRING')  # URI for connecting to MongoDB
MONGODB_DATABASE_NAME = os.environ.get('MONGODB_DATABASE_NAME', 'TGbot')       # DB name in MongoDB

LOGGRAM_API_KEY = os.environ.get('LOGGRAM_API_KEY')         # API key from https://loggram.me
LOGGRAM_CHANNEL_ID = os.environ.get('LOGGRAM_CHANNEL_ID')   # Logs channel ID from https://loggram.me

if LOGGRAM_API_KEY is None:
    print('[service] Loggram API key was not defined, please go to https://loggram.me to setup cloud logging')

