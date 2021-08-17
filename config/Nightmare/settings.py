#!/usr/bin/env python3

import sys
import configparser
import os

def abs_file():
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

abs_file()
config_file = "settings.txt"
config = configparser.ConfigParser()
config.read_file(open(config_file))


colour = config.get('colours', 'colour')
promt_colour = config.get('colours', 'promt_colour')
version = config.get('version', 'version')
date_release = config.get('version', 'date_release')