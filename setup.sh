#!/bin/bash

# تعیین رنگ‌ها برای خروجی زیباتر
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # بدون رنگ

echo -e "${GREEN}[*] در حال تشخیص توزیع لینوکس...${NC}"

# تشخیص توزیع لینوکس
if [ -f /etc/os-release ]; then
    . /etc/os-release
    OS=$ID
else
    echo -e "${RED}[!] نامشخص! این اسکریپت فقط روی لینوکس و ترموکس کار می‌کند.${NC}"
    exit 1
fi

# نصب وابستگی‌های اصلی
install_dependencies() {
    echo -e "${YELLOW}[*] در حال نصب پیش‌نیازها...${NC}"
    sudo $1 update -y
    sudo $1 install -y python3 python3-pip nmap
}

# نصب روی کالی و دبیان/اوبونتو
if [[ "$OS" == "kali" || "$OS" == "debian" || "$OS" == "ubuntu" ]]; then
    install_dependencies "apt"

# نصب روی Arch Linux
elif [[ "$OS" == "arch" ]]; then
    install_dependencies "pacman"

# نصب روی Termux (اندروید)
elif [[ "$OS" == "android" ]]; then
    echo -e "${YELLOW}[*] در حال نصب پکیج‌ها در ترموکس...${NC}"
    pkg update -y && pkg upgrade -y
    pkg install -y python pip nmap
else
    echo -e "${RED}[!] توزیع شما پشتیبانی نمی‌شود!${NC}"
    exit 1
fi

# نصب پکیج‌های پایتونی
if [ -f "requirements.txt" ]; then
    echo -e "${GREEN}[*] در حال نصب پکیج‌های Python...${NC}"
    pip3 install --upgrade pip
    pip3 install -r requirements.txt
else
    echo -e "${RED}[!] فایل requirements.txt پیدا نشد!${NC}"
    exit 1
fi

echo -e "${GREEN}[✔] نصب کامل شد! حالا می‌تونید برنامه رو اجرا کنید.${NC}"

