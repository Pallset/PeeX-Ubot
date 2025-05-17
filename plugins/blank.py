from telethon import events
import asyncio

BLANK_MODE = False

def register(client):
    global BLANK_MODE

    @client.on(events.NewMessage(pattern=r"^\.blank (on|off)", outgoing=True))
    async def toggle_blank(event):
        global BLANK_MODE
        status = event.pattern_match.group(1)

        if status == "on":
            BLANK_MODE = True
            await event.edit("> **Mode Blank Aktif!** Nama akan otomatis kosong saat mengirim pesan ke channel.")
        else:
            BLANK_MODE = False
            await event.edit("> **Mode Blank Nonaktif!** Nama kembali normal.")

    @client.on(events.NewMessage(outgoing=True))
    async def blank_message(event):
        global BLANK_MODE
        if not BLANK_MODE:
            return
        
        if event.is_channel and not event.is_group:
            user = await client.get_me()
            old_name = user.first_name

            try:
                await client(UpdateProfileRequest(first_name="‎"))
                await asyncio.sleep(0.5)
                await event.respond(event.text)
                await asyncio.sleep(1)
            except:
                pass
            finally:
                await client(UpdateProfileRequest(first_name=old_name))
