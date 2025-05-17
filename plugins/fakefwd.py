# Coded By PeeX Authority 
# Please Join Telegram Channel For Updated
# PeeX - Userbot
# t.me/peexubot
# t.me/peex_ubot
from telethon import events

def register(client):
    @client.on(events.NewMessage(pattern=r"^\.fakefwd (\S+) (.+)", outgoing=True))
    async def fake_forward(event):
        args = event.pattern_match
        user = args.group(1)
        msg = args.group(2)

        try:
            user_entity = await event.client.get_entity(user)
            await event.client.send_message(user_entity, msg)
            await event.edit(f"✅ Berhasil kirim pesan palsu dari {user}!")
        except Exception as e:
            await event.edit(f"❌ Gagal kirim pesan palsu: {str(e)}")
