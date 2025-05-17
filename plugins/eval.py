# plugins/eval_plugin.py
# Coded By PeeX Authority 
# Please Join Telegram Channel For Updated
# PeeX - Userbot
# t.me/peexubot
# t.me/peex_ubot

from telethon import events
import asyncio

def register(client):
    @client.on(events.NewMessage(pattern=r"^\.eval (.+)", outgoing=True))
    async def eval_cmd(event):
        code = event.pattern_match.group(1)
        try:
            result = eval(code)
            if asyncio.iscoroutine(result):
                result = await result
            await event.edit(f"💻 Result:\n{result}")
        except Exception as e:
            await event.edit(f"❌ Error:\n{e}")
