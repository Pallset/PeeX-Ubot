# Coded By PeeX Authority 
# Please Join Telegram Channel For Updated
# PeeX - Userbot
# t.me/peexubot
# t.me/peex_ubot
import sys
import os
import asyncio
from telethon import events

def register(client):
    @client.on(events.NewMessage(pattern=r"^\.restart$", outgoing=True))
    async def restart_bot(event):
        await event.edit("<blockquote>> 🔄 **Restarting Userbot...**</blockquote>", parse_mode="html")

        await asyncio.sleep(2)

        os.execl(sys.executable, sys.executable, *sys.argv)
