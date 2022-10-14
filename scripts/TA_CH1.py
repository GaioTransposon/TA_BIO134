#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 12:57:47 2022

@author: dgaio
"""


# =============================================================================
# # Dread Pirate Roberts: 
# import random
# secret = random.randint(1, 99)  # Picks secret number
# guess = 0
# tries = 0
# print ("AHOY! I'm the Dread Pirate Roberts, and I have a secret!")
# print ("It is a number from 1 to 99. I'll give you 6 tries.")
# 
# # Allows up to 6 guesses
# while guess != secret and tries < 6:
#     guess = int(input("What's yer guess? "))  # Gets player’s guess
#     if guess < secret:
#         print ("Too low, ye scurvy dog!")
#     elif guess > secret:
#         print ("Too high, landlubber!")
#     tries = tries + 1                          # Uses up one try
# 
# # Prints a message at the end of the game
# if guess == secret:
#     print ("Avast! Ye got it! Found my secret, ye did!")
# else:
#     print ("No more guesses! Better luck next time, matey!")
#     print ("The secret number was", secret)
# =============================================================================

# First steps in Python

# =============================================================================
# # "random" is a module
# # randit is a function of the "random" module
# 
# # incorrect because randit is not a function of numpy 
# import numpy
# secret = numpy.randint(1,100)
# 
# # correct
# import numpy as np
# secret = np.random.randint(1,100)
# 
# # incorrect because you are not importing numpy first 
# secret = numpy.random.randint(1,100)
# 
# # incorrect because "random " is repeated twice 
# import numpy.random as rd
# secret = rd.random.randint(1,100)
# 
# # correct
# import numpy.random as rd
# secret = rd.randint(1,100)
# 
# # correct 
# import numpy.random as joke
# secret = joke.randint(1,100)
# =============================================================================

# =============================================================================
# # Exercise: randint() in random and numpy library
# 
# # check whether the randint() function of random does the same as the randint() function of numpy.random
# import random as rand
# num = rand.randint(1,3)
# print(num)
# # yes, can acquire 1, 2, or 3 
# 
# # Which of the following values can num acquire?
# import numpy.random as rd
# num = rd.randint(1,3)
# print(num)
# # 1 or 2. But why not 3 actually?
# # because numpy.random.randint() and random.randint() are thus not exactly the same
# =============================================================================

# =============================================================================
# # Exercise: quotient and remainder
# q = 3987 // 8
# mod = 3987 % 8
# print(q, mod)
# 
# # Exercise: e-notation
# scientific_notation = "{:e}".format(0.000356)
# print(scientific_notation)
# =============================================================================

# =============================================================================
# # Exercise: square root
# 
# # with library:
# import math
# print(math.sqrt(4489))
# 
# # only with operator: 
# print(4498 ** (0.5))
# =============================================================================

# =============================================================================
# # Data types 
# 
# # string 
# a = '5'
# 
# # float
# a = 5.
# 
# # boolean 
# x = 2 > 3
# =============================================================================

# Basic operations in Python 
    
# Input: 
# Make a program that asks the user for a float, squares this float, 
# converts the outcome to an integer and prints this integer. 

# =============================================================================
# a = input("give me a float ")
# a=float(a)
# 
# if(type(a) == float):
#     print('This is a float')      
#     squared = a**2
#     integer = int(squared)
#     print(integer)
#     
# else: 
# 	print('Not a float') 
# =============================================================================

# =============================================================================
# # Exercise: printing on the same line
# a = 3
# print(a)
# a += 2
# print(a, end=" ")
# =============================================================================

# Exercises in Logic 

# =============================================================================
# # Question 2 (6)
# # It prints 3 because if statement is met (b does not change) 
# a = 2
# b = 3
# if a == 2:
#    a += 1
# else:
#    b *= 2
# print(b)
# =============================================================================

# =============================================================================
# # Question 3 (6)
# # It prints 3 because it enters immediately else. 
# # (b *= 2) == (b = b*2)
# a = 2
# b = 3
# if a == 3:
#    a += 1
# else:
#    b *= 2
# print(b)
# =============================================================================

# =============================================================================
# # Question 4 (6) 
# # It does not enter elif because 1st condition is met first (top to bottom)
# a = 2
# b = 3
# if a == 2:
#    a += 1
# elif b == 3:
#    b *= 2
# print(b)
# =============================================================================

# =============================================================================
# # Question 5 (6)
# # it enters elif, b becomes 6 then 5 is added to it
# a = 2
# b = 3
# if a == 3:
#    a += 1
# elif b == 3:
#    b *= 2
#    if b == 6:
#       b += 5
# else:
#    b -= 1
# print(b)
# =============================================================================

# =============================================================================
# # Question 6 (6)
# # It enters elif, b becomes 6, then stops 
# a = 2
# b = 3
# if a == 3:
#    a += 1
# elif b == 3:
#    b *= 2
#    if b == 4:
#       b += 5
#    elif a == 3:
#       b += 6
# else:
#    b -= 1
# print(b)
# =============================================================================

# Branches 

# =============================================================================
# # Gene mapping: 
# # Write a program that asks for a recombination frequency as input 
# # and gives the map distance as output. 
# # In case a frequency lower than zero or higher than or equal to 0.5 is entered, 
# # the program should tell the user that the recombination frequency must be 
# # equal to or higher than 0 and lower than 0.5. 
# # The natural logarithm can be calculated using log() from the numpy library.
# 
# import numpy as np 
# f_rec = float(input('Please enter the recombination frequency: ')) 
# if f_rec < 0 or f_rec >= 0.5: 
#     print('The recombination frequency must be equal to or higher than to 0 and lower than 0.5') 
# else: 
#     d_map = -1/2*np.log(1-2*f_rec) 
#     print('The map disctance d: ', d_map) 
# =============================================================================









