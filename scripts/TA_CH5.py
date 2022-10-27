#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 11:43:44 2022

@author: dgaio
"""

          
# =============================================================================
# # Auto-checker: assembling a list
# bases = ['A','T','C','G']
# my_list = []
# 
# for b1 in bases:
# 	for b2 in bases:
# 		for b3 in bases:
# 			if b1 != b2 and b2 != b3:
# 				my_list.append(b1 + b2 + b3)
# 
# my_list.sort()
# print(my_list[28])
# =============================================================================

# =============================================================================
# # # Auto-checker:select bases
# this_list = ['d', 'i', 'v', 'g', 'p', 'h', 'r', 'f', 'd', 'd', 'j', 'n', 'j', 'k', 'l', 'c', 'm', 'u', 'i', 'c', 'g', 's', 'o', 'a', 't', 's', 't', 'p', 'h', 'x', 'e', 'l', 'a', 'a', 'n', 'a', 'd', 'l', 'w', 'v', 't', 'i', 'm', 'y', 'u', 'v', 'r', 'e', 'j', 'm', 'i', 'c', 'z', 'j', 'o', 'g', 'z', 'a', 'a', 'g', 'a', 'x', 'i', 'm', 'd', 'z', 't', 'n', 'w', 'j', 't', 'm', 'g', 'o', 'c', 'd', 'y', 'b', 'c', 'q']
# 
# lys_DNA=['a','t','c','g']
# lys_RNA=['a','u','c','g']
# 
# only_DNA = [i for i in this_list if i in lys_DNA]
# print(only_DNA)
# print(len(only_DNA))
# 
# only_RNA = [i for i in this_list if i in lys_RNA]
# print(only_RNA)
# print(len(only_RNA))
# =============================================================================

# =============================================================================
# # Exercise: keyword 'in'
# l = ['a', 'c', 'd', 'e', 'c', 'y']
# if 'c' in l:
#     print ('Found it!')
# =============================================================================

# =============================================================================
# # Question 1 (8)
# lyst = [5, 8, 2, 4, 6, 9, 1]
# print(lyst[2])
# =============================================================================

# =============================================================================
# #Question 2 (8)
# lyst = [5, 8, 2, 4, 6, 9, 1]
# print(lyst[-2])
# =============================================================================

# =============================================================================
# #Question 3 (8)
# lyst = [5, 8, 2, 4, 6, 9, 1]
# print(lyst[10])
# =============================================================================

# =============================================================================
# #Question 4 (8)
# lyst = [5, 8, 2, 4, 6, 9, 1]
# print(lyst[2:5])
# =============================================================================

# =============================================================================
# #Question 5 (8)
# lyst = [5, 8, 2, 4, 6, 9, 1]
# print(lyst[:3])
# =============================================================================

# =============================================================================
# #Question 6 (8)
# lyst = [5, 8, 2, 4, 6, 9, 1]
# print(lyst[5:])
# =============================================================================

# =============================================================================
# #Question 7 (8)
# lyst = [5, 8, 2, 4, 6, 9, 1]
# print(lyst[5:9])
# =============================================================================

# =============================================================================
# #Question 8 (8)
# lyst = [5, 8, 2, 4, 6, 9, 1]
# print(lyst[8:10])
# =============================================================================

# =============================================================================
# # Exercises: enumerate & lists of lists
# # Exercise: enumerate
# lys = ['The', 'sun', 'is', 'shining']
# i = 0
# for w in lys:
#    print(i, w)
#    i += 1
# 
# #Replace the program above by two other programs that do the same:
# #- one using range()
# for w in range(len(lys)):
#     print(w, lys[w])
#    
# #- one using enumerate()
# for i,w in enumerate(lys):
#     k = lys.index(w)
#     print(k,w)
# =============================================================================
    
# =============================================================================
# # Exercise: lists of lists 1 (4)
# lyst = [[2, 4], [1, 5, 7], [2, 6]] 
# print(lyst)
# # append '8' to list number 2 (which is index 1) of lyst:
# lyst[1].append(8)
# print(lyst)
# =============================================================================

# =============================================================================
# # Exercise: lists of lists 2 (4)
# lyst = [[2, 4], [1, [5, 9], 7], [2, 6]] 
# print(lyst)
# # append '3' to list number 2 (which is index 1) of list number 2 of lyst:
# lyst[1][1].append(3)
# print(lyst)
# =============================================================================

# =============================================================================
# # Exercise: lists of lists 3 (4)
# lyst = [[2, 4], [1, [5, 9], 7], [[2], 6]] 
# print(lyst)
# lyst[2][0].append(8)
# print(lyst)
# # [[2, 4], [1, [5, 9], 7], [[2, 8], 6]]
# =============================================================================

# =============================================================================
# # Exercise: lists of lists 4 (4)
# lyst = [[2, 4], [1, [5, 9], 7], [[2], 6]] 
# print(lyst)
# lyst[2][0].remove(2)
# print(lyst)
# =============================================================================

# =============================================================================
# # [Optional] Synonyms vs. copies: list of lists (Q1)
# a = [3, 2, 4]
# print(a, 'is a')
# b = [7, a]
# print(b, 'is b')
# c = a[:]
# print(c, 'is c')
# d = b[:]
# print(d, 'is d')
# print('#####')
# b[1][0] = 10
# b[0] = 6
# a[2] = 50
# print(a, 'is a')
# print(b, 'is b')
# print(c, 'is c')
# print(d, 'is d')
# =============================================================================

# =============================================================================
# # [optional] Synonyms vs. copies: list of lists (Q2)
# a = [3, 2, 4]
# print(a, 'is a')
# b = [7, a]
# print(b, 'is b')
# c = a[:]
# print(c, 'is c')
# d = b[:]
# print(d, 'is d')
# print('#####')
# b[1] = 10
# print(a, 'is a')
# print(b, 'is b')
# print(c, 'is c')
# print(d, 'is d')
# print('#####')
# b[0] = 6
# print(a, 'is a')
# print(b, 'is b')
# print(c, 'is c')
# print(d, 'is d')
# print('#####')
# a[2] = 50
# print(a, 'is a')
# print(b, 'is b')
# print(c, 'is c')
# print(d, 'is d')
# =============================================================================

# =============================================================================
# # Auto-checker: Tuples are immutable
# lyst = [2, 7, 6] 
# lyst = tuple(lyst)
# print(lyst)
# lyst[2]='d'
# print(lyst)
# =============================================================================

# =============================================================================
# # Auto-checker: Creating tuples
# t = (5, 4, 2)
# u = 5, 4, 2
# if t == u:
#     print('they are the same')
# =============================================================================

# =============================================================================
# # Looping through lists of lists (video)
# 
# l=[5,7,2]
# for el in l:
#     print(el)
# print('#####')
#     
# l=[5,7,2, [10,11]]
# for el in l:
#     print(el)
# print('#####')
#     
# l=[[5,4,9],[7,8],[2,5,6]]
# for el in l:
#     print(el)
# print('#####')
# 
# # read elements of list
# l=[[5,4,9],[7,8],[2,5,6]]
# for i, el in enumerate(l):
#     for j, el2 in enumerate(el):
#         print(i,j,el2)
# print('#####')
#         
# # add a plus 1 to all elements of nested list
# l=[[5,4,9],[7,8],[2,5,6]]
# for i, el in enumerate(l):
#     for j, el2 in enumerate(el):
#         l[i][j]+=1
# print(l)
# print('#####')
# 
# # add a plus 1 to all elements of nested list: SAFER WAY: 
# import copy
# l=[[5,4,9],[7,8],[2,5,6]]
# new_list=copy.deepcopy(l)
# for i, el in enumerate(l):
#     for j, el2 in enumerate(el):
#         new_list[i][j]+=1
# print(new_list)
# print('#####')
# 
# # add a plus 1 to all elements of nested list: SAFER-SAFER WAY: 
# import copy
# l=[[5,4,9],[7,8],[2,5,6]]
# new_list=copy.deepcopy(l)
# for i, el in enumerate(l):
#     for j, el2 in enumerate(el):
#         new_list[i][j] = l[i][j]+1
# print(new_list)
# print('#####')
# =============================================================================

# =============================================================================
# # Exercises on looping through lists: turn to integers 
# import copy
# l = [['8', '6', '9'], ['3'], ['8', '3'], ['8', '4', '1', '2'], ['9', '5'], ['5', '9', '7'], ['4', '8', '8', '2'], ['6', '3', '3', '4'], ['8', '4', '3'], ['3', '6', '1', '2'], ['4', '9', '6', '4'], ['3', '7', '4'], ['5', '6'], ['9', '1'], ['2', '5'], ['3'], ['6', '8', '9'], ['7', '5'], ['8', '4', '1'], ['6', '6'], ['4'], ['5', '8', '7'], ['8', '8', '4'], ['5'], ['8', '3'], ['9'], ['4', '9'], ['6', '6', '6'], ['8', '6', '5', '1'], ['5', '7', '3', '6'], ['8', '4', '3', '7'], ['3', '8'], ['9', '2'], ['8', '3', '1', '1'], ['1', '7'], ['1'], ['2', '4', '5', '9'], ['2', '5'], ['9', '7', '1'], ['1'], ['1', '8', '7', '9'], ['5', '1', '3', '1'], ['2', '5', '4', '3'], ['4', '6'], ['5', '5', '2', '7'], ['2', '9'], ['8', '7', '5', '8'], ['7', '5'], ['7'], ['9', '2'], ['7', '1'], ['1', '5', '5', '9'], ['3', '2', '1', '9'], ['5', '9'], ['2'], ['7', '1'], ['6', '6'], ['9', '5'], ['2'], ['7', '9', '1', '4'], ['8', '1'], ['1']]
# new_list=copy.deepcopy(l)
# for i, el in enumerate(l):
#     for j, el2 in enumerate(el):
#         new_list[i][j] = int(l[i][j])
# print(new_list)
# print('#####')
# =============================================================================

# =============================================================================
# # Exercises on looping through lists: turn to integers 
# lists = [[6, 1, 6], [6], [5, 6, 6], [5], [4], [7, 5, 7, 2], [5, 8], [9], [7], [5, 6], [3, 4], [8], [4, 9, 3, 6], [8, 2, 4], [9, 7], [6, 8], [2, 5], [2, 4], [8, 3, 4], [5, 2], [4], [4, 4, 5, 5], [5, 1], [1, 4, 8], [6, 5], [5, 7, 8, 9], [1], [6], [3], [6], [7, 3, 8, 8], [6], [2, 5, 4], [7], [3, 7], [1, 9, 1, 1], [2, 6, 2], [2, 7, 5], [6, 3, 7], [6, 1], [6, 3, 9, 7], [4, 3, 3]]
# new_list = []
# for nested in lists:
#     new_ls = []
#     my_sum=0
#     for item in nested:
#         my_sum=my_sum+item**2    # also: my_sum += item**2 
#     new_list.append(my_sum)
# print(new_list)
# =============================================================================

# =============================================================================
# # Reading text files 1(2)
# import os
# os.getcwd()
# my_file = open('/Users/dgaio/Downloads/thompson.txt')
# lines = my_file.readlines()
# my_file.close()
# print(lines[89][:48])
# =============================================================================

# =============================================================================
# # Exercise: copy
# my_file = open('/Users/dgaio/Downloads/crick.txt')
# lines = my_file.readlines()
# s=''
# for line in lines: 
#     print(line)
#     s+= line.strip()+' '
# print(s)
# =============================================================================

# =============================================================================
# lines = my_file.readlines()
# print(str(lines).strip("'[]"))
# my_file.close()
# =============================================================================

# =============================================================================
# # Exercise: split & join
# s = 'dfkfje*jfdn*pwndnv*sfkjadjbvbjbajbfkaj*nkd*nvndlanakndndhnfajnja*lsdkjf*cevgfjh**nfe*en*m\r\n'
# print(s)
# z = s.split()
# z = "".join(z)
# z = z.split('*')
# z = "".join(z)
# print(z)
# print(len(z))
# =============================================================================

# =============================================================================
# # Exercise: txt-file
# import statistics
# fyle = open('/Users/dgaio/Downloads/darwin.txt')
# lines = fyle.readlines()
# fyle.close()
# empty=[]
# for line in lines:
#     z = line.split()
#     print(z[2], len(z[2]))
#     empty.append(len(z[2]))
# print(statistics.mean(empty))
# =============================================================================
    
# =============================================================================
# # [Optional] Coding in an html-file
# fyle = open('/Users/dgaio/Downloads/headings.html')
# lines = fyle.readlines()
# print(lines)
# =============================================================================

# =============================================================================
# # [Optional] Reading webpages
# import urllib.request
# seite = urllib.request.urlopen('http://helloworldbook2.com/data/message.txt')
# message = seite.read()
# message = str(message,encoding='utf-8') # optional
# print (message)
# =============================================================================

# =============================================================================
# # Auto-Checker Proteomics exercise (I)
# brain = open('/Users/dgaio/Downloads/proteomics/human_brain_proteins.csv')
# plasma = open('/Users/dgaio/Downloads/proteomics/human_plasma_proteins.csv')
# 
# lines_brain = brain.readlines()[1:]
# lines_plasma = plasma.readlines()[1:]
# print(len(lines_brain))
# print(len(lines_plasma))
# =============================================================================


# =============================================================================
# # Auto-Checker Proteomics exercise (II)
# brain = open('/Users/dgaio/Downloads/proteomics/human_brain_proteins.csv')
# plasma = open('/Users/dgaio/Downloads/proteomics/human_plasma_proteins.csv')
# 
# brain_lines = brain.readlines()[1:]
# plasma_lines = plasma.readlines()[1:]
# 
# 
# def get_IDs(lines):
#     
#     my_list=[]
#     for n in range(0,len(lines)):
#         
#         x = lines[n]
#         x = x.split(',')
#         ID = x[0]
#         
#         if ID not in my_list:
#             
#             my_list.append(ID)
#             
#     return(my_list)
#     
#     
# brain_IDs = get_IDs(brain_lines)
# plasma_IDs = get_IDs(plasma_lines)
# 
# 
# only_brain = list(set(brain_IDs) - set(plasma_IDs))
# print('only brain:', len(only_brain))
# 
# only_plasma = list(set(plasma_IDs) - set(brain_IDs))
# print('only plasma:', len(only_plasma))
# 
# both = list(set(brain_IDs).intersection(plasma_IDs))
# print('in common:', len(both))
# 
# only_brain.sort()
# print(only_brain[1131])
# 
# only_plasma.sort()
# print(only_plasma[1131])
# 
# both.sort()
# print(both[1131])
# =============================================================================

# =============================================================================
# # [Advanced] Gamow's diamonds
# bases = 'ATGC'
# complements = 'TACG'
# diamonds = {}
# 
# for i, b1 in enumerate(bases):
#     for j, b2 in enumerate(bases):
#         for k, b3 in enumerate(bases):
#             codon = b1+b2+b3
#             diamond = [b1+b2+complements[k]+complements[j], b1+complements[j]+complements[k]+b2, \
#                        complements[k]+complements[j]+b1+b2, complements[k]+b2+b1+complements[j]]
#             diamond.sort()
#             diamond = tuple(diamond)
#             print(diamond)
#             if not diamond in diamonds:
#                 diamonds[diamond] = []
#             diamonds[diamond].append(codon)
#             diamonds[diamond].sort()               
#     
# print(diamonds)
# codonList = sorted(list(diamonds.values()))
# =============================================================================



