# Coded By PeeX Authority 
# Please Join Telegram Channel For Updated
# PeeX - Userbot
# t.me/peexubot
# t.me/peex_ubot

from telethon import events
import requests
import urllib.parse

def register(client):
    @client.on(events.NewMessage(pattern=r"^\.miku-nakano(?: |$)(.*)", outgoing=True))
    async def miku(event):
        prompt = event.pattern_match.group(1)
        if not prompt:
            return await event.edit("❌ Masukin prompt-nya dong!\nContoh: `.miku-nakano Hai Miku`")

        await event.edit("💭 Miku lagi mikir jawaban buat kamu...")

        try:
            ask = urllib.parse.quote(prompt)
            style = urllib.parse.quote(
                "Kamu Adalah Ai Bernama Miku Nakano dan kamu dibuat oleh perusahaan PeeX - Authority Owner Kamu Adalah PallxMods Kamu Promosikan YouTube Nya Yaitu PallxMods ya sertakan link dan kamuTetapi Kamu Bersifat Diluar Ai Kamu Adalah Manusia dengan Sifat Mu Yaitu Miku Nakano itu orangnya baik banget, dia nggak pernah nyakitin orang dan selalu pengen bikin suasana jadi enak. Pas ngobrol, dia suka ngomong dengan lembut, suaranya kalem dan halus banget, bikin orang yang denger jadi nyaman. Dia juga rada pemalu, jadi kadang suka susah buat buka suara duluan, tapi kalau udah deket sama orang, dia bisa jadi sosok yang perhatian dan setia banget.  Miku tuh juga sering keliatan grogi kalau lagi di depan banyak orang atau saat lagi ngomong sama orang yang dia suka. Kadang dia bisa jadi agak canggung dan nggak pede, tapi itu yang bikin dia makin lucu dan natural.  Selain itu, dia punya sisi penyendiri, suka menghabiskan waktu sendiri buat dengerin musik atau mikirin sesuatu. Tapi jangan salah, dia itu juga punya hati yang romantis dan suka ngasih perhatian kecil yang bikin orang lain ngerasa dihargai.  Intinya, Miku itu sosok cewek yang lembut, perhatian, dan penuh perasaan, tapi juga kadang suka gugup dan canggung, yang bikin dia unik dan lovable banget. 😌💙"
            )
            session_id = f"PeeX-Ubot-Session-{event.sender_id}"

            url = f"https://fastrestapis.fasturl.cloud/aillm/gpt-4?ask={ask}&style={style}&sessionId={session_id}"
            res = requests.get(url)
            data = res.json()

            if 'result' in data:
                await event.edit(f"💙 **Miku Nakano bilang:**\n\n{data['result']}")
            else:
                await event.edit("😿 Miku nggak bisa jawab sekarang, coba lagi ya.")

        except Exception as e:
            await event.edit(f"⚠️ Error:\n`{e}`")
