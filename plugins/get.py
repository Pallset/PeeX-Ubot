# Coded By PeeX Authority 
# Please Join Telegram Channel For Updated
# PeeX - Userbot
# t.me/peexubot
# t.me/peex_ubot
import aiohttp
import os
from telethon import events
import mimetypes
import re

def register(client):
    @client.on(events.NewMessage(pattern=r"^\.get (.+)", outgoing=True))
    async def get_handler(event):
        url = event.pattern_match.group(1)
        await event.edit(f"⏳ Sedang fetch: {url}")
        match_ext = re.search(r"\.([a-zA-Z0-9]+)(?:\?|$)", url)
        ext = match_ext.group(1).lower() if match_ext else None

        try:
            async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
                async with session.get(url) as resp:
                    content_type = resp.headers.get('Content-Type', '').lower()
                    data = await resp.read()
            if ext or any(x in content_type for x in ['image', 'video', 'audio', 'application']):
                if not ext:
                    ext = mimetypes.guess_extension(content_type.split(";")[0].strip())
                if not ext:
                    ext = ''

                filename = f"file{ext}"
                with open(filename, 'wb') as f:
                    f.write(data)
                await event.client.send_file(
                    event.chat_id,
                    filename,
                    caption=f"📁 File dari {url}\n\nPowered By PeeX-Userbot\nt.me/sharingscript"
                )
                os.remove(filename)

            else:
                filename = "source.html"
                with open(filename, 'wb') as f:
                    f.write(data)
                await event.client.send_file(
                    event.chat_id,
                    filename,
                    caption=f"📄 Source HTML dari {url}\n\nPowered By PeeX-Userbot\nt.me/sharingscript"
                )
                os.remove(filename)

            await event.delete()

        except Exception as e:
            await event.edit(f"❌ Gagal fetch: {e}")
