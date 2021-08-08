#!/bin/bash

if [[ $1 == "install" ]]; then
    apt install python3 python3-pip net-tools hostapd dnsmasq ettercap-text-only bettercap tshark iw aircrack-ng xterm figlet xterm grep tcpflow john hashcat
    pip3 install -r requirements.txt
    if [[ $2 == "global" ]]; then
        mkdir /usr/share/Nightmare
        cp -r /usr/share/Nightmare
        cp /usr/share/Nightmare/scripts/nightmare /usr/bin/
        chmod +x /usr/bin/nightmare
    fi
fi

if [[ $1 == "uninstall" ]]; then
    if [[ -d /usr/share/Nightmare ]]; then
        rm -r /usr/share/Nightmare
        rm /usr/bin/Nightmare        
    fi
fi
