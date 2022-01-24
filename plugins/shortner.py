import os
import aiohttp
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InlineQueryResultArticle, InputTextMessageContent
from pyshorteners import Shortener


BITLY_API = os.environ.get("BITLY_API", None)
CUTTLY_API = os.environ.get("CUTTLY_API", None)
SHORTCM_API = os.environ.get("SHORTCM_API", None)
GPLINKS_API = os.environ.get("GPLINKS_API", None)
POST_API = os.environ.get("POST_API", None)
OWLY_API = os.environ.get("OWLY_API", None)

@Client.on_message(filters.command(["shorten"]) & filters.regex(r'https?://[^\s]+'))
async def reply_shortens(bot, update):
    message = await update.reply_text(
        text="🎊",
        disable_web_page_preview=True,
        quote=True
    )
    link = update.matches[0].group(0)
    shorten_urls = await short(link)
    await message.edit_text(
        text=shorten_urls,
        disable_web_page_preview=True
    )


@Client.on_inline_query(filters.regex(r'https?://[^\s]+'))
async def inline_short(bot, update):
    link = update.matches[0].group(0)
    shorten_urls = await short(link)
    answers = [
        InlineQueryResultArticle(
            title="Short Links",
            description=update.query,
            input_message_content=InputTextMessageContent(
                message_text=shorten_urls,
                disable_web_page_preview=True
            ),
        )
    ]
    await bot.answer_inline_query(
        inline_query_id=update.id,
        results=answers
    )


async def short(link):
    shorten_urls = "**⚙ Shortened URLs**\n"
    
    # Bit.ly shorten
    if BITLY_API:
        try:
            s = Shortener(api_key=BITLY_API)
            url = s.bitly.short(link)
            shorten_urls += f"\n**BitLy -** {url}"
        except Exception as error:
            print(f"Bit.ly error :- {error}")
    
    # Clck.ru shorten
        try:
            s = Shortener()
            url = s.clckru.short(link)
            shorten_urls += f"\n\n**Clck -** {url}"
        except Exception as error:
            print(f"Click.ru error :- {error}")
    
    # TinyURL.com shorten
        try:
            s = Shortener()
            url = s.tinyurl.short(link)
            shorten_urls += f"\n\n**TinyURL -** {url}"
        except Exception as error:
            print(f"TinyURL.com error :- {error}")
    
    # GPLinks shorten
    if GPLINKS_API:
        try:
            api_url = "https://gplinks.in/api"
            params = {'api': GPLINKS_API, 'url': link}
            async with aiohttp.ClientSession() as session:
                async with session.get(api_url, params=params, raise_for_status=True) as response:
                    data = await response.json()
                    url = data["shortenedUrl"]
                    shorten_urls += f"\n**GPLinks.in :-** {url}"
        except Exception as error:
            print(f"GPLink error :- {error}")
    
    # Send the text
    try:
        shorten_urls += "\n\n**Made by @x69aadii**"
        return shorten_urls
    except Exception as error:
        return error
