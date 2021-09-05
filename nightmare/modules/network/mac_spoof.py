import random, os, subprocess, termcolor
from nightmare.core.config.settings import colour

def get_rand():
    return random.choice("abcdef0123456789")

def new_mac():
    mac = ""
    for i in range(0,6):
        rand = f"{get_rand()}{get_rand()}"
        if not i == 5:
            mac += f"{rand}:"
        else:
            mac += f"{rand}"
    return mac

def mac_main():
    interface = input(termcolor.colored("Enter Interface: ", colour))
    # print(os.system("ifconfig eth0 | grep ether | grep -oE [0-9abcdef:]{17}"))

    # subprocess.call(["sudo", "ifconfig", "eth0", "down"])
    
    # new_address = new_mac()
    # subprocess.call(["sudo", "ifconfig", "eth0", "hw", "ether", "%s"%new_address])
    
    # subprocess.call(["sudo", "ifconfig", "eth0", "up"])
    
    # # New MAC address
    # print(os.system("ifconfig eth0 | grep ether | grep -oE [0-9abcdef:]{17}"))

    print(os.system("ifconfig " + interface + " | grep ether | grep -oE [0-9abcdef:]{17}"))

    # subprocess.call(["sudo", "ifconfig", interface, "down"])
    os.system("sudo ifconfig " + interface + " down")
    new_address = new_mac()
    # subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", "%s"%new_address])
    os.system("sudo ifconfig " + interface + " hw ether " + new_address)
    # subprocess.call(["sudo", "ifconfig", interface, "up"])
    os.system("sudo ifconfig " + interface + " up")
    # New MAC address
    print(os.system("ifconfig " + interface + " | grep ether | grep -oE [0-9abcdef:]{17}"))
    
    
