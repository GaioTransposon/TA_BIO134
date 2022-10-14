#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 12:40:55 2022

@author: dgaio
"""

# =============================================================================
# # Calculations with a list
# # Exercise: Reviewing lists
# l = [38, 38, 46, 46, 13, 24, 3, 54, 18, 47, 4, 42, 8, 66, 50, 46, 62, 36, 19, 19, 77, 17, 7, 63, 28, 47, 46, 65, 63, 12, 16, 24, 14, 51, 34, 56, 29, 59, 92, 79]
# new_list=[]
# for i in l: 
#     new_list.append(i**3)
# print(new_list)
# =============================================================================

# =============================================================================
# # Coins
# import numpy.random as rd
# rd.seed(0)
# 
# heads_in_row=0
# tails_in_row=0
# count=0
# 
# while heads_in_row or tails_in_row <= 7: 
#     
#     flip=rd.randint(1,3)
#     count+=1
#     
#     if flip==1:
#         heads_in_row+=1
#         tails_in_row=0
#         print(flip, "which is head; in a row:", heads_in_row)
#         
#     if flip==2:
#         heads_in_row=0
#         tails_in_row+=1
#         print(flip, "which is tail; in a row:", tails_in_row)
#     
# print(count)
# =============================================================================
        
# Simulating a cross
##### MY LAPTOP


# Comparison with expected outcome
##### MY LAPTOP

# =============================================================================
# # Testing Mendel's first experiment
# import numpy as np
# np.random.seed(0)
# tot_men_closer=0
# tot_equal=0
# tot_sim_closer=0
# 
# for game in range(0,10000):
#     
#     sim_dom=0
#     men_closer = 0
#     equal = 0
#     sim_closer = 0
#     
#     for i in range(0,7324):
#         allele_parent1 = np.random.randint(0,2)
#         if allele_parent1 == 0:
#             allele1 = 'd'
#         else:
#             allele1 = 'r'
#         allele_parent2 = np.random.randint(0,2)
#         if allele_parent2 == 0:
#             allele2 = 'd'
#         else:
#             allele2 = 'r'
#         if allele1 == 'd' or allele2 == 'd':
#             sim_dom += 1
#     #print(sim_dom)
#     
#     exact_dominant=5493
#     men_dom=5474
#     x = exact_dominant-sim_dom
#     y = exact_dominant-men_dom
#     
#     #print(abs(x))
#     #print(abs(y))
#     
# 
#     if abs(x) > abs(y):
#         sim_closer += 1
#         #print("mend closer", mendel_closer)
#     elif abs(x) < abs(y):
#         men_closer +=1 
#         #print("mendel cheated", mendel_cheated)
#     elif abs(x)==abs(y):
#         equal += 1
#         #print("equal", equal)
#     #else: 
#         #print("booo")
# 
#     tot_men_closer = tot_men_closer + men_closer
#     tot_equal = tot_equal + equal
#     tot_sim_closer = tot_sim_closer + sim_closer 
#     
# print("tot mendel closer", tot_men_closer)
# print("tot equal", tot_equal)
# print("tot simulation closer", tot_sim_closer)
# =============================================================================

# =============================================================================
# # Testing all of Mendel's experiments
# # Warm-up
# lys1 = [4, 3, 91, 5, 67, 53, 2]
# lys2 = [46, 68, 30, 29, 100, 7, 4]
# lys3=[]
# 
# for count, item in enumerate(lys1, start=1):
#     
#     if count<=3:
#         R = item*lys2[count-1]
#         lys3.append(R)
#         
#     if count > 3:
#         R = item+lys2[count-1]
#         lys3.append(R)
# 
# print(lys3)
# print(sum(lys3))
# =============================================================================
    
# =============================================================================
# # Mendel exercise 
# import numpy.random as rd
# 
# men_dom=[5474,6022,705,882,428,651,787,372,353,64,71,60,67,72,65]
# men_rec=[1850,2001,224,299,152,207,277,193,166,36,29,40,33,28,35]
# 
# men_closer=15*[0]
# sim_closer=15*[0]
# equal=15*[0]
# 
# 
# for k in range(15):
#     
#     plant_number=men_dom[k]+men_rec[k]
#     
#     if k<7:
#         expected_dom=plant_number*3/4
#     else:
#         expected_dom=plant_number*2/3
#         
#         
#     # 1000 times
#     for j in range(1000):
# 
#         sim_dom=0
#         for i in range(plant_number):
#             
#             # simulate a cross
#             if k<7:
#                 r=rd.randint(1,5)
#             else:
#                 r=rd.randint(1,4)
#                 
#             if r>1: 
#                 sim_dom+=1
# 
#         # check whether Mendel is closer to the expected result or whether ...
#         if abs(men_dom[k]-expected_dom) < abs(sim_dom-expected_dom):
#             men_closer[k]+=1
#         elif abs(sim_dom-expected_dom) < abs(men_dom[k]-expected_dom):
#             sim_closer[k]+=1
#         else: 
#             equal[k]+=1 
# 
# print('men_closer',men_closer)
# print("sim_closer",sim_closer)
# print("equal",equal)   
# =============================================================================


