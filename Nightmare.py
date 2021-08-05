#!/usr/bin/env python

# imports required modules
import sys
import argparse

# Distros vars
known_compatible_distros = (
    "Wifislax Kali Parrot Backbox BlackArch Cyborg Ubuntu Mint Debian SuSE CentOS Gentoo Fedora Red Hat Arch OpenMandriva Pentoo Manjaro").split()

known_arm_compatible_distros = ("raspbian Parrot Kali").split()

ap_tools = (
    "hostapd dnsmasq ettercap bettercap dhcpcd tshark packetforge-ng").split()

essential_tools_names = (
    "iw awk airmon-ng airodump-ng aircrack-ng xterm ip lspci ps").split()

web_tools = ("lighttpd").split()

hash_tools = ("john hashcat").split()

def main():
    # create parser
    parser = argparse.ArgumentParser()
    