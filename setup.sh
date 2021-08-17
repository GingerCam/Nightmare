#!/bin/bash

if [[ $EUID -ne 0 ]]; then
    echo "This script must be run as root"
    echo "Exit"
    exit 1
fi


if [[ $1 == "install" ]]; then
    apt update
    apt install python3 python3-pip net-tools hostapd dnsmasq ettercap-text-only bettercap tshark iw aircrack-ng xterm figlet xterm grep tcpflow john hashcat
    pip3 install -r requirements.txt
    if [[ $2 == "global" ]]; then
        mkdir /usr/share/Nightmare
        cp -r  config pictures scripts sysfiles Nightmare.py setup.sh README.md requirements.txt /usr/share/Nightmare/
        cp /usr/share/Nightmare/sysfiles/nightmare /usr/bin/
        chmod +x /usr/bin/nightmare
        cp /usr/share/Nightmare/sysfiles/Nightmare.desktop /usr/share/applications/
    fi
fi

if [[ $1 == "uninstall" ]]; then
    if [[ -d /usr/share/Nightmare ]]; then
        rm -r /usr/share/Nightmare
        rm /usr/bin/nightmare
        rm /usr/share/applications/Nightmare.desktop
    else
        echo "Nightmare is not installed"        
    fi
fi
