#!/usr/bin/env python3

import termcolor
import scapy
import os
import sys
import time
from tqdm import tqdm

colour = "green"
promt_colour="green"
status="idle"

channel_range = range(1, 15)
config_files = {'/tmp/hostapd.conf', '/tmp/dnsmasq.conf'}
tmpdir = "/tmp/"
version = "v0.1"
date_release = "6/7/2021"


def intro():
    os.system(command="clear")
    os.system(command="figlet Nightmare")
    termcolor.cprint(
        "Written by GingerCam. https://github.com/GingerCam/", "green")
    #termcolor.cprint("NightMare written by GingerCam", colour)
    time.sleep(0.1)
    termcolor.cprint(version, "red")
    time.sleep(0.1)
    termcolor.cprint(date_release, "red")
    termcolor.cprint("mode=access point", colour)
    time.sleep(0.1)
    print('')

def clear_temp():
    try:
        tmp_files = ("hostapd.conf dnsmasq.conf").split()
        for file in tmp_files:
            os.remove(tmpdir + file)
    except:
       random=4

def help():
    termcolor.cprint("captive portal -- captive portal attack for evil twin and/or phishing", colour)
    #termcolor.cprint("http sniffing", colour)


def main():
    os.system("cd scripts/")
    #intro()
    promt=termcolor.colored("ghost@Nightmare:~", promt_colour)
    directory=termcolor.colored("/WiFi/", "blue")
    not_root=termcolor.colored("$ ", colour)
    all_promt=promt + directory + not_root
    while True:
        command = input(all_promt).split()

        
        if len(command) == 0:
            random = "3"
        elif command == ['clear']:
            os.system("clear")
        elif command == ['exit'] or command == ['back']:
            clear_temp()
            sys.exit()
        elif command == ['help']:
            help()
        elif command == ['captive', 'portal']:
            os.system("sudo python3 scripts/portal/portal.py")
        else:
            termcolor.cprint("Command Not Found", "red")


if __name__ == "__main__":
    main()