#!/usr/bin/env python3

import os
import sys
import termcolor
colour = "green"
promt_colour = "green"

def help():
    termcolor.cprint("set interface -- sets the ap interface", "yellow")
    termcolor.cprint("set online interface -- sets the online interface for internet", "yellow")
    termcolor.cprint("set ssid -- sets the name of the ap", "yellow")
    termcolor.cprint("set channel --  sets the channel for the ap (1-14)", "yellow")
    termcolor.cprint("run -- runs the captive portal module with the config", "yellow")
    termcolor.cprint("help -- shows this message", "yellow")
    termcolor.cprint("back or exit -- exits the captive portal module", "yellow")

def main():
    interface = "wlan0"
    online_interface = "eth0"
    ssid = "Nightmare"
    channel = "1"
    promt = termcolor.colored("ghost@Nightmare:~", promt_colour)
    directory = termcolor.colored("/WiFi/rogue_ap/", "blue")
    not_root = termcolor.colored("$ ", colour)
    all_promt = promt + directory + not_root
    while True:
        #command = input(termcolor.colored("ghost@Nightmare:~/Wi-Fi/captive_portal/$ ", promt_colour)).split()
        command = input(all_promt).split()
        if command[0:2] == ['set', 'interface']:
            if len(command) == 3:
                interface = command[2]
        elif len(command) == 0:
            random = 2
        elif command[0:3] == ['set', 'online', 'interface']:
            if len(command) == 4:
                online_interface = command[3]
        elif command == ['run']:
            os.system("cd scripts/rogue && sudo bash Nightmare_ap " + interface + ' ' + online_interface + ' ' + ssid + ' ' + channel)
        elif command == ['exit'] or command == ['back']:
            sys.exit()
        elif command[0:2] == ['set', 'ssid']:
            if len(command) == 3:
                ssid = command[2]
        elif command[0:2] == ['set', 'channel']:
            if len(command) == 3:
                try:
                    channel = int(command[2])
                except:
                    termcolor.cprint(
                        "channel must be a number between 1-14", "red")
        elif command == ['show', 'config']:
            termcolor.cprint("interface=" + interface, colour)
            termcolor.cprint("online interface=" + online_interface, colour)
            termcolor.cprint("channel=" + channel, colour)
            termcolor.cprint("ssid=" + ssid, colour)
        elif command == ['help']:
            help()
        else:
            termcolor.cprint("Command Not Found", "red")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        termcolor.cprint("\nCtrl + C pressed............Quitting", "red")
        sys.exit()