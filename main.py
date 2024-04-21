"""
Launch this file to start the bot
"""
from aiogram import executor
from aiogram.types import ContentTypes

from eth_account import Account
from mnemonic import Mnemonic

from settings.bot import dispatcher


def create_wallet():
    Account.enable_unaudited_hdwallet_features()
    mnemo = Mnemonic("english")
    mnemonic = mnemo.generate(strength=256)
    account = Account.from_mnemonic(mnemonic)

    return f'New wallet created\n\nAddress: {account.address}\n\nSeed phrase:\n{mnemonic}\n\nPrivate key:\n{account.key.hex()}'


@dispatcher.message_handler(content_types=ContentTypes.all())
async def text_handler(message):
    if message.text == "/new":
        await message.reply(create_wallet())


# Starting bot polling
executor.start_polling(dispatcher)
