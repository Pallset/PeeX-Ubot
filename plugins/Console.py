# Coded By PeeX Authority 
# Please Join Telegram Channel For Updated
# PeeX - Userbot
# t.me/peexubot
# t.me/peex_ubot
from telethon import events
import asyncio
import subprocess

def register(client):
    @client.on(events.NewMessage(pattern=r"^=> (.+)", outgoing=True))
    async def run_shell(event):
        cmd = event.pattern_match.group(1)

        try:
            process = await asyncio.create_subprocess_shell(
                cmd,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            stdout, stderr = await process.communicate()

            output = stdout.decode().strip()
            error = stderr.decode().strip()

            if not output and not error:
                result = "✅ Perintah dijalankan, tapi tidak ada output."
            else:
                result = output if output else error

            if len(result) > 4096:
                result = result[:4093] + "..."

            await event.reply(f"📥 Hasil:\n<blockquote>{result}</blockquote>", parse_mode="html")

        except Exception as e:
            await event.reply(f"❌ Gagal:\n<blockquote>{e}</blockquote>", parse_mode="html")
