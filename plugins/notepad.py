# Coded By PeeX Authority 
# Please Join Telegram Channel For Updated
# PeeX - Userbot
# t.me/peexubot
# t.me/peex_ubot
import json
import time
from telethon import events

NOTEPAD_FILE = "notepad.json"

def load_notepad():
    try:
        with open(NOTEPAD_FILE, "r") as f:
            data = json.load(f)
            if not isinstance(data, dict):
                return {}
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_notepad(data):
    with open(NOTEPAD_FILE, "w") as f:
        json.dump(data, f, indent=4)

def register(client):

    @client.on(events.NewMessage(pattern=r"^\.notepad (add|delete)\|(.*?)\|(.*?)?$", outgoing=True))
    async def manage_notepad(event):
        notepad = load_notepad()

        args = event.pattern_match.groups()
        action, key, value = args[0], args[1].strip(), (args[2] or "").strip()

        if action == "add":
            if key in notepad:
                await event.edit("> **Notepad sudah ada!** Gunakan `.notepad delete|{key}` untuk menghapusnya dulu.")
                return

            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            notepad[key] = {"response": value, "time": timestamp}
            save_notepad(notepad)

            await event.edit(
                f"<blockquote>« « sᴜᴄᴄᴇsғᴜʟʟʏ ᴀᴅᴅᴇᴅ ɴᴏᴛᴇᴘᴀᴅ » »</blockquote>\n"
                f"<blockquote>| • ᴘᴇsᴀɴ : {key}</blockquote>\n"
                f"<blockquote>| • ᴊᴀᴡᴀʙᴀɴ : {value}</blockquote>\n"
                f"<blockquote>| • ᴛɪᴍᴇ : {timestamp}</blockquote>",
                parse_mode="html"
            )

        elif action == "delete":
            if key not in notepad:
                await event.edit("> **Notepad tidak ditemukan!**")
                return

            deleted_data = notepad.pop(key)
            save_notepad(notepad)

            await event.edit(
                f"<blockquote>« « sᴜᴄᴄᴇsғᴜʟʟʏ ᴅᴇʟᴇᴛᴇᴅ ɴᴏᴛᴇᴘᴀᴅ » »</blockquote>\n"
                f"<blockquote>| • ᴘᴇsᴀɴ : {key}</blockquote>\n"
                f"<blockquote>| • ᴊᴀᴡᴀʙᴀɴ : {deleted_data['response']}</blockquote>\n"
                f"<blockquote>| • ᴛɪᴍᴇ : {deleted_data['time']}</blockquote>",
                parse_mode="html"
            )

    @client.on(events.NewMessage(outgoing=True))
    async def check_notepad(event):
        notepad = load_notepad()
        message_text = event.text.strip()

        if message_text in notepad:
            await event.edit(notepad[message_text]["response"], parse_mode="html")
