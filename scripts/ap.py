#!/usr/bin/env python3

import termcolor
import os
import sys
from config.Nightmare.settings import colour, promt_colour

def abs_file():
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

config_files = {'/tmp/hostapd.conf', '/tmp/dnsmasq.conf'}
tmpdir = "/tmp/"

def clear_temp():
    try:
        tmp_files = ("hostapd.conf dnsmasq.conf").split()
        for file in tmp_files:
            os.remove(tmpdir + file)
    except:
       random=4

def help():
    termcolor.cprint("captive portal -- captive portal attack for evil twin and/or phishing", colour)
    termcolor.cprint("http sniffer -- sniffs http connections from ap", colour)
    termcolor.cprint("rogue ap -- creates a base rogue access point", colour)

def ap_main():
    #os.system("cd scripts/")
    #intro()
    promt=termcolor.colored("ghost@Nightmare:~", promt_colour)
    directory=termcolor.colored("/WiFi/", "blue")
    not_root=termcolor.colored("$ ", promt_colour)
    abs_file()
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
            os.system("sudo python3 portal/portal.py")
        elif command == ['rogue', 'ap']:
            os.system("sudo python3 rogue/rogue.py")
        elif command == ['http', 'sniffer']:
            os.system("sudo python3 http_sniff/sniffer.py")
        elif command[0] == ['sys']:
            command_temp=' '.join(command[1:])
            os.system(command_temp)
        else:
            termcolor.cprint("Command Not Found", "red")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        termcolor.cprint("\nCtrl + C pressed............Quitting", "red")
        sys.exit()