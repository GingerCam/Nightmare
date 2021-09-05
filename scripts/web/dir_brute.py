#!/usr/bin/env python3

'''
usage :-
python <url> <wordlist> <extension>
for example :
python http://www.google.com/ common.txt .php
it supports all extensions & wordlists. 
if you just want subdirectories write "/" in place of extension it will find it for you.
'''
import requests
import sys
from termcolor import colored

url = input(colored("Input url: ", "yellow"))
wordlist = input(colored("Input wordlist: ", "yellow"))
ext = input(colored("Input extension: ", "yellow"))
if url == '':
    print("url has to have a value")
    sys.exit()
if wordlist == '':
    print("wordlist must have a value")
if ext == '':
    print("No extension provided. default = / for subdirectories")
    ext = "/"

def write(word):
	f1 = open("write1.txt","a")
	f1.write(word +"\n")
	
fo = open(wordlist,"r+")
for i in range(2000):
	word = fo.readline(10).strip()
	surl = url+word+ext
	#print (surl)
	
	response = requests.get(surl)
	#print (response)
	if (response.status_code == 200):
		print ("[+] found :- ",surl)
		write(word)
	else:	
		print ("[-] Not found :- ",surl)
		pass