from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


START_TEXT = """Hello {} 💎
I am a link shortner telegram bot.

>> `Just send me any link & I'll shorten it Instantly`"""

MADE WITH ❤️ IN 🇮🇳

START_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('⚡ Contact Owner ⚡', url='https://t.me/x69aadii')
        ]
    ]
)

@Client.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        reply_markup=START_BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )
