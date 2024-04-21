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

    return f'New wallet created\n\nAddress: <code>{account.address}</code>\n\nSeed phrase:\n<code>{mnemonic}</code>\n\nPrivate key:\n<code>{account.key.hex()}</code>'


@dispatcher.message_handler(content_types=ContentTypes.all())
async def text_handler(message):
    if message.text == "/new":
        await message.reply(create_wallet(), parse_mode="HTML")
    else:
        await message.reply("Send /new to create a new wallet")


# Starting bot polling
executor.start_polling(dispatcher)
