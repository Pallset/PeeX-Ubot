# Coded By PeeX Authority 
# Please Join Telegram Channel For Updated
# PeeX - Userbot
# t.me/peexubot
# t.me/peex_ubot
import random
from telethon import events

EMOJIS = ["🔥", "💀", "🚀", "🐱", "👀", "💎", "🍕", "⚡", "🎉", "❤️", "🎭", "👑"]

async def get_members(client, chat_id):
    try:
        members = []
        async for user in client.iter_participants(chat_id):
            if not user.bot and user.username:
                members.append(user)
        return members
    except Exception as e:
        return []

async def mention_users(client, event):
    chat = await event.get_chat()
    members = await get_members(client, chat.id)
    
    if not members:
        await event.edit("Gagal mengambil daftar pengguna!")
        return

    await event.delete()
    
    messages = []
    current_message = ""
    count = 0

    for user in members:
        emoji = random.choice(EMOJIS)
        mention = f'<a href="https://t.me/{user.username}">{emoji}</a>'
        
        if count >= 30:
            messages.append(current_message)
            current_message = ""
            count = 0

        current_message += mention + " "
        count += 1
    
    if current_message:
        messages.append(current_message)

    for msg in messages:
        await client.send_message(chat.id, msg, parse_mode="html")

def register(client):
    @client.on(events.NewMessage(pattern=r"^\.mentionall$", outgoing=True))
    async def mentionall(event):
        await mention_users(client, event)
