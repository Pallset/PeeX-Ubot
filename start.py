import subprocess
import requests
import sys
from colorama import init, Fore, Style

init(autoreset=True)

banner = f"""{Fore.CYAN}
███████╗████████╗ █████╗ ██████╗ ████████╗
██╔════╝╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝
███████╗   ██║   ███████║██████╔╝   ██║   
╚════██║   ██║   ██╔══██║██╔═══╝    ██║   
███████║   ██║   ██║  ██║██║        ██║   
╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝        ╚═╝   
{Style.RESET_ALL}
"""

print(banner)
print(f"{Fore.MAGENTA}Key diperlukan untuk menjalankan program ini.")
print(f"{Fore.YELLOW}Key bisa diambil dari: https://raw.githubusercontent.com/PallSet/MYAPI/main/security.txt\n")

key_input = input(f"{Fore.GREEN}Please Enter The Key =>> {Style.RESET_ALL}")

try:
    response = requests.get("https://raw.githubusercontent.com/PallSet/MYAPI/main/security.txt")
    if response.status_code == 200:
        valid_keys = [line.strip() for line in response.text.splitlines()]
        if key_input in valid_keys:
            print(f"{Fore.GREEN}✅ Key Valid! Menjalankan script...\n")

            main_proc = subprocess.Popen(["python", "main.py"])
            bot_proc = subprocess.Popen(["python", "bot.py"])

            main_proc.wait()
            bot_proc.wait()
        else:
            print(f"{Fore.RED}❌ Key Salah! Program dihentikan.")
            sys.exit()
    else:
        print(f"{Fore.RED}Gagal mengambil key dari GitHub.")
        sys.exit()
except Exception as e:
    print(f"{Fore.RED}Terjadi error: {e}")
    sys.exit()
