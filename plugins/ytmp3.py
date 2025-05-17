# Coded By PeeX Authority 
# Please Join Telegram Channel For Updated
# PeeX - Userbot
# t.me/peexubot
# t.me/peex_ubot
import os
import requests
from telethon import events
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3

API_URL = "https://fastrestapis.fasturl.cloud/downup/ytdown-v1?name={}&format=mp3&quality=128&server=auto"

def register(client):
    @client.on(events.NewMessage(pattern=r"^.playlagu (.+)", outgoing=True))
    async def _(event):
        query = event.pattern_match.group(1)
        await event.edit(f"🔎 Mencari lagu: `{query}` ...")

        try:
            res = requests.get(API_URL.format(query))
            data = res.json()

            if data["status"] != 200:
                return await event.edit("❌ Gagal mengambil lagu.")

            result = data["result"]
            title = result["title"]
            duration = result["metadata"]["duration"]
            views = result["metadata"]["views"]
            author = result["author"]["name"] or "Tidak diketahui"
            thumbnail_url = result["metadata"]["thumbnail"]
            mp3_url = result["media"]

            filename = f"{title}.mp3"

            mp3_req = requests.get(mp3_url)
            with open(filename, "wb") as f:
                f.write(mp3_req.content)

            try:
                audio = EasyID3(filename)
            except Exception:
                audio = MP3(filename)
                audio.add_tags()
                audio = EasyID3(filename)

            audio["artist"] = "t.me/sharingscript"
            audio["title"] = title
            audio.save()

            thumb_name = "thumb.jpg"
            thumb_req = requests.get(thumbnail_url)
            with open(thumb_name, "wb") as img:
                img.write(thumb_req.content)

            await client.send_file(
                event.chat_id,
                filename,
                caption=(
                    f"🎧 <b>{title}</b>\n"
                    f"👤 <b>Author:</b> {author}\n"
                    f"⏱️ <b>Duration:</b> {duration}\n"
                    f"👁️ <b>Views:</b> {views}\n"
                ),
                voice=False,
                thumb=thumb_name,
                parse_mode="html"
            )
            await event.delete()

            os.remove(filename)
            os.remove(thumb_name)

        except Exception as e:
            await event.edit(f"❌ Error:\n`{str(e)}`")
