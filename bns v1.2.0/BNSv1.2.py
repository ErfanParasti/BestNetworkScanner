import os
import time
import json
from colorama import Fore, Style, init
import ipaddress

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
                                                  _   _  /_/_/_/_/_/_/_/_/_/_/
    Program   : Best_Network_Scanner   /-\\:/-\\/:/ 
    Version   : 1.2.0                            \\:::::/:/
    Developer : Your Friend                       \\:::/:/
_____________________________________________      \\:/:/
__/_/-----------------/_/_/_/_/_/_/_/_/_/_/_|_______/_/
    """
    # print(Fore.GREEN + Style.BRIGHT + logo)  # لوگو با رنگ سبز روشن

# Display header with logo
    print(Fore.GREEN + Style.BRIGHT + logo)

# Main menu
def main_menu():
    display_header()
    print(Fore.CYAN + "[ 1 ] Network Scan")
    print(Fore.CYAN + "[ 2 ] IP Range Set (Default: 192.168.0.0 - 192.168.0.255)")
    print(Fore.CYAN + "[ 3 ] Services")
    print(Fore.CYAN + "[ 4 ] Pre Results")
    print(Fore.CYAN + "[ 5 ] Target")
    print(Fore.CYAN + "[ 00 ] Exit")
    print("\n----------------------------------------------------------------------------")
    choice = input(Fore.YELLOW + Style.BRIGHT + "Your Choice? : ")
    return choice

# Check if IP is private
def is_private_ip(ip):
    try:
        addr = ipaddress.IPv4Address(ip)
        return addr.is_private
    except ValueError:
        return False

# Network scan function
def network_scan(start_ip, end_ip):
    scan_results = []
    start = int(ipaddress.IPv4Address(start_ip))
    end = int(ipaddress.IPv4Address(end_ip))
    ip_id = 0
    for ip_int in range(start, end + 1):
        ip = str(ipaddress.IPv4Address(ip_int))
        response = os.system(f"ping -c 1 -w 1 {ip} > /dev/null 2>&1")
        if response == 0:
            ip_id = ip_id + 1
            print(Fore.GREEN + f"[{ip_id}] - Found: {ip}")
            scan_results.append({"id": len(scan_results) + 1, "ip": ip, "state": "up"})
    return scan_results

# Save results to a JSON file
def save_results_to_file(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

# Select target from scan results
def select_target(scan_results):
    print(Fore.CYAN + "Available IPs:")
    for result in scan_results:
        print(Fore.YELLOW + f"[{result['id']}] {result['ip']} - State: {result['state']}")
    choice = input(Fore.YELLOW + "Select an ID: ")
    for result in scan_results:
        if str(result["id"]) == choice:
            return result
    return None
def read_file_json(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        print(Fore.RED + f"Error: Cannot read {filename}!")
        return []


# Main program function
def main():
    default_start_ip = "192.168.0.0"
    default_end_ip = "192.168.0.255"

    while True:
        choice = main_menu()
        if choice == "1": #======================choois-1=====================================================
            start_ip = input(f"Enter start IP (default: {default_start_ip}): ") or default_start_ip
            end_ip = input(f"Enter end IP (default: {default_end_ip}): ") or default_end_ip
            
            if not (is_private_ip(start_ip) and is_private_ip(end_ip)):
                print(Fore.RED + "Error: Only private IP ranges are allowed!")
                time.sleep(2)
                continue

            print(Fore.YELLOW + "Starting network scan...")
            scan_results = network_scan(start_ip, end_ip)
            save_results_to_file("scan_results.json", scan_results)
            print(Fore.GREEN + "Scan results saved to 'scan_results.json'")
            clear_screen()
            display_header()
            target = select_target(scan_results)
            if target:
                print(Fore.GREEN + f"Target selected: {target['ip']}")
                save_results_to_file("target.json", [target])
                print(Fore.GREEN + "Target saved to 'target.json'")
            else:
                print(Fore.RED + "Invalid target ID!")
        elif choice == "2": #======================choois-2=====================================================
            print(Fore.GREEN + "IP Range Set selected. Adjust IPs in the code if needed.")
            time.sleep(2)
        elif choice == "3":#======================choois-3=====================================================
            print(Fore.GREEN + "Services selected.")
            time.sleep(2)
        elif choice == "4":#======================choois-4=====================================================
            print(Fore.GREEN + "Pre Results selected.")
            data = read_file_json("scan_results.json")
            results = []
             # بررسی اینکه داده‌ها لیست هستند
            if isinstance(data, list):
                # پردازش داده‌ها و ذخیره id, ip, state
                for entry in data:
                    id = entry.get("id")
                    ip = entry.get("ip")
                    state = entry.get("state")
                    results.append(f"ID: {id}, IP: {ip}, State: {state}")
            else:
                print("داده‌های فایل JSON لیست نیستند. لطفاً فایل را بررسی کنید.")
                return
        
            # # نمایش همه نتایج
            # print(Fore.YELLOW + Style.BRIGHT + "\nresult:")
            # for result in results:
            #     print(Fore.GREEN + result)

            target = select_target(data)
            if target:
                print(Fore.GREEN + f"Target selected: {target['ip']}")
                save_results_to_file("target.json", [target])
                print(Fore.GREEN + "Target saved to 'target.json'")
            else:
                print(Fore.RED + "Invalid target ID!")
            print("-------------------------------------------")
            time.sleep(1)
            input()
            clear_screen()
            main_menu()
            
        elif choice == "5":#======================choois-5=====================================================
           data = read_file_json("target.json")
           results = []
            # بررسی اینکه داده‌ها لیست هستند
           if isinstance(data, list):
               # پردازش داده‌ها و ذخیره id, ip, state
            for entry in data:
                id = entry.get("id")
                ip = entry.get("ip")
                state = entry.get("state")
                results.append(f"ID: {id}, IP: {ip}, State: {state}")
           else:
               print("داده‌های فایل JSON لیست نیستند. لطفاً فایل را بررسی کنید.")
               return
           for result in results:
               print(Fore.YELLOW + Style.BRIGHT + "\n Target : " + Fore.GREEN + result)
            #    print(Fore.GREEN + result)
                   # نمایش همه نتایج
           time.sleep(1)
           input()
           clear_screen()
           main_menu()

        elif choice == "00":#======================choois-00====================================================
            print(Fore.RED + "\nExiting... Goodbye!")
            time.sleep(1)
            clear_screen()
            exit(0)  # خروج کامل از برنامه

        else:#=====================-else ======================================================
            print(Fore.RED + "Invalid option in Main Menu!")
            time.sleep(1)

if __name__ == "__main__":
    main()
