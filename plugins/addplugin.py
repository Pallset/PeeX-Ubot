# Coded By PeeX Authority 
# Please Join Telegram Channel For Updated
# PeeX - Userbot
# t.me/peexubot
# t.me/peex_ubot
import os
import datetime
from telethon import events

PLUGIN_FOLDER = "plugins"

def register(client):
    @client.on(events.NewMessage(pattern=r"^\.addplugin(?:\s+(.+))?", outgoing=True))
    async def add_plugin(event):
        args = event.pattern_match.group(1)

        if event.reply_to and not args:
            reply_msg = await event.get_reply_message()
            if not reply_msg.media:
                return await event.edit("> **Reply ke file plugin yang valid!**")
            
            file_path = await event.client.download_media(reply_msg, PLUGIN_FOLDER)
            plugin_name = os.path.basename(file_path)
        elif args and "|" in args:
            try:
                code, filename = args.split("|", 1)
                filename = filename.strip()
                if not filename.endswith(".py"):
                    filename += ".py"

                file_path = os.path.join(PLUGIN_FOLDER, filename)
                with open(file_path, "w") as f:
                    f.write(code)
                
                plugin_name = filename
            except Exception as e:
                return await event.edit(f"> **Error:** {str(e)}")
        else:
            return await event.edit("> **Format tidak valid!**")

        commands = []
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
                for line in lines:
                    if line.strip().startswith("@client.on(events.NewMessage(pattern="):
                        cmd = line.split('"')[1]
                        commands.append(cmd)
        except:
            pass

        command_list = ", ".join(commands) if commands else "Tidak terdeteksi"

        time_added = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        success_message = f"""
<blockquote>
> « « sᴜᴄᴄᴇsғᴜʟʟʏ ᴀᴅᴅᴇᴅ ᴘʟᴜɢ-ɪɴ » »
> | • ɴᴀᴍᴇ : {plugin_name}
> | • ᴛɪᴍᴇ : {time_added}
> | • ᴄᴏᴍᴍᴀɴᴅ : {command_list}
</blockquote>
"""
        await event.edit(success_message, parse_mode="html")
