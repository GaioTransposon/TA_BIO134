#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 14:28:52 2022

@author: dgaio
"""




# for-loops: 

# Questions: in range()

# =============================================================================
# # Question 4(5)
# j=0
# for i in range(1,2,2):
#     print ('hello')
# print (i)
# # hello printed 3 times
# # values taken by i: 1, 3, 5
# =============================================================================

# =============================================================================
# # Question 5(5)
# j=0
# for i in range(8,0,-2):
#     print (i)
# # it's exactly the same as having: 
# for i in range(0,8,2):
#     print (i)
# # but inverted order 
# =============================================================================

# Exercises: loop and print

# =============================================================================
# # Exercise: loop and print I
# for n in range(1,6):
#     print(n-1, end=" ")
#     print(n-1+4)
# =============================================================================

# =============================================================================
# # Exercise: loop and print II
# for n in range(1,12, 2):
#     print(n-1, end=" ")
#     print((n-1)*3)
# =============================================================================

# Exercises: loop and adding up

# =============================================================================
# # Exercise: loop and adding up I
# # What is the sum of numbers 1 through 213?
# n=1
# sum = 0
# for num in range(0, 214, 1):
#     sum = sum+num
# print("Sum is: ", sum )
# =============================================================================

# =============================================================================
# # Exercise: loop and adding up II
# # What is the sum of even numbers until 226?
# sum = 0
# for num in range(0, 228, 1):
#     if num % 2 == 0:
#         #print(num)
#         sum = sum+num
# print("Sum is: ", sum )
# =============================================================================

# Exercise: Population dynamics

# =============================================================================
# # Warm-up 1 (2)
# # how large the rabbit population will be in the absence of foxes after 40 days 
# # (initial population: 1000, increase of 5% a day)
# r=1000
# r_growth=0.05
# for d in range(1, 41, 1):
#     r=r+(r*r_growth)
#     print(d, end =" ")
#     print(int(r))
# =============================================================================

# =============================================================================
# # Warm-up 2 (2)
# # If foxes are present, the daily change in rabbit population (prey) will be: 
# # 0.05*rabbit-0.0002*fox*rabbit. 
# # Simulate the hypothetical case that the fox population does not change and is always 100. 
# # What will the rabbit population be after 10 days if it starts with 1000? 
# f=100
# r=1000
# for d in range(1, 11, 1):
#     r_growth=0.05*r-0.0002*f*r
#     r=r+r_growth
#     print(d, end =" ")
#     print(int(r))
# =============================================================================

# =============================================================================
# # Exercise: 
# # Enter the numbers of foxes and rabbits respectively after 200 days, 
# # if there are 100 foxes and 1000 rabbits present in the beginning. 
# # Your program should work with float without rounding, except for the final answer, 
# # which is to be rounded down to an integer (manually).
# f=100
# r=1000
# for d in range(1, 201, 1):
#     
#     r_growth=(0.05*r)-0.0002*f*r   # just read the text carefully: decrease vs increase
#     f_growth=(-0.1*f)+0.0001*f*r   # just read the text carefully: decrease vs increase
#     
#     r=r+r_growth
#     f=f+f_growth
#     print(d, end =" ")
#     print(r, end=" ")
#     print(f)
# =============================================================================

# Numerically solving ODEs

# =============================================================================
# # Predator and prey prolonged
# f=100
# r=1000
# for d in range(1, 1543, 1):
#     
#     r_growth=(0.05*r)-0.0002*f*r   
#     f_growth=(-0.1*f)+0.0001*f*r
#     
#     r=r+r_growth
#     f=f+f_growth
#     print(d, end =" ")
#     print(int(r), end=" ")
#     print(int(f))
# =============================================================================

# =============================================================================
# # Update every hour
# f=100
# r=1000
# for d in range(1*24, 201*24, 1):
#     
#     r_growth=((0.05*r)-0.0002*f*r)/24
#     f_growth=((-0.1*f)+0.0001*f*r)/24
#     
#     r=r+r_growth
#     f=f+f_growth
#     print(d, end =" ")
#     print(r, end=" ")
#     print(f)
# =============================================================================
    
# =============================================================================
# # Update every minute
# f=100
# r=1000
# for d in range(1*24*60, 201*24*60, 1):
#     
#     r_growth=((0.05*r)-0.0002*f*r)/(24*60)
#     f_growth=((-0.1*f)+0.0001*f*r)/(24*60)
#     
#     r=r+r_growth
#     f=f+f_growth
#     print(d, end =" ")
#     print(r, end=" ")
#     print(f)
# =============================================================================

# =============================================================================
# # Exercises: looping through lists
# # Exercise: calculation with list elements
# lys = [5, 7, 2, 9, 8, 9, 3, 4, 2, 3, 2, 7, 7, 5]
# res=1
# for l in lys: 
#     res = res*l
# print(res)
# =============================================================================

# Exercise: loop and if
# =============================================================================
# lys = [5, 7, 2, 9, 8, 9, 3, 4, 2, 3, 2, 7, 7, 5]
# res=1
# for l in lys[lys.index(3)::]: 
#     res = res*l
# print(res)
# =============================================================================
# mylist.index(x)   where x is the value (can also be a string)
# lys[x:y:z]        where x,y,z are start, stop and interval of the list





# =============================================================================
# def multiplyList(any_list):
#     # Multiply elements one by one
#     result = 1
#     for x in any_list:
#         if x==3:
#             stored = x
#             if stored==3:
#                 result = result * x
#                 return result
# lys = [3, 3, 2]
# print(multiplyList(lys))
# 
# =============================================================================




# Looping through lists using indices

# =============================================================================
# # My loop to understand how indeces work: 
# lys1=[4, 5, 7, 2]
# lys2=[3, 7, 10, 12]
# lys3=4*[0]
# for i in range(4): 
#     print(i, end = " ")
#     print(lys1[i], end = " ")
#     print(lys2[i], end = " ")
#     print(lys3[i])
# =============================================================================
    
# =============================================================================
# lys1=[4, 5, 7, 2]
# lys2=[3, 7, 10, 12]
# lys3=4*[0]
# for i in range(4): 
#    lys3[i]=lys1[i]+lys2[i]
# print (lys3)
# =============================================================================

# =============================================================================
# # Exercise: calculations with two lists
# lys1 = [7, 3, 2, 5, 1, 4, 4, 6, 2, 9, 1, 6, 3, 2, 6, 5, 5]
# lys2 = [8, 9, 8, 9, 6, 4, 5, 5, 8, 2, 4, 3, 1, 6, 5, 6, 5]
# lys3=16*[0]
# for i in range(16): 
#     lys3[i] = lys1[i] * lys2[i+1]
# print (lys3)
# print(sum(lys3))
# # trick: to get a lag in a specific list by 1 position, just +1 
# =============================================================================

















































