#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 12:37:07 2022

@author: dgaio
"""


import os
home=os.getenv("HOME")


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
#print(l[:,1])
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
#l[0] /= 0
#print(l)      # ZeroDivisionError: division by zero

d = {'a': 1, 'b': 2}
#d['a'] /= 0
#print(d)      # ZeroDivisionError: division by zero

a = np.array([3, 6, 0])
#a = a /0
#print(a)      # [inf inf inf]

#####
# Regeneration exercise: lists 1 (2)
def file_to_list(some_file):
    opened_file = open(some_file)
    lines = opened_file.readlines()
    opened_file.close()
    my_list=[]
    for line in lines:
        sublist = line.split()
        sublist[0]=int(sublist[0])
        sublist[2]=float(sublist[2])
        my_list.append(sublist)
    return my_list


my_path_to_file=home+'/github/TA_BIO134/source_data/bif_after.txt'
l_after=file_to_list(my_path_to_file)
print(l_after[36])
#####

#####
# Regeneration exercise: lists 2 (2)
my_path_to_file=home+'/github/TA_BIO134/source_data/bif_before.txt'
l_before=file_to_list(my_path_to_file)

for b in l_before:
    if b[0]==5 and b[1]=='V3':
        bef=b[2]
for a in l_after:
    if a[0]==5 and a[1]=='V3':
        aft=a[2]
print(aft/bef)

#####
# Regeneration exercise: dictionaries 1 (2)
def list_to_dict(some_list):
    my_dict={}
    for line in some_list:
        fish=line[0]
        fin=line[1]
        bif=line[2]
        
        if fin not in my_dict:
            my_dict[fin] = {}
        my_dict[fin][fish]=bif
        
    return my_dict

d_before = list_to_dict(l_before)
print(d_before['V9'])

#####
# Regeneration exercise: dictionaries 2 (2)
d_after = list_to_dict(l_after)
    
ratio=d_after['V3'][5]/d_before['V3'][5]
#####  

#####
# Arrays
# Regeneration exercise: arrays 1 (2)
 
def ray_dictionary():
   rays = {}
   for i in range(9): 
      s = 'D' + str(i+1)
      print(s)
      rays[s] = i 
   for i in range(9):
      s = 'V' + str(9-i)
      print(s)
      rays[s] = i + 9 
   return rays
   
rays = ray_dictionary()
print(rays)

def list_to_array(some_list, no_fish, rays):
    a = np.zeros(shape = [len(rays), no_fish]) + np.NaN
    print(a)
    for sublist in some_list:
        fish = sublist[0]
        ray = sublist[1]
        bif = sublist[2]
        a[rays[ray], fish-1] = bif
    return a

rays = ray_dictionary()
no_fish = 7
a_before = list_to_array(l_before, no_fish, rays)
print('a_before[4,:]',a_before[4,:])
print('a_before[:,4]',a_before[:,4])
#####

#####
# Regeneration exercise: arrays 2 (2)
# Calculate the ratio for ray V3 in fish 5.
a_after = list_to_array(l_after, no_fish, rays)
print(a_after)

ratio = a_after[rays['V3'], 5-1] / a_before[rays['V3'], 5-1]
print ('ratio V3, fish5, calculated with arrays:', ratio)

##### 
# Calculations and plotting
# Bifurcation ratios for one fish


  
    
  
    
  
    
  
    