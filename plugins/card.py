# Coded By PeeX Authority 
# Please Join Telegram Channel For Updated
# PeeX - Userbot
# t.me/peexubot
# t.me/peex_ubot
import os
import json
import requests
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps
from telethon import events

BACKGROUND_URL = "https://wallpapercave.com/wp/wp11917343.jpg"
BACKGROUND_PATH = "background.jpg"
FONT_PATH = "./font/2.otf"
ID_CARD_PATH = "id_card.png"
SCAM_JSON_PATH = "scam.json"

if not os.path.exists(BACKGROUND_PATH):
    r = requests.get(BACKGROUND_URL)
    with open(BACKGROUND_PATH, "wb") as f:
        f.write(r.content)

def get_custom_font(size):
    return ImageFont.truetype(FONT_PATH, size)

def load_scam_db():
    if os.path.exists(SCAM_JSON_PATH):
        try:
            with open(SCAM_JSON_PATH, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}
    return {}

def generate_id_card(user_info, profile_photo_path):
    base = Image.open(BACKGROUND_PATH).resize((800, 400)).convert("RGB")
    blurred = base.filter(ImageFilter.GaussianBlur(8))
    draw = ImageDraw.Draw(blurred)

    overlay = Image.new("RGBA", (720, 320), (0, 0, 0, 160))
    blurred.paste(overlay, (40, 40), overlay)

    title_font = get_custom_font(36)
    text_font = get_custom_font(24)

    if profile_photo_path and os.path.exists(profile_photo_path):
        pfp = Image.open(profile_photo_path).resize((120, 120)).convert("RGB")
        mask = Image.new("L", (120, 120), 0)
        draw_mask = ImageDraw.Draw(mask)
        draw_mask.ellipse((0, 0, 120, 120), fill=255)
        pfp.putalpha(mask)
        blurred.paste(pfp, (60, 100), pfp)

    text_x = 200
    start_y = 100
    spacing = 40
    draw.text((text_x, start_y), "Telegram ID Card", font=title_font, fill="white")
    draw.text((text_x, start_y + spacing), f"First Name: {user_info.get('first_name', 'N/A')}", font=text_font, fill="white")
    draw.text((text_x, start_y + spacing * 2), f"Last Name: {user_info.get('last_name', 'N/A')}", font=text_font, fill="white")
    draw.text((text_x, start_y + spacing * 3), f"Username: @{user_info.get('username', 'N/A')}", font=text_font, fill="white")
    draw.text((text_x, start_y + spacing * 4), f"User ID: {user_info['id']}", font=text_font, fill="#00ffc3")

    scam_db = load_scam_db()
    uid = str(user_info['id'])
    if uid in scam_db:
        draw.text((text_x, start_y + spacing * 5), f"⚠️ SCAMMER: {scam_db[uid]}", font=text_font, fill="red")

    blurred.save(ID_CARD_PATH)
    return ID_CARD_PATH

def register(client):
    @client.on(events.NewMessage(pattern=r"^\.(idcard|idc)(?:\s+(.*))?$", outgoing=True))
    async def idcard(event):
        input_text = event.pattern_match.group(2)
        user = None

        if event.is_reply:
            reply = await event.get_reply_message()
            user = await reply.get_sender()
        elif input_text:
            try:
                user = await client.get_entity(input_text)
            except Exception:
                await event.edit("User tidak ditemukan!")
                return
        else:
            user = await event.get_sender()

        photo_path = await client.download_profile_photo(user.id, "profile.jpg") if user.photo else None

        user_info = {
            "first_name": user.first_name or "N/A",
            "last_name": user.last_name or "N/A",
            "full_name": f"{user.first_name or ''} {user.last_name or ''}",
            "username": user.username or "N/A",
            "id": user.id
        }

        try:
            await event.edit("Generating ID Card...")
            id_card = generate_id_card(user_info, photo_path)

            await client.send_file(event.chat_id, id_card, caption="Here's the ID card", reply_to=event.reply_to_msg_id)
            await event.delete()

            if os.path.exists(ID_CARD_PATH): os.remove(ID_CARD_PATH)
            if photo_path and os.path.exists(photo_path): os.remove(photo_path)

        except Exception as e:
            await event.edit(f"Error: {str(e)}")
