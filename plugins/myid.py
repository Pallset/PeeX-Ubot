# Coded By PeeX Authority 
# Please Join Telegram Channel For Updated
# PeeX - Userbot
# t.me/peexubot
# t.me/peex_ubot
from telethon import events

def register(client):
    @client.on(events.NewMessage(pattern=r"^\.myid$", outgoing=True))
    async def my_id(event):
        await event.edit(f"ID Chat ini: `{event.chat_id}`")
