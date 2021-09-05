#!/usr/bin/env python3

from nightmare.core.config.settings import *
import os
import sys
import termcolor
from nightmare.modules.hash.md5_crack import md5_main
def help():
    termcolor.cprint("md5 -- cracks md5 with wordlist", colour)

def hash_main():
    promt = termcolor.colored("ghost@Nightmare:~", promt_colour)
    directory = termcolor.colored("/hash/", "blue")
    not_root = termcolor.colored("$ ", promt_colour)
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
        elif command == ['md5']:
            md5_main()
        elif command[0] == ['sys']:
            command_temp=' '.join(command[1:])
            os.system(command_temp)
        else:
            termcolor.cprint("Command Not Found", "red")
