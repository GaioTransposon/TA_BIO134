#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 19:57:46 2022

@author: dgaio
"""


import matplotlib.pyplot as plt



# Exercise: 
# Enter the numbers of foxes and rabbits respectively after 200 days, 
# if there are 100 foxes and 1000 rabbits present in the beginning. 
# Your program should work with float without rounding, except for the final answer, 
# which is to be rounded down to an integer (manually).
f=100
r=1000

time=[]
rabbit_pop=[]
fox_pop=[]
for d in range(1*24, 201*24, 1):
    
    r_growth=((0.05*r)-0.0002*f*r)/24   # just read the text carefully: decrease vs increase
    f_growth=((-0.1*f)+0.0001*f*r)/24   # just read the text carefully: decrease vs increase
    
    r=r+r_growth
    f=f+f_growth
    print(d, end =" ")
    print(r, end=" ")
    print(f)
    
    time.append(d)
    rabbit_pop.append(r)
    fox_pop.append(f)
    
time
rabbit_pop
max(fox_pop)

plt.figure()
plt.plot(time,rabbit_pop,'.')
plt.plot(time,fox_pop,'.')


    
    