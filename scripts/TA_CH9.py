#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 12:37:07 2022

@author: dgaio
"""

# Creating lists 
s = 'abcdefghijk'
lnew = []   #1: define an empty list
for i in range(0, len(s), 4):
    lnew.append(s[i:i+2])
    #lnew.append(s[i]+s[i+1])
print(lnew)


# Creating strings
s = 'abcdefghijk'
snew = ''   #1: define an empty string
for i in range(0, len(s), 4):    
    snew=snew+s[i:i+2]
print(snew)


# Creating dictionaries
s = 'abcdefghijk'
dnew = {}   #1: define an empty dictionary
for i in range(0, len(s), 4):
    dnew[s[i:i+2]]=s[i+2:i+4] 
print(dnew)




# Creating arrays

import numpy as np
anew =    #1: create array with zeros
for i in range(len(anew)):
    anew[...] = i + 1   #2: define non-zero values by replacing the points by code.