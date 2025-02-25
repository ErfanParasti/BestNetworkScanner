import os
import time
import json
import ipaddress
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# تابع برای پاک کردن صفحه نمایش
def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")

# تابع برای نمایش هدر برنامه
def display_header():
    clear_screen()
    logo = """
        _____                     _____                    _____          
       /\\    \\                   /\\    \\                  /\\    \\             | 
      /::\\    \\                 /::\\____\\                /::\\    \\            | 
     /::::\\    \\               /::::|   |               /::::\\    \\           | 
    /::::::\\    \\             /:::::|   |              /::::::\\    \\          | 
   /:::/\\:::\\    \\           /::::::|   |             /:::/\\:::\\    \\         | 
  /:::/__\\:::\\    \\         /:::/|::|   |            /:::/__\\:::\\    \\        | 
 \\::::\\   \\:::\\    \\       /:::/ |::|   |            \:::\\   \\:::\\    \\       | 
  \\::::\\::\\    \\::::\\     /:::/  |::|   | _____    ___\:::\\   \\:::\\    \\      | 
   \\:::\\:::\\    \\::::\\___/:::/   |::|   |/\\    \\  /\\   \\:::\\   \\:::\\    \\     | 
    \\:::\\:::\\   \\::::|   /:: /   |::|   /::\\____\\/::\\   \\:::\\   \\:::\\____\\    |     
     \\:::\\:::\\  /::::|___/:::/   |::|  /:::/    /\\:::\\   \\:::\\   \\::/    /    | 
      \\:::\\:::\\/:/    / \\::/    /|::| /:::/    /  \\:::\\   \\:::\\   \\/____/     | 
       \\::::::::/    /   \\/____/ |::|/:::/    /    \\:::\\   \\::::\\    \\        | 
        \\::::::/    /            |::::::/    /      \\:::\\   \\:::\\_____\\       | 
         \\::::/    /             |:::::/    /        \\:::\\  /:::/    /        | 
          \\::/____/              |::::/    /          \\:::\\/:::/    /         | 
           ~~                    /:::/    /            \\::::::/    /          | 
                                 \::/    /              \\::::/    /           | 
                                  \/____/                \\/______/            |
______________________________________________________________________________|
                                                  __  __  _/_/_/_/_/_/_/_/_/_/
    Program   : Best_Network_Scanner   /::\\/::\\/:/ 
    Version   : 1.0.5                            \\::::::/:/
    Developer : Your Friend                       \\::::/:/
______________________________________________     \\::/:/
_/_/_/-----------------/_/_/_/_/_/_/_/_/_/_/_/______\\/_/
    """
    print(Fore.GREEN + Style.BRIGHT + logo)

# نمایش منوی اصلی
def main_menu():
    display_header()
    print(Fore.CYAN + "[ 1 ] Network Scan")
    print(Fore.CYAN + "[ 2 ] Set IP Range")
    print(Fore.CYAN + "[ 3 ] Services")
    print(Fore.CYAN + "[ 4 ] Pre Results")
    print(Fore.CYAN + "[ 5 ] Target")
    print(Fore.CYAN + "[ 00 ] Exit")
    print("\n----------------------------------------------------------------------------")
    choice = input(Fore.YELLOW + Style.BRIGHT + "Your Choice? : ")
    return choice

# تابع برای تنظیم محدوده IP (گزینه ۲)
def set_ip_range():
    display_header()
    print(Fore.YELLOW + "Enter IP range in CIDR format (e.g., 192.168.1.0/24):")
    ip_range = input(Fore.CYAN + "IP Range: ")

    try:
        # بررسی معتبر بودن محدوده IP
        network = ipaddress.IPv4Network(ip_range, strict=False)
        save_json("range.json", {"range": ip_range})
        print(Fore.GREEN + f"IP range {ip_range} saved successfully!")
    except ValueError:
        print(Fore.RED + "Invalid IP range! Please try again.")

    time.sleep(2)
    clear_screen()

# تابع برای نمایش منوی خدمات (گزینه ۳)-------------------------------------------------------
def services_menu():
    display_header()
    print(Fore.CYAN + "[ 1 ] Ping Sweep")
    print(Fore.CYAN + "[ 2 ] Port Scan")
    print(Fore.CYAN + "[ 3 ] OS Detection")
    print(Fore.CYAN + "[ 00 ] Back to Main Menu")
    print("\n----------------------------------------------------------------------------")
    
    choice = input(Fore.YELLOW + Style.BRIGHT + "Your Choice? : ")

    if choice == "1":
        print(Fore.GREEN + "Starting Ping Sweep...")
        # اینجا می‌تونی تابع پینگ اسکن رو اضافه کنی
        time.sleep(2)

    elif choice == "2":
        print(Fore.GREEN + "Starting Port Scan...")
        # اینجا می‌تونی تابع اسکن پورت رو اضافه کنی
        time.sleep(2)

    elif choice == "3":
        print(Fore.GREEN + "Starting OS Detection...")
        # اینجا می‌تونی تابع تشخیص سیستم‌عامل رو اضافه کنی
        time.sleep(2)

    elif choice == "00":
        return

    else:
        print(Fore.RED + "Invalid choice! Try again.")
        time.sleep(2)
        

    clear_screen()


# بررسی خصوصی بودن IP =======================================
# def is_private_ip(ip):
#     try:
#         addr = ipaddress.IPv4Address(ip)
#         return addr.is_private
#     except ValueError:
#         return False

# ذخیره و خواندن فایل JSON
def save_json(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

def read_json(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# نمایش نتایج اسکن‌شده (گزینه ۴)
def show_scan_results():
    data = read_json("scan_results.json")
    if not data:
        print(Fore.RED + "No scan results found!")
    else:
        print(Fore.YELLOW + "\nScan Results:")
        for entry in data:
            print(Fore.GREEN + f"ID: {entry['id']}, IP: {entry['ip']}, State: {entry['state']}")
    input(Fore.CYAN + "\nPress Enter to return...")
    clear_screen()

# نمایش اهداف ذخیره‌شده (گزینه ۵)
def show_targets():
    data = read_json("target.json")
    if not data:
        print(Fore.RED + "No targets found!")
    else:
        print(Fore.YELLOW + "\nSaved Targets:")
        for entry in data:
            print(Fore.GREEN + f"Target IP: {entry['ip']}, State: {entry['state']}")
    input(Fore.CYAN + "\nPress Enter to return...")
    clear_screen()

# اجرای برنامه اصلی
def main():
    while True:
        choice = main_menu()

        if choice == "1":  # Network Scan
            ip_range = read_json("range.json")
            if not ip_range:  # بررسی اینکه رنج تنظیم شده یا نه
                print(Fore.RED + "No IP range selected! Please set an IP range first.")
                time.sleep(2)
                set_ip_range()
            else:
                services_menu()

        elif choice == "2":
            set_ip_range()

        elif choice == "3":
            services_menu()

        elif choice == "4":  # نمایش نتایج اسکن‌شده
            show_scan_results()

        elif choice == "5":  # نمایش تارگت‌های ذخیره‌شده
            show_targets()

        elif choice == "00":
            print(Fore.YELLOW + "Exiting...")
            time.sleep(1)
            break

        else:
            print(Fore.RED + "Invalid choice, try again!")
            time.sleep(2)

if __name__ == "__main__":
    main()

         