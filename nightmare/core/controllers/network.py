#!/usr/bin/env python3

import termcolor
import os
import sys
from nightmare.core.config.settings import *
from nightmare.modules.network.mac_spoof import *



def help():
    termcolor.cprint("mac spoof -- spoofs the mac of specified network interface", colour)

def net_main():
    #os.system("cd scripts/")
    #intro()
    promt=termcolor.colored("ghost@Nightmare:~", promt_colour)
    directory=termcolor.colored("/Network/", "blue")
    not_root=termcolor.colored("$ ", promt_colour)
    all_promt=promt + directory + not_root
    while True:
        command = input(all_promt).split()

        
        if len(command) == 0:
            random = "3"
        elif command == ['clear']:
            os.system("clear")
        elif command == ['exit'] or command == ['back']:
            # sys.exit()
            break
        elif command == ['help']:
            help()
        elif command == ['mac', 'spoof']:
            mac_main()
        elif command[0] == ['sys']:
            command_temp=' '.join(command[1:])
            os.system(command_temp)
        else:
            termcolor.cprint("Command Not Found", "red")

if __name__ == "__main__":
    try:
        net_main()
        
    except KeyboardInterrupt:
        termcolor.cprint("\nCtrl + C pressed............Quitting", "red")
