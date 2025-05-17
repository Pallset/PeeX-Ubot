# Coded By PeeX Authority 
# Please Join Telegram Channel For Updated
# PeeX - Userbot
# t.me/peexubot
# t.me/peex_ubot
from telethon import events
import asyncio

broadcasting = False

def register(client):
    @client.on(events.NewMessage(pattern=r"^\.bc (\w+)(?:\s(.+))?", outgoing=True))
    async def broadcast(event):
        global broadcasting
        args = event.pattern_match
        broadcast_type = args.group(1).lower()
        text = args.group(2)

        if broadcast_type not in ["fwd", "def"]:
            return await event.reply("> **Tipe broadcast harus 'fwd' atau 'def'.**")

        if event.reply_to_msg_id:
            message = await event.get_reply_message()
        elif broadcast_type == "def" and text:
            message = text
        else:
            return await event.reply("> **Gunakan reply ke pesan atau tulis teks broadcast.**")

        chats = []
        async for dialog in client.iter_dialogs():
            if dialog.is_group or dialog.is_channel:
                chats.append(dialog.id)

        broadcasting = True
        success, failed = 0, 0
        for chat_id in chats:
            if not broadcasting:
                break
            try:
                if broadcast_type == "fwd" and isinstance(message, events.NewMessage.Event):
                    await client.forward_messages(chat_id, message)
                else:
                    await client.send_message(chat_id, message if isinstance(message, str) else message.text)

                success += 1
            except Exception:
                failed += 1
            await asyncio.sleep(0.5)

        broadcasting = False
        result_message = f"""<blockquote>
> « « ʙʀᴏᴀᴅᴄᴀsᴛ ʀᴇᴘᴏʀᴛ » »  
> | • ᴛʏᴘᴇ : {broadcast_type.capitalize()}  
> | • ᴛᴏᴛᴀʟ ᴄʜᴀᴛs : {len(chats)}  
> | • sᴜᴄᴄᴇss : {success}  
> | • ғᴀɪʟᴇᴅ : {failed}  
> | • sᴛᴀᴛᴜs : {"ᴄᴀɴᴄᴇʟʟᴇᴅ" if not broadcasting else "ᴄᴏᴍᴘʟᴇᴛᴇᴅ"}
</blockquote>"""

        await event.reply(result_message, link_preview=False)

    @client.on(events.NewMessage(pattern=r"^\.stopbc$", outgoing=True))
    async def stop_broadcast(event):
        global broadcasting
        if broadcasting:
            broadcasting = False
            await event.reply("> **Broadcast dihentikan.**")
        else:
            await event.reply("> **Tidak ada broadcast yang sedang berjalan.**")
