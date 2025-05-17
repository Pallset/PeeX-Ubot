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
    @client.on(events.NewMessage(pattern=r"^\.inf(?:\s@?(\w+))?", outgoing=True))
    async def get_user_info(event):
        user = None
        username = event.pattern_match.group(1)

        if event.reply_to_msg_id:
            reply_message = await event.get_reply_message()
            user = reply_message.sender
        elif username:
            try:
                user = await client.get_entity(username)
            except:
                return await event.reply("> **User tidak ditemukan.**")

        if not user:
            return await event.reply("> **Tidak ada user yang di-reply atau username tidak valid.**")

        first_name = user.first_name or "False"
        last_name = user.last_name or "False"
        full_name = f'<a href="tg://user?id={user.id}">{first_name} {last_name}</a>'
        username = f"@{user.username}" if user.username else "Tidak ada"
        user_id = user.id

        is_scam = False
        scam_reason = "False"

        if os.path.exists(SCAM_FILE):
            try:
                with open(SCAM_FILE, "r") as f:
                    scam_data = json.load(f)
                    if str(user_id) in scam_data:
                        is_scam = True
                        scam_reason = scam_data[str(user_id)]
            except:
                pass

        is_mutual = "False"
        async for user_in_chat in client.iter_participants(event.chat_id):
            if user_in_chat.id == user_id:
                is_mutual = "True"
                break

        info_message = f"""
<b>« « ᴜsᴇʀ ɪɴғᴏʀᴍᴀᴛɪᴏɴ » »</b>
<code>| • ғɪʀsᴛ ɴᴀᴍᴇ :</code> {first_name}
<code>| • ʟᴀsᴛ ɴᴀᴍᴇ :</code> {last_name}
<code>| • ғᴜʟʟ ɴᴀᴍᴇ :</code> {full_name}
<code>| • ᴜsᴇʀɴᴀᴍᴇ :</code> {username}
<code>| • ɪᴅ :</code> {user_id}
<code>| • ɪs sᴄᴀᴍ :</code> {"✅" if is_scam else "❌"}
<code>| • ʀᴇᴀsᴏɴ sᴄᴀᴍ :</code> {scam_reason}
<code>| • ɪs ᴍᴜᴛᴜᴀʟ ᴀᴄᴄᴏᴜɴᴛ :</code> {"✅" if is_mutual == "True" else "❌"}
"""

        await event.reply(info_message, parse_mode="html", link_preview=False)
