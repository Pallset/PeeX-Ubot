# Coded By PeeX Authority 
# Please Join Telegram Channel For Updated
# PeeX - Userbot
# t.me/peexubot
# t.me/peex_ubot
import os
from telethon import events

def register(client):
    @client.on(events.NewMessage(pattern=r"^\.help$", outgoing=True))
    async def help_cmd(event):
        img_path = "img/help.png"

        if not os.path.exists(img_path):
            return await event.reply("⚠️ File `help.png` tidak ditemukan di folder `img/`!")

        plugin_count = len([f for f in os.listdir("plugins") if f.endswith(".py") and f != "__init__.py"])

        is_premium = "True" if "dl.py" in os.listdir("plugins") else "False"

        caption = f"""
<blockquote>
___________________________
«« ᴘᴇᴇx - ᴜsᴇʀʙᴏᴛ »»
___________________________
• ᴘʟᴜɢɪɴ : {plugin_count}
• ᴏᴡɴᴇʀ : @ʟᴏ_ᴘᴏᴏ
• ᴄʜᴀɴɴᴇʟ : <a href='https://t.me/sharingscript'>ᴛ.ᴍᴇ/sʜᴀʀɪɴɢsᴄʀɪᴘᴛ/</a>
• sᴛᴀᴛᴜs : ᴀᴄᴛɪᴠᴇ
• ᴘʀᴇᴍɪᴜᴍ : {is_premium}
___________________________

Cek Command @PeeXUbot
</blockquote>
"""

        await event.client.send_file(
            event.chat_id,
            file=img_path,
            caption=caption,
            parse_mode="html"
        )
        await event.delete()
