# Coded By PeeX Authority 
# Please Join Telegram Channel For Updated
# PeeX - Userbot
# t.me/peexubot
# t.me/peex_ubot
from telethon import events

def register(client):
    @client.on(events.NewMessage(pattern=r"^\.id (.+)", outgoing=True))
    async def get_id(event):
        input_name = event.pattern_match.group(1)
        await event.edit("**Process...**")

        try:
            entity = await event.client.get_entity(input_name)
            chat_id = entity.id

            if chat_id < 0:
                chat_id = f"-100{abs(chat_id)}"

            await event.edit(f"**Found ID:**`-100{chat_id}`")
        except Exception as e:
            await event.edit(f"❌ **Error:** {str(e)}")
