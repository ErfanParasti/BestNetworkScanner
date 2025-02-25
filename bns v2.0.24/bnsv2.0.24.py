import os
import time
import json
import ipaddress
import subprocess
from colorama import Fore, Style, init
import re

# Initialize colorama
init(autoreset=True)

def clear_screen():
    """Clear the terminal screen."""
    subprocess.call('cls' if os.name == 'nt' else 'clear', shell=True)

# تابع برای نمایش هدر برنامه
def display_header():
    clear_screen()
    print(Fore.GREEN + Style.BRIGHT + """
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
    \\:::\\:::\\   \\::::|  /:::/    |::|   /::\\____\\/::\\   \\:::\\   \\:::\\____\\    |     
     \\:::\\:::\\  /::::|_/:::/     |::|  /:::/    /\\:::\\   \\:::\\   \\::/    /    | 
      \\:::\\:::\\/:/    /\\::/     /|::| /:::/    /  \\:::\\   \\:::\\   \\/____/     | 
       \\::::::::/    /  \\/_____/ |::|/:::/    /    \\:::\\   \\::::\\    \\        | 
        \\::::::/    /            |::::::/    /      \\:::\\   \\:::\\_____\\       | 
         \\::::/    /             |:::::/    /        \\:::\\  /:::/    /        | 
          \\::/____/              |::::/    /          \\:::\\/:::/    /         | 
           \\/                    /:::/    /            \\::::::/    /          | 
                                 \::/    /              \\::::/    /           | 
                                  \/____/                \\/______/            |
______________________________________________________________________________|
                                                  __  __  _/_/_/_/_/_/_/_/_/_/
    Program   : Best_Network_Scanner   /::\\/::\\/:/ 
    Version   : 2.0.24                            \\::::::/:/
    Developer : Your Friend                       \\::::/:/
______________________________________________     \\::/:/
_/_/_/-----------------/_/_/_/_/_/_/_/_/_/_/_/______\\/_/
    """)
    print(Fore.YELLOW + "Best Network Scanner - BNS v1.0.0\n")

# تابع برای دریافت ورودی معتبر
def get_valid_input(prompt, valid_choices):
    while True:
        choice = input(Fore.YELLOW + prompt)
        if choice in valid_choices:
            return choice
        print(Fore.RED + "Invalid input! Please enter a valid choice.")

# تابع برای تنظیم محدوده IP
def set_ip_range():
    while True:
        display_header()
        ip_range = input(Fore.YELLOW + "Enter IP Range (e.g., 192.168.1.0/24): ")

        try:
            # بررسی معتبر بودن محدوده IP
            network = ipaddress.ip_network(ip_range, strict=False)
            save_json("range.json", {"range": ip_range})
            print(Fore.GREEN + f"IP Range {ip_range} saved successfully!")
            time.sleep(2)
            break
        except ValueError:
            print(Fore.RED + "Invalid IP Range! Try again...")
            time.sleep(2)


# تابع برای ذخیره اطلاعات در فایل JSON



def save_json(filename, data):
    try:
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(Fore.RED + f"Error saving data to {filename}: {e}")



# تابع برای اجرای اسکن شبکه با nmap


def network_scan():
    ip_range_data = read_json("range.json")
    if not ip_range_data:
        print(Fore.RED + "No IP range selected! Please set an IP range first.")
        time.sleep(2)
        set_ip_range()
        return

    ip_range = ip_range_data["range"]
    print(Fore.GREEN + f"Scanning network: {ip_range} ...")
    
    try:
        # اجرای دستور Nmap با دسترسی ریشه و استفاده از -sP برای کشف دستگاه‌ها
        result = subprocess.run(["sudo", "nmap", "-sP", ip_range], capture_output=True, text=True)
        scan_output = result.stdout

        # چاپ خروجی Nmap برای بررسی
        print(Fore.YELLOW + "Nmap Scan Output:")
        print(scan_output)  # چاپ خروجی Nmap برای بررسی

        # استخراج آی‌پی‌های زنده و مک‌آدرس از خروجی nmap
        alive_hosts = []
        id_counter = 1  # شمارش ID دستگاه‌ها
        current_ip = None
        current_mac = None
        
        # تحلیل خروجی
        for line in scan_output.split("\n"):
            if "Nmap scan report for" in line:
                current_ip = line.split()[-1]
            elif "MAC Address" in line:
                current_mac = line.split()[2]
                if current_ip and current_mac:
                    alive_hosts.append({"id": id_counter, "ip": current_ip, "mac": current_mac, "state": "up"})
                    id_counter += 1

        # بررسی آیا دستگاه‌های زنده پیدا شده‌اند یا خیر
        if alive_hosts:
            save_json("scan_results.json", alive_hosts)
            print(Fore.YELLOW + "Scan completed! Results saved in scan_results.json")
        else:
            print(Fore.RED + "No devices found during the scan.")

    except Exception as e:
        print(Fore.RED + f"Error running nmap: {e}")

    input(Fore.CYAN + "\nPress Enter to return...")
    clear_screen()

def read_json(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except Exception as e:
        print(Fore.RED + f"Error reading {filename}: {e}")
        return None

# Perform ping on a device
def ping_device(ip):
    print(Fore.CYAN + f"Pinging {ip}...")
    result = subprocess.run(["ping", "-c", "4", ip], capture_output=True, text=True)
    return result.stdout

# Perform tracert (traceroute) on a device
def tracert_device(ip):
    command = ["tracert", ip] if os.name == 'nt' else ["traceroute", ip]
    print(Fore.CYAN + f"Performing tracert for {ip}...")
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

# Service menu that doesn't trigger a new scan, uses previously scanned IPs
def services_menu():
    """ نمایش منوی سرویس‌ها برای تارگت‌های ذخیره‌شده """
    scan_data = read_json("targets.json")
    
    if not scan_data:
        print(Fore.RED + "No targets found!")
        return
    
    while True:
        print(Fore.CYAN + "\n[ 1 ] nmap services")
        print(Fore.CYAN + "[ 2 ] Ping all targets")
        print(Fore.CYAN + "[ 3 ] Tracert all targets")
        print(Fore.CYAN + "---------------------")
        print(Fore.CYAN + "[ 00 ]. Back")
        choice = input(Fore.YELLOW + "\nYour Choice? : ")

        if choice == "1":
            nmap_services(scan_data)
        elif choice == "2":
            results = ""
            for device in scan_data:
                ip = device.get("ip")
                ping_result = subprocess.run(["ping", "-c", "4", ip], capture_output=True, text=True)
                results += f"Ping results for {ip}:\n{ping_result.stdout}\n" + "-" * 50 + "\n"
            print(Fore.GREEN + results)

            if input(Fore.YELLOW + "Do you want to save the results? (y/n): ").lower() == "y":
                save_results(results)

        elif choice == "3":
            results = ""
            for device in scan_data:
                ip = device.get("ip")
                tracert_result = subprocess.run(["traceroute", ip], capture_output=True, text=True)
                results += f"Tracert results for {ip}:\n{tracert_result.stdout}\n" + "-" * 50 + "\n"
            print(Fore.GREEN + results)

            if input(Fore.YELLOW + "Do you want to save the results? (y/n): ").lower() == "y":
                save_results(results)

        elif choice == "00":
            return

        else:
            print(Fore.RED + "Invalid choice, please select again.")

# --------------------------------------------------------------------------------------------------------

def run_nmap_scan(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"Error during scan: {e}")
        return None


# -----------------------------------------------------------------------------------------------
def nmap_services(scan_data):
    final_results = {}

    for device in scan_data:
        ip = device.get("ip")
        if not ip:
            continue

        print(Fore.CYAN + f"\nStarting Nmap scans for IP: {ip}")

        # انتخاب نوع اسکن Nmap
        print(Fore.CYAN + "\n[ 1 ] OS Detection")
        print(Fore.CYAN + "[ 2 ] Service Version Detection")
        print(Fore.CYAN + "[ 3 ] Aggressive Scan")
        print(Fore.CYAN + "[ 4 ] Scan Specific Ports")
        print(Fore.CYAN + "[ 5 ] Nmap Scripting Engine")
        nmap_choice = input(Fore.YELLOW + "\nYour Nmap Choice? : ")

        result = {}

        if nmap_choice == "1":
            # OS Detection
            os_result = subprocess.run(["sudo", "nmap", "-O", ip], capture_output=True, text=True)
            result["OS details"] = os_result.stdout
            final_results[ip] = {"OS Detection": result}
        elif nmap_choice == "2":
            # Service Version Detection
            service_version_result = subprocess.run(["sudo", "nmap", "-sV", ip], capture_output=True, text=True)
            result["Service versions"] = parse_services(service_version_result.stdout)
            final_results[ip] = {"Service Version Detection": result}
        elif nmap_choice == "3":
            # Aggressive Scan
            aggressive_result = subprocess.run(["sudo", "nmap", "-A", ip], capture_output=True, text=True)
            result["Scan results"] = aggressive_result.stdout
            final_results[ip] = {"Aggressive Scan": result}
        elif nmap_choice == "4":
            # Scan Specific Ports
            ports = input(Fore.YELLOW + "Enter ports (comma separated): ")
            port_scan_result = subprocess.run(["sudo", "nmap", "-p", ports, ip], capture_output=True, text=True)
            result["Ports"] = parse_ports(port_scan_result.stdout)
            final_results[ip] = {"Port Scan": result}
        elif nmap_choice == "5":
            # Nmap Scripting Engine
            script_name = input(Fore.YELLOW + "Enter script name: ")
            nse_result = subprocess.run(["sudo", "nmap", "--script", script_name, ip], capture_output=True, text=True)
            result["Scripts"] = parse_nse(nse_result.stdout)
            final_results[ip] = {"NSE Result": result}
        else:
            print(Fore.RED + "Invalid choice!")

        # نمایش نتایج
        display_nmap_results(ip, list(final_results[ip].keys())[0], result)


# ---------------------------------------------------------------------------------------


# تابعی برای نمایش نتایج اسکن Nmap به شکل تفسیر شده و شکیل
def display_nmap_results(ip, scan_type, result):
    if scan_type == "OS Detection":
        print(Fore.CYAN + f"\n[OS Detection for {ip}]")
        if "OS details" in result:
            print(Fore.GREEN + result["OS details"])
        else:
            print(Fore.RED + "No OS details found.")

    elif scan_type == "Service Version Detection":
        print(Fore.CYAN + f"\n[Service Version Detection for {ip}]")
        if "Service versions" in result:
            for service, version in result["Service versions"].items():
                print(Fore.GREEN + f"Service: {service}, Version: {version}")
        else:
            print(Fore.RED + "No services detected.")
            
    elif scan_type == "Aggressive Scan":
        print(Fore.CYAN + f"\n[Aggressive Scan for {ip}]")
        if "Scan results" in result:
            print(Fore.GREEN + result["Scan results"])
        else:
            print(Fore.RED + "No aggressive scan results found.")
            
    elif scan_type == "Port Scan":
        print(Fore.CYAN + f"\n[Port Scan for {ip}]")
        if "Ports" in result:
            for port in result["Ports"]:
                print(Fore.GREEN + f"Port {port['port']} is {port['status']}")
        else:
            print(Fore.RED + "No open ports detected.")
            
    elif scan_type == "NSE Result":
        print(Fore.CYAN + f"\n[Nmap Scripting Engine Result for {ip}]")
        if "Scripts" in result:
            for script, output in result["Scripts"].items():
                print(Fore.GREEN + f"Script: {script}, Output: {output}")
        else:
            print(Fore.RED + "No NSE results found.")

# Save results to a specified file
def save_results(results):
    file_path = input(Fore.YELLOW + "Enter path to save results (e.g., /path/to/directory): ")
    if not os.path.exists(file_path):
        print(Fore.RED + "Invalid path entered!")
        return
    
    full_path = os.path.join(file_path, "results.txt")
    with open(full_path, "w") as file:
        file.write(results)
    print(Fore.GREEN + f"Results saved to {full_path}")

# تابع برای نمایش منوی اصلی
def main_menu():
    while True:
        display_header()
        print(Fore.CYAN + "[ 1 ] Network Scan")
        print(Fore.CYAN + "[ 2 ] Set IP Range")
        print(Fore.CYAN + "[ 3 ] Services")
        print(Fore.CYAN + "[ 4 ] Pre Results")
        print(Fore.CYAN + "[ 5 ] Target")
        print(Fore.CYAN + "[ 00 ] Exit")
        print("\n----------------------------------------------------------------------------")

        choice = get_valid_input("Your Choice? : ", ["1", "2", "3", "4", "5", "00"])

        if choice == "1":
            network_scan()
        elif choice == "2":
            set_ip_range()
        elif choice == "3":
            services_menu()
        elif choice == "4":
            show_scan_results()
        elif choice == "5":
            show_targets()
        elif choice == "00":
            # print(Fore.YELLOW + "Exiting...")
            print(Fore.RED + "\nExiting... Goodbye!")
            time.sleep(1)
            clear_screen()
            exit(0)  # خروج کامل از برنامه

# تابع برای نمایش نتایج اسکن‌شده (گزینه ۴)
def show_scan_results():
    """ نمایش نتایج اسکن شده از فایل scan_results.json """
    data = read_json("scan_results.json")
    if not data:
        print(Fore.RED + "No scan results found!")
        time.sleep(2)
        return

    print(Fore.YELLOW + "\nScan Results:")
    for entry in data:
        print(Fore.GREEN + f"ID: {entry['id']}, IP: {entry['ip']}, State: {entry['state']}")

    # انتخاب هدف برای ذخیره در فایل targets.json
    while True:
        choice = input(Fore.CYAN + "\nSelect target ID to save or enter 'all' to save all: ").strip().lower()
        if choice == "all":
            save_json("targets.json", data)
            print(Fore.GREEN + "All results saved as targets!")
            break
        elif choice.isdigit():
            target_id = int(choice)
            target_entry = next((x for x in data if x["id"] == target_id), None)
            if target_entry:
                save_json("targets.json", [target_entry])
                print(Fore.GREEN + f"Target {target_entry['ip']} saved!")
                break
            else:
                print(Fore.RED + "Invalid ID! Try again...")
        else:
            print(Fore.RED + "Invalid input!")

    input(Fore.CYAN + "\nPress Enter to return...")
    clear_screen()


# تابع برای نمایش اهداف ذخیره‌شده (گزینه ۵)
def show_targets():
    data = read_json("targets.json")
    if not data:
        print(Fore.RED + "No targets found!")
    else:
        print(Fore.YELLOW + "\nSaved Targets:")
        for entry in data:
            print(Fore.GREEN + f"Target IP: {entry['ip']}, State: {entry['state']}")
    input(Fore.CYAN + "\nPress Enter to return...")
    clear_screen()



# اجرای برنامه اصلی
if __name__ == "__main__":
    main_menu()
