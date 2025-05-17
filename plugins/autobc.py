# Coded By PeeX Authority 
# Please Join Telegram Channel For Updated
# PeeX - Userbot
# t.me/peexubot
# t.me/peex_ubot
import asyncio
import re
from datetime import datetime, timedelta
from telethon import events

def convert_time(duration_str):
    match = re.match(r"(\d+)([smhdw])", duration_str.lower())
    if not match:
        return None
    value, unit = int(match[1]), match[2]
    if unit == 's':
        return timedelta(seconds=value)
    if unit == 'm':
        return timedelta(minutes=value)
    if unit == 'h':
        return timedelta(hours=value)
    if unit == 'd':
        return timedelta(days=value)
    if unit == 'w':
        return timedelta(weeks=value)

def register(client):
    @client.on(events.NewMessage(pattern=r"^\.autobc\s+(.+)", outgoing=True))
    async def autobc(event):
        args = event.pattern_match.group(1)
        try:
            text, delay, duration = map(str.strip, args.split("|", 2))
            delay = int(delay)
            duration_td = convert_time(duration)
            if not duration_td:
                return await event.edit("> ❌ Format waktu gak valid! Contoh: `1h`, `1d`, `1w`")
        except:
            return await event.edit("> ❌ Format salah!\nGunakan `.autobc <text>|<delay>|<time>`")

        await event.edit(f"✅ Auto Broadcast dimulai!\n🕒 Delay: {delay}s\n⏳ Waktu: {duration}")

        end_time = datetime.now() + duration_td
        sent_count = 0

        async for dialog in client.iter_dialogs():
            entity = dialog.entity
            if hasattr(entity, 'megagroup') and entity.megagroup:
                chat_id = entity.id
                while datetime.now() < end_time:
                    try:
                        await client.send_message(chat_id, text)
                        sent_count += 1
                        await asyncio.sleep(delay)
                    except Exception as e:
                        print(f"[AutoBC ERROR] Gagal kirim ke {chat_id}: {e}")
                    break  # kirim satu kali per grup tiap loop

        await event.edit(f"✅ Broadcast selesai!\nTotal pesan terkirim: `{sent_count}`")

