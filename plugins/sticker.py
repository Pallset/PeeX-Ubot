# Coded By PeeX Authority 
# Please Join Telegram Channel For Updated
# PeeX - Userbot
# t.me/peexubot
# t.me/peex_ubot
import os
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
from telethon import events

STICKER_PATH = "sticker.webp"
FONT_PATH = "./font/3.otf"

def wrap_text(text, width=25):
    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        if len(current_line + " " + word) <= width:
            current_line += " " + word if current_line else word
        else:
            lines.append(current_line)
            current_line = word

    if current_line:
        lines.append(current_line)

    return "\n".join(lines)

def generate_meme(image_path, text):
    img = Image.open(image_path).convert("RGBA")
    img = img.resize((512, int(512 * img.height / img.width)), Image.LANCZOS)

    if text:
        draw = ImageDraw.Draw(img)
        try:
            font = ImageFont.truetype(FONT_PATH, 40)
        except OSError:
            font = ImageFont.load_default()

        wrapped_text = wrap_text(text, width=25)
        text_width, text_height = draw.textbbox((0, 0), wrapped_text, font=font)[2:]
        text_x = (img.width - text_width) // 2
        text_y = img.height - text_height - 20

        # Shadow (biar keliatan)
        for offset in [(-2, -2), (-2, 2), (2, -2), (2, 2)]:
            draw.text((text_x + offset[0], text_y + offset[1]), wrapped_text, font=font, fill="black")

        draw.text((text_x, text_y), wrapped_text, fill="white", font=font)

    img.save(STICKER_PATH, "WEBP")
    return STICKER_PATH

def register(client):
    @client.on(events.NewMessage(pattern=r"^\.(s|sticker)$", outgoing=True))
    async def sticker_cmd(event):
        if event.is_reply:
            reply_msg = await event.get_reply_message()
            if reply_msg.media:
                img_path = await reply_msg.download_media()
                sticker = generate_meme(img_path, "")  
                await event.client.send_file(event.chat_id, sticker, reply_to=event.reply_to_msg_id, force_document=False, file_type="sticker")
                os.remove(sticker)
                os.remove(img_path)
                await event.delete()
            else:
                await event.edit("Reply ke gambar!")
        else:
            await event.edit("Gunakan .s atau .sticker dengan reply ke gambar!")

    @client.on(events.NewMessage(pattern=r"^\.(smeme|stickermeme) (.+)$", outgoing=True))
    async def meme_cmd(event):
        text = event.pattern_match.group(2)
        if event.is_reply:
            reply_msg = await event.get_reply_message()
            if reply_msg.media:
                img_path = await reply_msg.download_media()
                sticker = generate_meme(img_path, text)  
                await event.client.send_file(event.chat_id, sticker, reply_to=event.reply_to_msg_id, force_document=False, file_type="sticker")
                os.remove(sticker)
                os.remove(img_path)
                await event.delete()
            else:
                await event.edit("Reply ke gambar untuk membuat meme!")
        else:
            await event.edit("Gunakan .smeme <teks> dengan reply ke gambar!")
