#!/usr/bin/env/python3

import sys
import termcolor
import os

colour = "yellow"
promt_colour = "green"

def help():
    termcolor.cprint("dir brute -- brute forces a directory tree on a server with file", colour)
    termcolor.cprint("help -- prints this message", colour)
    termcolor.cprint("exit or back -- exits this module", colour)

def main():
    
    promt=termcolor.colored("ghost@Nightmare:~", promt_colour)
    directory=termcolor.colored("/web/", "blue")
    not_root=termcolor.colored("$ ", promt_colour)
    all_promt=promt + directory + not_root

    while True:
        command = input(termcolor.colored(all_promt, promt_colour)).split()

        if command == ['help']:
            help()
        elif command == ['exit'] or command == ['back']:
            sys.exit()
        elif command == ['dir', 'brute']:
            os.system("sudo python3 scripts/web/dir_brute.py")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        termcolor.cprint("Ctrl + C caught.........aborting", colour)
        sys.exit()
        