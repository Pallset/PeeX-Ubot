# Coded By PeeX Authority 
# Please Join Telegram Channel For Updated
# PeeX - Userbot
# t.me/peexubot
# t.me/peex_ubot
from telethon import events
from telethon.tl.functions.account import ReportPeerRequest
from telethon.tl.types import (
    InputReportReasonSpam,
    InputReportReasonFake,
    InputReportReasonViolence,
    InputReportReasonPornography,
    InputReportReasonChildAbuse,
    InputReportReasonCopyright,
    InputReportReasonIllegalDrugs,
    InputReportReasonPersonalDetails,
    InputReportReasonOther
)
import asyncio
import os

REASONS = {
    "spam": InputReportReasonSpam(),
    "fake": InputReportReasonFake(),
    "violence": InputReportReasonViolence(),
    "porn": InputReportReasonPornography(),
    "child": InputReportReasonChildAbuse(),
    "copyright": InputReportReasonCopyright(),
    "drugs": InputReportReasonIllegalDrugs(),
    "personal": InputReportReasonPersonalDetails(),
    "other": InputReportReasonOther()
}

DEFAULT_REASON = "spam"
DEFAULT_COUNT = 5
DEFAULT_MESSAGE = "This channel is constantly scamming people by promoting fake giveaways and phishing links. Immediate action is needed to prevent users from being harmed."

def register(client):
    @client.on(events.NewMessage(pattern=r"^\.banch(?:\s+([\S]+))?(?:\s+(\w+))?(?:\s+(\d+))?$", outgoing=True))
    async def handler(event):
        args = event.pattern_match.groups()
        target = args[0]
        reason_key = args[1] or DEFAULT_REASON
        count = int(args[2]) if args[2] else DEFAULT_COUNT

        if not target:
            await event.edit("Gunakan: `.banch <username/channel_id> <reason> <jumlah>`\nContoh: `.banch @kontolchannel spam 10`")
            return

        reason = REASONS.get(reason_key.lower())
        if not reason:
            await event.edit(f"Alasan tidak valid. Gunakan salah satu dari: {', '.join(REASONS.keys())}")
            return

        try:
            entity = await client.get_entity(target)
        except Exception as e:
            await event.edit(f"Gagal ambil target: {e}")
            return

        await event.edit(f"Mulai nge-report {target} sebanyak {count}... 😼")

        success = 0
        for i in range(count):
            try:
                await client(ReportPeerRequest(
                    peer=entity,
                    reason=reason,
                    message=DEFAULT_MESSAGE
                ))
                success += 1
                await asyncio.sleep(2)
            except Exception as e:
                await event.respond(f"Gagal report ke-{i+1}: {e}")
                break

        await event.respond(f"✅ Berhasil report {target} sebanyak {success}x.")
        await event.delete()
