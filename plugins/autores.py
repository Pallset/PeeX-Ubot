# Coded By PeeX Authority 
# Please Join Telegram Channel For Updated
# PeeX - Userbot
# t.me/peexubot
# t.me/peex_ubot
import asyncio
from telethon import events

autores_tasks = {}

def register(client):
    @client.on(events.NewMessage(pattern=r"^\.autores\s+(.+)", outgoing=True))
    async def start_autores(event):
        args = event.pattern_match.group(1)

        if "|" not in args:
            return await event.edit("> **Format salah!**\nGunakan: `.autores <id grup/username>|<pesan>|<delay>`")

        try:
            target, text, delay = map(str.strip, args.split("|", 2))
            delay = int(delay)
        except ValueError:
            return await event.edit("> **Delay harus angka dalam detik!**")

        try:
            entity = await client.get_entity(target)
            chat_id = entity.id
        except:
            return await event.edit("> **Grup gak ketemu!**")

        if chat_id in autores_tasks:
            return await event.edit("> ❌ Auto respon udah jalan di grup itu!")

        await event.edit(f"✅ Auto Respon dimulai!\n\n🧾 Chat: `{chat_id}`\n🕒 Delay: `{delay}` detik\n💬 Pesan: `{text}`")

        async def autores_task():
            while True:
                try:
                    await client.send_message(chat_id, text)
                    await asyncio.sleep(delay)
                except Exception as e:
                    print(f"[AUTORESP ERROR] {e}")
                    break

        task = asyncio.create_task(autores_task())
        autores_tasks[chat_id] = task

    @client.on(events.NewMessage(pattern=r"^\.stopres(?:\s+(.+))?", outgoing=True))
    async def stop_autores(event):
        args = event.pattern_match.group(1)

        if not args:
            return await event.edit("> **Gunakan:** `.stopres <id grup/username>`")

        try:
            entity = await client.get_entity(args.strip())
            chat_id = entity.id
        except:
            return await event.edit("> **Grup gak ketemu!**")

        task = autores_tasks.get(chat_id)
        if task:
            task.cancel()
            del autores_tasks[chat_id]
            await event.edit(f"✅ Auto Respon dihentikan untuk grup `{chat_id}`")
        else:
            await event.edit("> ❌ Belum ada auto respon aktif di grup itu.")
