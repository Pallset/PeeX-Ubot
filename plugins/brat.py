# Coded By PeeX Authority 
# Please Join Telegram Channel For Updated
# PeeX - Userbot
# t.me/peexubot
# t.me/peex_ubot
import os
from PIL import Image, ImageDraw, ImageFont
from telethon import events

FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # Ganti kalau perlu
STICKER_PATH = "brat_sticker.webp"
IMG_SIZE = (76, 76)  # Ukuran canvas

def generate_brat_image(text, text_color, bg_color):
    img = Image.new("RGB", IMG_SIZE, bg_color)
    draw = ImageDraw.Draw(img)

    font_size = 120
    try:
        font = ImageFont.truetype(FONT_PATH, font_size)
    except:
        font = ImageFont.load_default()

    x, y = 10, 10
    words = text.split()
    line_spacing = font_size * 0.1

    for word in words:
        draw.text((x, y), word, fill=text_color, font=font)
        y += int(line_spacing)

    img.save(STICKER_PATH, "WEBP")
    return STICKER_PATH

def register(client):
    @client.on(events.NewMessage(pattern=r"^\.brat (.+)", outgoing=True))
    async def brat(event):
        args = event.pattern_match.group(1).split("|")

        if len(args) != 3:
            await event.edit("> **Format salah!** Gunakan: `.brat teks|warna teks|warna background`")
            return

        text, text_color, bg_color = args

        try:
            await event.edit("> **Processing...**")
            sticker_path = generate_brat_image(text, text_color, bg_color)

            with open(sticker_path, "rb") as sticker:
                await event.client.send_file(event.chat_id, sticker, force_document=False, reply_to=event.reply_to_msg_id)

            await event.delete()
            os.remove(sticker_path)

        except Exception as e:
            await event.edit(f"> **Error:** {str(e)}")
