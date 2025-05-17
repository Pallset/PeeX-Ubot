# Coded By PeeX Authority 
# Please Join Telegram Channel For Updated
# PeeX - Userbot
# t.me/peexubot
# t.me/peex_ubot
from telethon import events

def register(client):
    @client.on(events.NewMessage(pattern=r"^\.say (.+)", outgoing=True))
    async def say_cmd(event):
        text = event.pattern_match.group(1)
        
        if not text:
            return await event.edit("Mau ngomong apa?")

        formatted_text = f"<blockquote>{text.upper()}</blockquote>"
        
        await event.edit(formatted_text, parse_mode="html")
