# Coded By PeeX Authority 
# Please Join Telegram Channel For Updated
# PeeX - Userbot
# t.me/peexubot
# t.me/peex_ubot

import os
import importlib.util
import asyncio
from datetime import timedelta
from telethon import TelegramClient, events
from telethon.tl.functions.messages import GetInlineBotResultsRequest, SendInlineBotResultRequest
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InlineQueryResultArticle, InputTextMessageContent
from pyrogram.enums import ParseMode

from config import API_ID, API_HASH, BOT_SESSION, BOT_TOKEN

client = TelegramClient(BOT_SESSION, API_ID, API_HASH)

bot = Client("peex", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

PLUGINS_FOLDER = "plugins"

def load_plugins():
    for file in os.listdir(PLUGINS_FOLDER):
        if file.endswith(".py") and not file.startswith("__"):
            module_path = os.path.join(PLUGINS_FOLDER, file)
            module_name = f"plugins.{file[:-3]}"

            try:
                spec = importlib.util.spec_from_file_location(module_name, module_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                if hasattr(module, "register"):
                    module.register(client)
                    print(f"✅ Plugin {file} berhasil dimuat!")
                else:
                    print(f"⚠️ Plugin {file} tidak memiliki fungsi register, dilewati!")

            except Exception as e:
                print(f"❌ Error saat memuat plugin {file}: {e}")

def help_menu(page):
    pages = {
        1: InlineKeyboardMarkup([
            [InlineKeyboardButton("•| ᴜsᴇʀ ɪɴғᴏ |•", callback_data="help_inf"),
             InlineKeyboardButton("•| sᴀʏ |•", callback_data="help_say")],
            [InlineKeyboardButton("•| ᴀᴅᴅ ᴘʟᴜɢɪɴ |•", callback_data="help_addplugin"),
             InlineKeyboardButton("•| ᴅᴏᴡɴʟᴏᴀᴅᴇʀ |•", callback_data="help_dl")],
            [InlineKeyboardButton("➡ Next", callback_data="help_page_2")]
        ]),
        2: InlineKeyboardMarkup([
            [InlineKeyboardButton("•| ᴀɪ |•", callback_data="help_ai"),
             InlineKeyboardButton("•| ʙʟᴀɴᴋ ɴᴀᴍᴇ |•", callback_data="help_blank")],
            [InlineKeyboardButton("•| ʙʀᴏᴀᴅᴄᴀsᴛ |•", callback_data="help_bc"),
             InlineKeyboardButton("•| sᴄᴀᴍ ʟɪsᴛ |•", callback_data="help_scam")],
            [InlineKeyboardButton("•| ɴᴏᴛᴇᴘᴀᴅ |•", callback_data="help_notepad")],
            [InlineKeyboardButton("⬅ Previous", callback_data="help_page_1"),
             InlineKeyboardButton(" Back", callback_data="help_main")]
        ])
    }
    return pages.get(page, pages[1])

@bot.on_callback_query()
async def callback_query(client, callback_query):
    data = callback_query.data

    if data.startswith("help_page_"):
        page = int(data.split("_")[-1])
        await callback_query.message.edit_text("<blockquote>\n **Pilih Command yang ingin kamu lihat:**\n</blockquote>", reply_markup=help_menu(page))
        return

    if data == "help_main":
        await callback_query.message.edit_text("<blockquote>\n **Silakan tekan tombol yang ada:**\n</blockquote>", reply_markup=help_menu(1))
        return

    commands = {
        "help_inf": "ℹ️ `.ɪɴғ <ʀᴇᴘʟʏ/ᴜsᴇʀɴᴀᴍᴇ/ɪᴅ>` → ʟɪʜᴀᴛ ɪɴғᴏ ᴜsᴇʀ.",
        "help_say": " `.sᴀʏ <ᴛᴇxᴛ>` → ɴɢᴏᴍᴏɴɢ ᴅᴇɴɢᴀɴ ғᴏʀᴍᴀᴛ ʙʟᴏᴄᴋǫᴏᴏᴛᴇ.",
        "help_addplugin": "️ `.ᴀᴅᴅᴘʟᴜɢɪɴ <ʀᴇᴘʟʏ/ᴄᴏᴅᴇ>|<ɴᴀᴍᴀ ғɪʟᴇ>` → ᴛᴀᴍʙᴀʜ ᴘʟᴜɢɪɴ.",
        "help_dl": " `.ᴅʟ <ʏᴛ/ᴛɪᴋᴛᴏᴋ/sᴘᴏᴛɪғʏ/ɪɢ> <ʟɪɴᴋ>` → ᴅᴏᴡɴʟᴏᴀᴅ ᴍᴇᴅɪᴀ.",
        "help_ai": " `.ᴀɪ <ᴘʀᴏᴍᴘᴛ>` → ᴄʜᴀᴛ ᴅᴇɴɢᴀɴ ᴀɪ.",
        "help_blank": "⚡ `.ʙʟᴀɴᴋ <ᴏɴ/ᴏғғ>` → ᴀᴋᴛɪғɪɴ ᴍᴏᴅᴇ ᴄʜᴀᴛ ᴋᴏsᴏɴɢ.",
        "help_bc": " `.ʙᴄ <ғᴡᴅ/ᴅᴇғ> <ʀᴇᴘʟʏ/ᴘᴇsᴀɴ>` → ᴋɪʀɪᴍ ʙᴄ ᴋᴇ sᴇᴍᴜᴀ ᴄʜᴀᴛ.",
        "help_scam": " `.ᴀᴅᴅsᴄᴀᴍ <ɪᴅ>|<ᴀʟᴀsᴀɴ>` → ᴛᴀᴍʙᴀʜ sᴄᴀᴍ ʟɪsᴛ.",
        "help_notepad": " `.ɴᴏᴛᴇᴘᴀᴅ <ᴅᴇʟᴇᴛᴇ/ᴀᴅᴅ>|<ᴘᴇʀᴛᴀɴʏᴀᴀɴ>|<ᴊᴀᴡᴀʙᴀɴ>` → ᴛᴀᴍʙᴀʜ ɴᴏᴛᴇ/ᴅᴇʟᴇᴛᴇ ɴᴏᴛᴇ."
    }

    await callback_query.message.edit_text(commands.get(data, "❌ Tidak ditemukan"), reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(" Back", callback_data="help_main")]]))

@bot.on_inline_query()
async def inline_query_handler(client, query):
    try:
        thumb_url = "https://i.ibb.co.com/0jJ5QQYz/IMG-20250331-164503.jpg"  # URL gambar
        await query.answer(
            results=[
                InlineQueryResultArticle(
                    title="Help Menu",
                    input_message_content=InputTextMessageContent(
                        message_text=" **Pilih Command yang ingin kamu lihat:**",
                        parse_mode=ParseMode.DEFAULT_HTML
                    ),
                    reply_markup=help_menu(1),
                    thumb_url=thumb_url
                )
            ],
            cache_time=1
        )
    except Exception as e:
        print(f"❌ Error inline query: {e}")

async def main():
    load_plugins()
    await asyncio.gather(client.run_until_disconnected(), bot.start())

if __name__ == "__main__":
    with client:
        client.loop.run_until_complete(main())
