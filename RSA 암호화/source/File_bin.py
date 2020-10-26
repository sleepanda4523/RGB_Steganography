# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 13:06:50 2020

@author: msi
"""
import binascii

f = open("testjpg.jpg","rb+")
fw = open("binary.txt","w")
string = ""
line = f.read()
#print(line)
string+=str(binascii.b2a_hex(line))
string = string.replace("'", "")
string = string[1:]
print(string)
fw.write(string)
f.close()
fw.close()

