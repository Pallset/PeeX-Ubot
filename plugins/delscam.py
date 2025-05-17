# Coded By PeeX Authority 
# Please Join Telegram Channel For Updated
# PeeX - Userbot
# t.me/peexubot
# t.me/peex_ubot
import json
import os
from telethon import events

SCAM_FILE = "scam.json"

def register(client):
    @client.on(events.NewMessage(pattern=r"^\.delscam(?:\s+(.+))?", outgoing=True))
    async def del_scam(event):
        args = event.pattern_match.group(1)

        if not event.reply_to_msg_id and not args:
            return await event.reply("> **Gunakan dengan reply atau format** `.delscam <id/username>`")

        user = None

        if event.reply_to_msg_id:
            reply_message = await event.get_reply_message()
            user = reply_message.sender
        else:
            try:
                user = await client.get_entity(args.strip())
            except:
                return await event.reply("> **User tidak ditemukan.**")

        if not user:
            return await event.reply("> **Tidak bisa mendapatkan informasi user.**")

        user_id = str(user.id)
        username = f"@{user.username}" if user.username else "Tidak ada"

        # Load scam.json
        scam_data = {}
        if os.path.exists(SCAM_FILE):
            try:
                with open(SCAM_FILE, "r") as f:
                    scam_data = json.load(f)
                if not isinstance(scam_data, dict):
                    scam_data = {}
            except:
                pass

        if user_id in scam_data:
            del scam_data[user_id]
            with open(SCAM_FILE, "w") as f:
                json.dump(scam_data, f, indent=4)

            success_message = f"""
<b>« « ᴜsᴇʀ ʀᴇᴍᴏᴠᴇᴅ ғʀᴏᴍ sᴄᴀᴍ » »</b>
<code>| • ᴜsᴇʀɴᴀᴍᴇ :</code> {username}
<code>| • ɪᴅ ᴛᴇʟᴇɢʀᴀᴍ :</code> {user_id}
"""
            return await event.edit(success_message, parse_mode="html")
        else:
            return await event.reply("> **User tidak ada di scam list.**")
