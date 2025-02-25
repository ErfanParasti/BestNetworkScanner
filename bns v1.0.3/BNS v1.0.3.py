import os
import time
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
       /\    \                   /\    \                  /\    \             | 
      /::\    \                 /::\____\                /::\    \            | 
     /::::\    \               /::::|   |               /::::\    \           | 
    /::::::\    \             /:::::|   |              /::::::\    \          | 
   /:::/\:::\    \           /::::::|   |             /:::/\:::\    \         | 
  /:::/__\:::\    \         /:::/|::|   |            /:::/__\:::\    \        | 
 \::::\   \:::\    \       /:::/ |::|   |            \:::\   \:::\    \       | 
  \::::\::\    \::::\     /:::/  |::|   | _____    ___\:::\   \:::\    \      | 
   \:::\:::\    \::::\___/:::/   |::|   |/\    \  /\   \:::\   \:::\    \     | 
    \:::\:::\   \::::|   /:: /   |::|   /::\____\/::\   \:::\   \:::\____\    |     
     \:::\:::\  /::::|___/:::/   |::|  /:::/    /\:::\   \:::\   \::/    /    | 
      \:::\:::\/:/    / \::/    /|::| /:::/    /  \:::\   \:::\   \/____/     | 
       \::::::::/    /   \/____/ |::|/:::/    /    \:::\   \::::\    \        | 
        \::::::/    /            |::::::/    /      \:::\   \:::\_____\       | 
         \::::/    /             |:::::/    /        \:::\  /:::/    /        | 
          \::/____/              |::::/    /          \:::\/:::/    /         | 
           ~~                    /:::/    /            \::::::/    /          | 
                                 \::/    /              \::::/    /           | 
                                  \/____/                \/______/            |
                                                                              |
______________________________________________________________________________|
                                                  _   _  /_/_/_/_/_/_/_/_/_/_/
    Program   : Best_Network_Scanner             /-\:/-\\/:/ 
    Version   : 1.0.3                            \:::::/:/
    Developer : Your Friend                       \:::/:/
_____________________________________________      \:/:/
/_/_/-----------------/_/_/_/_/_/_/_/_/_/_/_|_______/_/
    """
    print(Fore.GREEN + Style.BRIGHT + logo)  # لوگو با رنگ سبز روشن

# تابع برای نمایش منوی اصلی
def main_menu():
    display_header()
    print(Fore.CYAN + "[ 1 ] Network Scan")
    print(Fore.CYAN + "[ 2 ] IP Range Set (Default: 0.0.0.0)")
    print(Fore.CYAN + "[ 3 ] Services")
    print(Fore.CYAN + "[ 4 ] Pre Results")
    print("----------------------------------------------------------------------------")
    choice = input(Fore.YELLOW + Style.BRIGHT + "Your Choice? : ")
    return choice

# تابع برای نمایش زیرمنوی گزینه Services
def services_menu():
    display_header()
    print(Fore.YELLOW + "[ 1 ] Start Service")
    print(Fore.YELLOW + "[ 2 ] Stop Service")
    print(Fore.YELLOW + "[ 3 ] Restart Service")
    print(Fore.YELLOW + "[ 4 ] Back to Main Menu")
    print("----------------------------------------------------------------------------")
    choice = input(Fore.YELLOW + Style.BRIGHT + "Your Choice? : ")
    return choice

# تابع برای نمایش خطاها
def show_error(message):
    print(Fore.RED + Style.BRIGHT + "[ERROR] " + message)

# تابع برای نمایش هشدارها
def show_warning(message):
    print(Fore.YELLOW + Style.BRIGHT + "[WARNING] " + message)

# تابع اصلی برای مدیریت ناوبری بین منوها
def main():
    while True:
        choice = main_menu()
        if choice == "1":
            print(Fore.GREEN + "Network Scan selected.")
            time.sleep(2)
            
        elif choice == "2":
            print(Fore.GREEN + "IP Range Set selected.")
            time.sleep(2)

        elif choice == "3":
            while True:
                service_choice = services_menu()
                if service_choice == "4":
                    break
                elif service_choice == "1":
                    print(Fore.GREEN + "Start Service selected.")
                elif service_choice == "2":
                    print(Fore.GREEN + "Stop Service selected.")
                elif service_choice == "3":
                    print(Fore.GREEN + "Restart Service selected.")
                else:
                    show_error("Invalid option in Services Menu!")
                time.sleep(2)
        elif choice == "4":
            print(Fore.GREEN + "Pre Results selected.")
            time.sleep(2)
        else:
            show_error("Invalid option in Main Menu!")
            time.sleep(2)


if __name__ == "__main__":
    main()
