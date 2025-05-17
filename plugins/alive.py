# Coded By PeeX Authority 
# Please Join Telegram Channel For Updated
# PeeX - Userbot
# t.me/peexubot
# t.me/peex_ubot
from telethon import events

def register(client):
    @client.on(events.NewMessage(pattern=r"^\.alive$", outgoing=True))
    async def alive_handler(event):
        try:
            bot_username = "@PeeX_Ubot"
            query = "help"

            results = await client.inline_query(bot_username, query)
            if results:
                await results[0].click(event.chat_id)
                await event.delete()
            else:
                await event.edit("❌ Gagal mendapatkan inline result.")
        except Exception as e:
            await event.edit(f"❌ Error: {e}")
