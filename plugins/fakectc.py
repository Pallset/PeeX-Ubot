# Coded By PeeX Authority 
# Please Join Telegram Channel For Updated
# PeeX - Userbot
# t.me/peexubot
# t.me/peex_ubot
from telethon import events
from telethon.tl.types import InputMediaContact
from telethon.tl.functions.messages import SendMediaRequest
from telethon.helpers import generate_random_long

def register(client):
    @client.on(events.NewMessage(pattern=r"^\.fakectc (.+)", outgoing=True))
    async def fakectc(event):
        try:
            number = event.pattern_match.group(1).strip()

            me = await client.get_me()
            full_name = f"{me.first_name or ''} {me.last_name or ''}".strip()
            if not full_name:
                full_name = "PeeX User"

            await client(SendMediaRequest(
                peer=event.chat_id,
                media=InputMediaContact(
                    phone_number=number,
                    first_name=f"{full_name} | PeeX-Userbot",
                    last_name="",
                    vcard=full_name
                ),
                message="📞 Powered By PeeX-Userbot\n🌐 t.me/sharingscript",
                random_id=generate_random_long()
            ))

            await event.delete()

        except Exception as e:
            await event.edit(f"❌ Gagal kirim fake contact:\n{e}")
