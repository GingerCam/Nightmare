#!/usr/bin/env python

# imports required modules
import sys
import os
import termcolor
import subprocess
from tqdm import tqdm
import time

# NightMare vars
version = "v0.1"
date_release = "5/7/2021"
colour = "green"
promt_colour="green"
standardhandshake_filename = "handshake-01.cap"
standardpmkid_filename = "pmkid_hash.txt"
standardpmkidcap_filename = "pmkid.cap"
timeout_capture_handshake = "20"
timeout_capture_pmkid = "25"
tmpdir = "/tmp/"
osversionfile_dir = "/etc/"
# plugins_dir="plugins/"
minimum_bash_version_required = "4.2"
standard_resolution = "1024x768"
curl_404_error = "404: Not Found"
broadcast_mac = "FF:FF:FF:FF:FF:FF"
# Distro vars
arch_package = ['pacman', 'yum']
debian_package = ['apt', 'dpkg']
debian_based = ['kali', 'Parrot', 'Ubuntu', 'Debian', 'Mint']
arch_based = ['Arch', 'Manjaro']


# Distros vars
known_compatible_distros = (
    "Kali Parrot Ubuntu Mint Debian ").split()

known_arm_compatible_distros = ("raspbian Parrot Kali ").split()

# tool vars
ap_tools = (
    "hostapd dnsmasq ettercap bettercap tshark packetforge-ng ").split()

essential_tools_names = (
    "iw awk airmon-ng airodump-ng aircrack-ng xterm ip lspci ps figlet xterm ip grep awk cut hostapd dnsmasq tcpflow ").split()

web_tools = ("lighttpd ").split()

hash_tools = ("john hashcat ").split()

# checks if user is root 
if not os.getuid() == 0:
    print("Nightmare needs to run with root permissions!")
    sys.exit()


def intro():
    os.system(command="clear")
    print('')
    for i in tqdm (range (25), desc="Loading Your Nightmares..."):
        pass
        time.sleep(0.1)
    os.system(command="clear")
    os.system(command="figlet Nightmare")
    termcolor.cprint("Written by GingerCam. https://github.com/GingerCam/", "green")
    #termcolor.cprint("NightMare written by GingerCam", colour)
    time.sleep(0.1)
    termcolor.cprint(version, "red")
    time.sleep(0.1)
    termcolor.cprint(date_release, "red")
    time.sleep(0.1)
    print('')

#detects if you are on linux and what distro you are on
def os_detect():
    if sys.platform != "linux":
        print("At the moment linux is the only platform that Nightmare can run on")
        sys.exit
    os_file = osversionfile_dir + "os-release"
    supported_distros = known_arm_compatible_distros + known_compatible_distros
    os_test = open(os_file, "r")
    for line in os_test:
        line = line.rstrip()
        if line.startswith('ID='):
            os_name = line.replace('ID=', '')
    print("Operating System detected: " + os_name)
    print('')
    print('')

#simple yes no
def yesno():
    option = input(termcolor.colored("Y/n: ", colour))
    if len(option) == 0:
        answer = "y"
    elif len(option) == "1":
        if option == "y" or option == "Y":
            option = True
        elif option == "n" or option == "N":
            option = False
        else:
            print("Input must be either Y or N")
            yesno()

#checks if all requred packages are installed
def package_check():
    all_tools = ap_tools + web_tools + hash_tools + essential_tools_names
    not_installed = ""
    for package in all_tools:
        exist = subprocess.call('command -v ' + package + '>> /dev/null', shell=True)
        if exist != 0:
            not_installed = not_installed + '' + package
    if len(not_installed) != 0:
        termcolor.cprint("Some packages are not installed!", "red")
        termcolor.cprint("Would you like to install these packages?", "red")
        option=input("Y/n: ")
        if option == "y" or option == "Y":
            os.system(command="apt install " + not_installed)


def clear_temp():
    try:
        tmp_files=("hostapd.conf dnsmasq.conf").split()
        for file in tmp_files:
            os.remove(tmpdir + file)
    except:
        print("No temp files to be removed")

def help():
    termcolor.cprint("sys (command) -- executes system commands", colour)
    termcolor.cprint("ap -- puts Nightmare into access point mode", colour)
    termcolor.cprint("netscan -- scans a selected subnet for avaliable hosts", colour)
    termcolor.cprint("clear -- clears the screen", colour)

#cli
def cli():
    while True:
        command = input(termcolor.colored(
            "ghost@Nightmare:~$ ", promt_colour)).split()
        if len(command) == 0:
            random="4"
        elif command == ['exit']:
            print("Aborting!")
            print("Cleaning temp files")
            clear_temp()
            sys.exit()
        elif command == ['clear']:
            os.system(command="clear")
        elif command[0] == "sys":
            command_temp=' '.join(command[1:])
            os.system(command_temp)
        elif command == ['ap']:
            os.system("sudo python3 scripts/ap.py")
        elif command == ['netscan']:
            os.system("sudo python3 scripts/network_scanner.py")
        elif command == ['help']:
            help()
        else:
            termcolor.cprint("Command Not Found")


def main():
    try:
        intro()
        os_detect()
        package_check()
        cli()
    except KeyboardInterrupt:
        termcolor.cprint("\nCtrl + C pressed............Quitting", "red")
        clear_temp()
        sys.exit()


if __name__ == '__main__':
    main()
