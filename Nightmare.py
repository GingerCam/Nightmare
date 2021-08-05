#!/usr/bin/env python

# imports required modules
import sys
import argparse
import os
from bs4 import BeautifulSoup
import requests
from termcolor import colored
import termcolor
import subprocess

# NightMare vars
version = "v0.1"
date_release = "5/8/2021"
color = "green"
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
command=None

# Distro vars
arch_package=['pacman', 'yum']
debian_package=['apt', 'dpkg']
debian_based=['kali', 'Parrot', 'Ubuntu', 'Debian', 'Mint']
arch_based=['Arch', 'Manjaro']


# Distros vars
known_compatible_distros = (
    "Kali Parrot Ubuntu Mint Debian Arch Manjaro ").split()

known_arm_compatible_distros = ("raspbian Parrot Kali ").split()

# tool vars
ap_tools = (
    "hostapd dnsmasq ettercap bettercap dhcpcd tshark packetforge-ng ").split()

essential_tools_names = (
    "iw awk airmon-ng airodump-ng aircrack-ng xterm ip lspci ps figlet ").split()

web_tools = ("lighttpd ").split()

hash_tools = ("john hashcat ").split()

if not os.getuid() == 0:
    print("Nightmare needs to run with root permissions!")
    sys.exit()

# create parser
parser = argparse.ArgumentParser()

# add arguments
parser.add_argument(
    "-i",
    "--iface",
    dest="interface",
    help="Wireless interface to run the access point",
    default=None,
)
args = parser.parse_args


def intro():
    os.system(command="clear")
    print("NightMare written by GingerCam")
    print(version)
    print(date_release)

def os_detect():
    if sys.platform is not "linux":
        print("At the moment linux is the only platform that Nightmare can run on")
        sys.exit
    os_file = osversionfile_dir + "os-release"
    supported_distros = known_arm_compatible_distros + known_compatible_distros
    for os in supported_distros:
        os_test = os.system(command="grep " + os + '' + os_file)
        if os_test != '':
            os_name = os
    if os_name in supported_distros:
        print("Operating System detected: " + os)
        if os_name in debian_based:
            package_manager=debian_package
    else:
        print("Operating System: unknown")
        print("Your OS could not be detected!")
        print("These OS are supported: " + supported_distros)


def yesno(Y):
    option = input(termcolor.colored("Y/n", color))
    if len(option) == 0:
        answer = "y"
    elif len(option) == "1":
        if option == "y" or option == "Y":
            option = True
        elif option == "n" or option == "N":
            option = False
        else:
            print("Input must be either Y or N")
            yesno("Y")


def yesno(N):
    option = input(termcolor.colored("y/N", color))
    if len(option) == 0:
        answer = "n"
    elif len(option) == "1":
        if option == "y" or option == "Y":
            option = True
        elif option == "n" or option == "N":
            option = False
        else:
            print("Input must be either Y or N")
            yesno("N")


def package_check():
    all_tools = ap_tools + web_tools + hash_tools + essential_tools_names
    not_installed = []
    for package in all_tools:
        exist = subprocess.call(
            'command -v ' + package + '>> /dev/null', shell=True)
        if exist != 0:
            not_installed.append(package)
    if len(not_installed) != 0:
        termcolor.cprint("Some packages are not installed!", "red")
        termcolor.cprint("Would you like to install these packages?", "red")
        option = None
        yesno("Y")
        if option == True:
            os.system(command=debian_package[0] + ' ' + not_installed)

def cli_cmds(command):
    if len(command) >= "1":
        if command == "ap":
            mode="ap"
            ap_menu()            
            cli()            



def cli():
    try:
        command = input(termcolor.colored("ghost@Nightmare:~" + mode + "$ ", color))
        cli_cmds(command)
    except:
        command = input(termcolor.colored("ghost@Nightmare:~$ ", color))
        cli_cmds(command)

def ap_menu():
    interface="wlan0"
    ssid="NightMare"
    channel="11"
    bssid="BC:F6:85:03:36:5B"
    contents=['access point', 'show config', 'set']
    





def main():
    intro()
    os_detect()
    package_check()
    cli()
