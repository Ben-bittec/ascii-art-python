#!/usr/bin/env python
# coding: utf-8

#written by s1ck0

import pyfiglet

name=input("Enter A Text: ")
name=str(name)
while True:
    try:
        style=input("Enter Style: ")
        style=str(style)
        word=pyfiglet.figlet_format(name,font=style)
        print(word)
    except Exception as e:
    	print("Wrong Font Style")
    	style=input("Enter Style: ")
    	style=str(style)
    	word=pyfiglet.figlet_format(name,font=style)
    	print(word)
