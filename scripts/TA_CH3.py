#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 15:50:48 2022

@author: dgaio
"""

print("Complex loops (A) ######################################################")
print("Reading nested loops ###################################################")
print("Questions: for and if ##################################################")
print("Question 1 (5) #########################################################")
# Question 1 (5)
for i in range(6):
    if 3<i<=5:
        print('yes')
# prints yes twice because i has values 0,1,2,3,4,5
#=============================================================================
print("Question 2 (5) #########################################################")
#=============================================================================
# Question 2 (5)
for i in range(6):
    if 3<i<=5:
        print('yes')
    else:
        print('no')
# prints no 4 times because it prints yes only twice 
#=============================================================================
print("Question 3 (5) #########################################################")
#=============================================================================
# Question 3 (5)
for i in range(6):
    if 3<i<=5:
        print('yes')
    elif i==2:
        print('no')
# it prints no once because i gets value 2 only once 
#=============================================================================
print("Question 4 (5) #########################################################")
#=============================================================================
# Question 4 (5)
for i in range(6):
    if 3<i<=5:
        print('yes')
    elif i<2:
        print('no')
# prints no twice because i<2 onlyy twice: 0,1 
#=============================================================================
print("Question 5 (5) #########################################################")
#=============================================================================
# Question 5 (5)
for i in range(6):
    if 3<i<=5:
        print('yes', end=" ")
    elif 2<=i<=4:
        print('no', end=" ")
        print(i)
#=============================================================================
print("#####################################################################")
print("Questions: nested loops ###############################################")
print("Question 1 (7) #########################################################")
#=============================================================================
# Question 1 (7)
for i in range(3): # (0,...) (1,...) (2,...)
    for j in range(2): # (...,0) (...,1)
        print(i,j)   
#=============================================================================
print("Question 2 (7) #########################################################")
#=============================================================================
# Question 2 (7)
for i in range(6):       # 0, 1, 2, 3, 4, 5 
    print('hello')       # 0, 1, 2, 3, 4, 5 
    for j in range(3):
        print('hi')      # 0,1,2   0,1,2   0,1,2   0,1,2   0,1,2   0,1,2
    print('bye')         # 0, 1, 2, 3, 4, 5 
#=============================================================================
print("Question 3 (7) #########################################################")
#=============================================================================
# Question 3 (7)       <-- not making sense                          
for i in range(6):
    print('hello')
    if i<=3:
        continue
    for j in range(3):      
        print('hi')
    print('bye')
#=============================================================================
print("Question 4 (7) #########################################################")
#=============================================================================
# Question 4 (7)
for i in range(6):         # 0, 1, 2, 3, 4, 5
    print('hello')
    if i<=3:               # 0, 1, 2, 3 
        for j in range(3): # (0, 1, 2)    * 4 times
            print('hi')    
        print('bye')       # 0, 1, 2, 3 
#=============================================================================
print("Question 5 (7) #########################################################")
#=============================================================================
# Question 5 (7)
for i in range(6):       
    print('hello')
    break           # the break here breaks the loop after the first iteration
    if i<=3:
        for j in range(3):
            print('hi')
        print('bye')
# prints once "hello"
#=============================================================================
print("Question 6 (7) #########################################################")
#=============================================================================
# Question 6 (7)
for i in range(6):           
    print('hello')           # 0, 1, 2, 3, 4, 5
    if i<=3:              
        for j in range(3):  
            print('hi')      # 0, 1, 2, 3
            break
        print('bye')         # 0, 1, 2, 3
#=============================================================================
print("Question 7 (7) #########################################################")
#=============================================================================
# Question 7 (7)
for i in range(6):
    print('hello')             # only once because it gets interrupted at break 
    if i<=3:                   # TRUE
        for j in range(3):     # 0, 1, 2
            print('hi')        # 0, 1, 2
        break
        print('bye')          
#=============================================================================
print("#####################################################################")       
print("Questions: double nested loops #########################################")
print("Question 1 (7) #########################################################")
# Question 1 (7)
for i in range(5):           # 0, 1, 2, 3, 4
    for j in range(3):       # 0, 1, 2
        for k in range(2):   # 0, 1
            print('hello')
# multiply 5 * 3 * 2 = 30 (because these are nested for loops)
#=============================================================================
print("Question 2 (7) #########################################################")
#=============================================================================
# Question 2 (7)
for i in range(5):             # 0, 1, 2, 3, 4
    for j in range(3):         # 0, 1, 2
        for k in range(2):     # 0, 1
            print(i,j,k)
# all the possible combinations 
#=============================================================================
print("Question 3 (7) #########################################################")
#=============================================================================
# Question 3 (7)
for i in range(4):              # 0, 1, 2, 3
    for j in range(4):          # 0, 1, 2, 3
        for k in range(4):      # 0, 1, 2, 3
            if i==j and j==k:
                print('hello')
#=============================================================================
print("Question 4 (7) #########################################################")
#=============================================================================
# Question 4 (7)
for i in range(4):              # 0, 1, 2, 3
    for j in range(4):          # 0, 1, 2, 3
        for k in range(4):      # 0, 1, 2, 3  # j==k 4 times, times loops of i (4)
            if i==j: 
                print('hello')
#=============================================================================
print("Question 5 (7) #########################################################")
#=============================================================================
# Question 5 (7)
for i in range(4):                # 0, 1, 2, 3
    for j in range(4):            # 0, 1, 2, 3
        for k in range(4):        # 0, 1, 2, 3  # j==k 4 times, times loops of i (4)
            if j==k:
                print('hello')
    print (k)       # 4 times k==3, because that's the last value at the end of each loop
#=============================================================================
print("Question 6 (7) ########################################################")
#=============================================================================
# Question 6 (7)
for i in range(4):                 
    for j in range(4):             
        for k in range(4):        
            if j==k:
                print('hello')
    print (i)
#=============================================================================
print("Question 7 (7) ########################################################")
# Question 7 (7)
for i in range(4):
    for j in range(i+1,4):
        for k in range(4):
            if i==j:
                print('hello')
print("#####################################################################")             
print("#####################################################################") 
###################################             
# Counting codons
print("Counting codons ########################################################")
bases = ['A','T','C','G']
count=0
for b1 in bases:
    for b2 in bases:
        for b3 in bases:
            count += 1
            print(count, end=" ")
            print(b1+b2+b3) 
print("#####################################################################") 
# A subset of codons
print("A subset of codons ########################################################")
bases = ['A','T','C','G']
count=0
for b1 in bases:
    for b2 in bases:
        for b3 in bases:
            if b1==b2 or b2==b3:
                if not (b1==b2==b3): 
                    count += 1
                    print(count, end=" ")
                    print(b1+b2+b3) 
print("#####################################################################")
print("#####################################################################")
################################### 
# Stochastic conditions inside loops
# Dice
print("Dice ####################################################################")
# Exercise: Rolling dice (Würfeln)
import numpy.random as rd
rd.seed(141)
count=0
for n in range(30):
    r = rd.randint(1,7)
    if r==6:
        count+=1
print(count)
print(" Rolling dice repeated #################################################")
# Exercise: Rolling dice repeated
rd.seed(141)
for game in range(10):
    count=0
    for n in range(30):
        r = rd.randint(1,7)
        if r==6:
            count+=1
    print(count)
# by running the game 10 times (each time rolling dice 30 times), 
# Only in one game I got 10 times "6". That is 1 out of 10 = 0.1 = 10% 
print(" Autochecker: probabilities #############################################")
# Exercise: Autochecker: probabilities 
rd.seed(141)
tot=0
for game in range(10):
    count=0
    for n in range(30):
        r = rd.randint(1,7)
        if r==6:
            count+=1
    print(count)
    if count>=10:
        tot+=1
print("tot is: ", tot)
print(" Heads and tails (Kopf oder Zahl) #######################################")
# Heads and tails (Kopf oder Zahl)
import numpy.random as rd
rd.seed(14)

longest=0
ones=0
twos=0

for n in range(1000):
    r = rd.randint(1,3)
    if r==1:
        ones+=1
        twos=0
    else:
        ones=0
        twos+=1
    if ones>longest:
        longest=ones
    if twos>longest:
        longest=twos 
    print(r)
print("longest: ", longest)
print(" Warm-up: Consecutive sequence ##########################################")
# Warm-up: Consecutive sequence
#########
#########
#########
print(" Warm-up: Maximum #######################################################")
# Warm-up: Maximum
import numpy.random as rd
rd.seed(5)
my_max=0
for n in range(500):
    r = rd.randint(1,5000)
    if r>my_max:
        my_max=r
print(my_max)  
print(" Turing's card problem ##################################################")
# guess the suit of a card 400 times
# 117 times or more correct 
# repeat 10,000 times 
import numpy.random as rd
at_least_117=0
# repeat 10,000 times
for j in range(10000):
    correct=0
    for i in range(400):
        # guess the suit of a card
        r=rd.randint(1,4)
        if r==1:     
            correct+=1
    if correct >=117:
        at_least_117+=1
probability=1-at_least_117/10000
print(probability)

    
    



