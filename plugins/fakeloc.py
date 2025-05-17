# Coded By PeeX Authority 
# Please Join Telegram Channel For Updated
# PeeX - Userbot
# t.me/peexubot
# t.me/peex_ubot
from telethon import events
from telethon.tl.types import InputMediaGeoPoint, GeoPoint

FAKE_LOCATIONS = {
    "tokyo": (35.682839, 139.759455),
    "newyork": (40.712776, -74.005974),
    "jakarta": (-6.208763, 106.845599),
    "paris": (48.856613, 2.352222),
}

def register(client):
    @client.on(events.NewMessage(pattern=r"^\.fakeloc (\S+)", outgoing=True))
    async def fake_location(event):
        loc_name = event.pattern_match.group(1).lower()
        if loc_name in FAKE_LOCATIONS:
            lat, lon = FAKE_LOCATIONS[loc_name]
            await event.client.send_message(
                event.chat_id,
                file=InputMediaGeoPoint(GeoPoint(lat, lon))
            )
            await event.edit(f"📍 Fake lokasi terkirim: {loc_name.capitalize()}")
        else:
            await event.edit("❌ Lokasi tidak ditemukan! Gunakan lokasi yang ada.")
