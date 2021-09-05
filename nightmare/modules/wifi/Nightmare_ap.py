#!/usr/bin/env python3

import scapy
import os
import termcolor
import time
import sys
import logging as log
from nightmare.core.config import settings

#log_file = log_dir + "ap.log"

def splash():
    os.system("figlet Nightmare AP")
    print("*" * 66)


splash()