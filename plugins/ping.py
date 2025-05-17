import asyncio
import platform
import os
import psutil
import socket
import urllib.request
from datetime import timedelta
from telethon import events

def get_uptime():
    try:
        output = os.popen("uptime -p").read().strip()  # Contoh hasil: "up 2 hours, 5 minutes"
        return output.replace("up ", "")
    except:
        return "0 minutes"

async def get_ping():
    try:
        proc = await asyncio.create_subprocess_shell(
            "ping -c 1 8.8.8.8 | grep 'time='",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, _ = await proc.communicate()
        result = stdout.decode()
        if "time=" in result:
            return result.split("time=")[-1].split(" ")[0]
        else:
            return "Timeout"
    except:
        return "Unavailable"

def get_ip():
    try:
        return urllib.request.urlopen('https://api.ipify.org').read().decode()
    except:
        return "Tidak Bisa Diakses"

def get_ram_usage():
    ram = psutil.virtual_memory()
    used = ram.used // (1024 * 1024)
    total = ram.total // (1024 * 1024)
    return f"{used}MB / {total}MB ({ram.percent}%)"

def get_cpu_usage():
    try:
        # Jalankan top 1 baris dan ambil CPU%
        output = os.popen("top -bn1 | grep 'CPU'").read()
        if not output:
            output = os.popen("top -n 1").read()
        return output.strip().split("\n")[0]  # Ambil baris pertama aja
    except Exception as e:
        return "CPU usage unavailable"

def get_disk_usage():
    disk = psutil.disk_usage('/')
    used = disk.used // (1024 * 1024 * 1024)
    total = disk.total // (1024 * 1024 * 1024)
    percent = disk.percent
    return f"{used}GB / {total}GB ({percent}%)"

def get_python_info():
    return f"{platform.python_version()} ({platform.architecture()[0]})"

def register(client):
    @client.on(events.NewMessage(pattern=r"^\.ping$"))
    async def ping_handler(event):
        msg = await event.reply("🔄 Collecting system info...")

        ping = await get_ping()
        os_info = f"{platform.system()} {platform.release()} ({platform.machine()})"
        uptime = get_uptime()
        ram = get_ram_usage()
        cpu = get_cpu_usage()
        ip = get_ip()
        disk = get_disk_usage()
        py_info = get_python_info()
        cores = os.cpu_count()

        await msg.edit(
            f"> 📡 **PING** : `{ping}`\n"
            f"> 🖥️ **OS** : `{os_info}`\n"
            f"> ⏱️ **UPTIME** : `{uptime}`\n"
            f"> 💾 **RAM** : `{ram}`\n"
            f"> 🧠 **CPU** : `{cpu}`\n"
            f"> 🌐 **PUBLIC IP** : `{ip}`\n"
            f"> 🧰 **PYTHON** : `{py_info}`\n"
            f"> 🧱 **CORES** : `{cores}`\n"
            f"> 📁 **DISK** : `{disk}`"
        )
