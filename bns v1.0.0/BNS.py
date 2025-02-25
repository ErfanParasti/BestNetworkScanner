import os
import time
from colorama import Fore, Back, Style, init

# تابع برای پاک کردن صفحه نمایش
def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")

# تابع برای نمایش هدر برنامه
def display_header():
    # clear_screen()

    logo = """
           _____                     _____                    _____          
          /\    \                   /\    \                  /\    \                   | 
         /::\    \                 /::\____\                /::\    \                  | 
        /::::\    \               /::::|   |               /::::\    \                 | 
       /::::::\    \             /:::::|   |              /::::::\    \                | 
      /:::/\:::\    \           /::::::|   |             /:::/\:::\    \               | 
     /:::/__\:::\    \         /:::/|::|   |            /:::/__\:::\    \              | 
    \::::\   \:::\    \       /:::/ |::|   |            \:::\   \:::\    \             | 
     \::::\::\    \::::\     /:::/  |::|   | _____    ___\:::\   \:::\    \            | 
      \:::\:::\    \::::\___/:::/   |::|   |/\    \  /\   \:::\   \:::\    \           | 
       \:::\:::\   \::::|   /:: /   |::|   /::\____\/::\   \:::\   \:::\____\\          |     
        \:::\:::\  /::::|___/:::/   |::|  /:::/    /\:::\   \:::\   \::/    /          | 
         \:::\:::\/:/    / \::/    /|::| /:::/    /  \:::\   \:::\   \/____/           | 
          \::::::::/    /   \/____/ |::|/:::/    /    \:::\   \::::\    \              | 
           \::::::/    /            |::::::/    /      \:::\   \:::\_____\             | 
            \::::/    /             |:::::/    /        \:::\  /:::/    /              | 
             \::/____/              |::::/    /          \:::\/:::/    /               | 
              ~~                    /:::/    /            \::::::/    /                | 
                                    \::/    /              \::::/    /                 | 
                                     \/____/                \/______/                  |
                                                                                       /
______________________________________________________________________________________/
                                                  _   _    \\
    Program   : Best_Network_Scanner             /-\:/-\\    \\
    ersion    : 1.0.0                            \:::::/    |
    Developer : Your Friend                       \:::/     |
_________________________________________________  \:/      /
        ∟------------------\_____________________\\_________/
    """



    animate_logo(logo)


    # ====================================================================================
# +++++++++++++++++++

    # ====================================================================================


def animate_logo(logo):
    os.system("clear")  # پاک کردن صفحه ترمینال
    for line in logo.split("\n"):
        print(Fore.GREEN + line)
        time.sleep(0.1)  # مکث برای انیمیشن خط‌به‌خط

# تابع برای نمایش منوی اصلی
def main_menu():
    display_header()
    print("[ 1 ] Network Scan")
    print("[ 2 ] IP Range Set (Default: 0.0.0.0)")
    print("[ 3 ] Services")
    print("[ 4 ] Pre Results")
    print("----------------------------------------------------------------------------")
    choice = input("Your Choice? : ")
    return choice

# تابع برای نمایش زیرمنوی گزینه Services
def services_menu():
    display_header()
    print(Fore.RED + "This text is red!")
    print(Fore.YELLOW + "[ 1 ] Start Service")
    print(Fore.YELLOW + "[ 2 ] Stop Service")
    print(Fore.YELLOW + "[ 3 ] Restart Service")
    print(Fore.YELLOW + "[ 4 ] Back to Main Menu")
    print("----------------------------------------------------------------------------")
    choice = input("Your Choice? : ")
    return choice

# تابع اصلی برای مدیریت ناوبری بین منوها
def main():
    while True:
        choice = main_menu()
        if choice == "1":
            print("Network Scan selected.")
            time.sleep(2)
        elif choice == "2":
            print("IP Range Set selected.")

            time.sleep(2)
        elif choice == "3":
            while True:
                service_choice = services_menu()
                if service_choice == "4":
                    break
                elif service_choice == "1":
                    print("Start Service selected.")
                elif service_choice == "2":
                    print("Stop Service selected.")
                elif service_choice == "3":
                    print("Restart Service selected.")
                else:
                    print("Invalid option.")
                time.sleep(2)
        elif choice == "4":
            print("Pre Results selected.")
            time.sleep(2)
        else:
            print("Invalid option.")
            time.sleep(2)


if __name__ == "__main__":
    main()
