# Coded By PeeX Authority 
# Please Join Telegram Channel For Updated
# PeeX - Userbot
# t.me/peexubot
# t.me/peex_ubot
import requests
import os
from telethon import events

# API URLs
API_URLS = {
    "youtube": "https://fastrestapis.fasturl.cloud/downup/ytmp4?url={}&quality=360&server=auto",
    "tiktok": "https://fastrestapis.fasturl.cloud/downup/ttdown?url={}",
    "instagram": "https://fastrestapis.fasturl.cloud/downup/igdown?url={}",
    "spotify": "http://localhost:3010/api/spotify?url={}"
}

def register(client):
    @client.on(events.NewMessage(pattern=r"^\.dl (\w+) (https?://\S+)", outgoing=True))
    async def download_media(event):
        args = event.pattern_match.groups()
        media_type, link = args[0].lower(), args[1]

        if media_type not in API_URLS:
            return await event.reply("> **Tipe tidak valid! Gunakan:** youtube, tiktok, instagram, spotify.")

        api_url = API_URLS[media_type].format(link)

        try:
            response = requests.get(api_url)
            if response.status_code != 200:
                return await event.reply("> **Gagal mendapatkan data dari API.**")

            data = response.json()

            if media_type == "tiktok":
                if "videoUrl" not in data or "result" not in data:
                    return await event.reply("> **Gagal mendapatkan file dari TikTok!**")
                
                file_url = data["videoUrl"]
                title = data["result"]["title"]
                description = title
                duration = data.get("duration", "Tidak ada")

            elif media_type == "youtube":
                if "media" not in data or "title" not in data or "description" not in data:
                    return await event.reply("> **Gagal mendapatkan file dari YouTube!**")
                
                file_url = data["media"]
                title = data["title"]
                description = data["description"]
                duration = data.get("duration", "Tidak ada")

            elif media_type == "spotify":
                if "download" not in data or "cover" not in data or "title" not in data or "duration" not in data:
                    return await event.reply("> **Gagal mendapatkan file dari Spotify!**")
                
                file_url = data["download"]
                title = data["title"]
                description = data["title"]
                duration = data["duration"]

            elif media_type == "instagram":
                if "url" not in data:
                    return await event.reply("> **Gagal mendapatkan file dari Instagram!**")
                
                file_url = data["url"]
                title = data.get("title", "Tidak ada")
                description = data.get("desc", "Tidak ada")
                duration = data.get("duration", "Tidak ada")

            file_path = f"{media_type}.mp4" if media_type in ["youtube", "tiktok", "instagram"] else f"{media_type}.mp3"
            with open(file_path, "wb") as file:
                file.write(requests.get(file_url).content)

            caption = f"""
> « « sᴜᴄᴄᴇsғᴜʟʟʏ ᴅᴏᴡɴʟᴏᴀᴅ » »
> | • ᴛʏᴘᴇ : {media_type}
> | • ᴛɪᴛʟᴇ : <a href="{link}">{title}</a>
> | • ᴅᴇsᴄʀɪᴘᴛɪᴏɴ : {description}
> | • ᴅᴜʀᴀᴛɪᴏɴ : {duration}
"""

            await event.respond(file=file_path, caption=caption, parse_mode="html")

            os.remove(file_path)

        except Exception as e:
            await event.reply(f"> **Error:** {str(e)}")
