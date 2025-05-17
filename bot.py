# Coded By PeeX Authority 
# Please Join Telegram Channel For Updated
# PeeX - Userbot
# t.me/peexubot
# t.me/peex_ubot
"""Dont Change Or Error"""
import os
from telebot import TeleBot, types
from config import BOT_TOKEN

bot = TeleBot(BOT_TOKEN)

def count_plugins():
    plugin_folder = "plugins"
    if not os.path.exists(plugin_folder):
        return 0
    return len([f for f in os.listdir(plugin_folder) if f.endswith('.py')])

def main_page_caption():
    plugin_count = count_plugins()
    return (
        "<pre>"
        "_______\n"
        "«« ᴘᴇᴇx - ᴜsᴇʀʙᴏᴛ »»\n"
        "_______\n"
        f"• ᴘʟᴜɢɪɴ : {plugin_count}\n"
        "• ᴏᴡɴᴇʀ : <a href=\"https://t.me/lo_poo\">@ʟᴏ_ᴘᴏᴏ</a>\n"
        "• ᴄʜᴀɴɴᴇʟ : <a href=\"https://t.me/sharingscript\">ᴛ.ᴍᴇ/sʜᴀʀɪɴɢsᴄʀɪᴘᴛ/</a>\n"
        "• sᴛᴀᴛᴜs : ᴀᴄᴛɪᴠᴇ\n"
        "• ᴘʀᴇᴍɪᴜᴍ : True\n"
        "Cek Fitur Lengkap Hanya Di Channel @PeeXUbot"
        "_______"
        "</pre>"
    )

pages = {
    1: (
        "<pre>"
        "🔥 Help 1 🔥\n\n"
        "ℹ️ <code>.ɪɴғ&lt;ʀᴇᴘʟʏ/ᴜꜱᴇʀɴᴀᴍᴇ/ɪᴅ&gt;</code> → ʟɪʜᴀᴛ ɪɴғᴏ ᴜsᴇʀ.\n"
        "<code>.sᴀʏ &lt;ᴛᴇxᴛ&gt;</code> → ɴɢᴏᴍᴏɴɢ ᴅᴇɴɢᴀɴ ғᴏʀᴍᴀᴛ ʙʟᴏᴄᴋǫᴜᴏᴛᴇ.\n"
        "<code>.ᴀᴅᴅᴘʟᴜɢɪɴ &lt;ʀᴇᴘʟʏ/ᴄᴏᴅᴇ&gt;|&lt;ɴᴀᴍᴀ ғɪʟᴇ&gt;</code> → ᴛᴀᴍʙᴀʜ ᴘʟᴜɢɪɴ.\n"
        "</pre>"
    ),
    2: (
        "<pre>"
        "🔥 Help 2 🔥\n\n"
        "<code>.ᴅʟ &lt;ʏᴛ/ᴛɪᴋᴛᴏᴋ/sᴘᴏᴛɪғʏ/ɪɢ&gt; &lt;link&gt;</code> → ᴅᴏᴡɴʟᴏᴀᴅ ᴍᴇᴅɪᴀ.\n"
        "<code>.ᴀɪ &lt;ᴘʀᴏᴍᴘᴛ&gt;</code> → ᴄʜᴀᴛ ᴅᴇɴɢᴀɴ ᴀɪ.\n"
        "⚡ <code>.ʙʟᴀɴᴋ &lt;ᴏɴ/ᴏғғ&gt;</code> → ᴀᴋᴛɪғᴋᴀɴ ᴍᴏᴅᴇ ʙʟᴀɴᴋ ɴᴀᴍᴇ.\n"
        "</pre>"
    ),
    3: (
        "<pre>"
        "🔥 Help 3 🔥\n\n"
        "<code>.ʙᴄ &lt;ᴛᴇxᴛ&gt;</code> → ʙʀᴏᴀᴅᴄᴀsᴛ ᴋᴇ ɢʀᴜᴘ.\n"
        "<code>.ᴀᴅᴅsᴄᴀᴍ &lt;ɪᴅ&gt;|&lt;ᴀʟᴀsᴀɴ&gt;</code> → ᴛᴀᴍʙᴀʜ sᴄᴀᴍ ʟɪsᴛ.\n"
        "<code>.ɴᴏᴛᴇᴘᴀᴅ &lt;ᴅᴇʟᴇᴛᴇ/ᴀᴅᴅ&gt;|&lt;ᴛᴇxᴛ&gt;|&lt;ᴊᴀᴡᴀʙᴀɴn&gt;</code> → ᴛᴀᴍʙᴀʜ ɴᴏᴛᴇ ʀᴇsᴘᴏɴ.\n"
        "</pre>"
    )
}

def get_markup(page):
    markup = types.InlineKeyboardMarkup()
    buttons = []

    if page > 0:
        buttons.append(types.InlineKeyboardButton("⬅ ᴘʀᴇᴠɪᴏᴜs", callback_data=f"page_{page-1}"))

    buttons.append(types.InlineKeyboardButton(f"🔥 ʜᴇʟᴘ {page if page>0 else 'Main'} 🔥", callback_data="noop"))

    if page < len(pages):
        buttons.append(types.InlineKeyboardButton("→ ɴᴇxᴛ", callback_data=f"page_{page+1}"))

    markup.row(*buttons)
    return markup

@bot.inline_handler(lambda query: "help" in query.query.lower())
def inline_query_handler(inline_query):
    try:
        caption = main_page_caption()
        markup = get_markup(0)

        img_url = "https://i.ibb.co/0jJ5QQYz/IMG-20250331-164503.jpg"
        result = types.InlineQueryResultPhoto(
            id="help_page_0",
            photo_url=img_url,
            thumbnail_url=img_url,
            caption=caption,
            reply_markup=markup,
            parse_mode='HTML'
        )

        bot.answer_inline_query(inline_query.id, [result], cache_time=1, is_personal=True)
    except Exception as e:
        print(f"[INLINE ERROR] {e}")

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    try:
        if call.data == "noop":
            bot.answer_callback_query(call.id)
            return

        if call.data.startswith("page_"):
            page = int(call.data.split("_")[1])
            if page == 0:
                caption = main_page_caption()
            elif page in pages:
                caption = pages[page]
            else:
                bot.answer_callback_query(call.id, "ʜᴀʟᴀᴍᴀɴ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ!", show_alert=True)
                return

            markup = get_markup(page)

            if call.inline_message_id:
                bot.edit_message_caption(
                    inline_message_id=call.inline_message_id,
                    caption=caption,
                    reply_markup=markup,
                    parse_mode='HTML'
                )
            else:
                bot.edit_message_caption(
                    chat_id=call.message.chat.id,
                    message_id=call.message.message_id,
                    caption=caption,
                    reply_markup=markup,
                    parse_mode='HTML'
                )
            bot.answer_callback_query(call.id)
    except Exception as e:
        print(f"[CALLBACK ERROR] {e}")

print("✅ Inline Ready")
bot.infinity_polling()
