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
anew = np.zeros(shape=(3,4))
print(anew)
for i in range(len(anew)):    
    anew[i,i+1] = i + 1  
print(anew)
    
# Slicing 1 (5)
import numpy as np
a = np.array([[0, 1, 0, 0], [5, 0, 0, 0], [0, 0, 3, 0]])
print(a[:,1])
# [1 0 0]

# Slicing 2 (5)
import numpy as np
a = np.array([[0, 1, 0, 0], [5, 0, 0, 0], [0, 0, 3, 0]])
#print(a[:][1]])
# gives error

# Slicing 3 (5)
import numpy as np
a = np.array([[0, 1, 0, 0], [5, 0, 0, 0], [0, 0, 3, 0]])
print(a[:][1])
# [5 0 0 0]

# Slicing 4 (5)
l = [[0, 1, 0, 0], [5, 0, 0, 0], [0, 0, 3, 0]]
print(l[:][1])
# [5, 0, 0, 0]

# Slicing 5 (5)
l = [[0, 1, 0, 0], [5, 0, 0, 0], [0, 0, 3, 0]]
print(l[:,1])
# gives error (can't access this list like it's an array)

# Accessing a specific element
v = {'a': {'b': 5, 
           'd': 8, 
           'e': 3}, 
     'f': {'g': 5, 
           'h': [3, 
                 4, 
                 ['z', 2]
                 ], 
           'c': 3}}   
# obtain the following: 
# {'a': {'b': 5, 'd': 8, 'e': 3}, 'f': {'g': 5, 'h': [3, 4, ['z', 5]], 'c': 3}}
v['f']['h'][2][1]=5
print(v)

# Integers and floats in arrays
import numpy as np
a = np.array([3, 6, 0])
a[0] = a[0] + 0.6       # 3  6  0     didn't change because array of integers so it rounds up
a = a / 3               # 1.  2.  0.  because division makes floats
a[2] += 2.2             # 1.  2.0   2.2
a = a / 2               # 0.5  1.0   1.1
print(a)

# Dividing by zero
l = [ 3, 5, 7]
l[0] /= 0
print(l)      # ZeroDivisionError: division by zero

d = {'a': 1, 'b': 2}
d['a'] /= 0
print(d)      # ZeroDivisionError: division by zero

a = np.array([3, 6, 0])
a = a /0
print(a)      # [inf inf inf]
















    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    