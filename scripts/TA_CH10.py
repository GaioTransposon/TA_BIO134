#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 18:14:39 2022

@author: danielagaio
"""
#####
#using lists
l1 = ['pear', 'apple', 'strawberry', 'apple']
l2 = ['grape', 'apple', 'melon', 'strawberry', 'orange']

common = []
for fruit in l1:    # ['pear', 'apple', 'strawberry', 'apple']
    if fruit in l2:    # ['grape', 'apple', 'melon', 'strawberry', 'orange']
        if fruit not in common:
            common.append(fruit)   # 'apple', 'strawberry'
#print(common)
#####
#using dictionaries
d1 = {'pear': [0], 'apple': [1, 3], 'strawberry': [2]}
d2 = {'grape': [0], 'apple': [1], 'melon': [2], 'strawberry': [3], 'orange': [4]}

common = []
for fruit in d1:
    if fruit in d2:
        if fruit not in common:
            common.append(fruit)
#print(common)
#####
import numpy.random as rd
import time

def random_list(length):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    l = []
    for i in range(length):
        s = ''
        for j in range(5):
            s += alphabet[rd.randint(0,24)]
        l.append(s)
    return l

rd.seed(0)
l1 = random_list(10000)
l2 = random_list(10000)

#####
# Exercise: Test speed dictionaries I
def list_to_dict(some_list):
    new_dict={}
    counter=0
    for i in some_list: 
        if i not in new_dict:
            new_dict[i]=[counter]
        else:
            new_dict[i].append(counter)
        counter+=1
    return(new_dict)

d1=list_to_dict(l1)
print(d1['oodms'])
d2=list_to_dict(l2)
#####
# Exercise: Test speed dictionaries II
# Time the part that finds the common strings in the two new dictionaries, 
# don't include generating the dictionaries. 
# Compare this time with the time that is used for the list part.
time_list0 = time.time()
common = []
for fruit in l1:
    if fruit in l2:
        if fruit not in common:
            common.append(fruit)
time_list2 = time.time()
###
time_dict0 = time.time()
common = []
for fruit in d1:
    if fruit in d2:
        if fruit not in common:
            common.append(fruit)
time_dict2 = time.time()
print((time_dict2-time_dict0)/(time_list2-time_list0))

#####
# Exercise: Test speed dictionaries II
time_create_dicts0 = time.time()
d1=list_to_dict(l1)
d2=list_to_dict(l2)
time_create_dicts2 = time.time()
print('time_to_create_dicts:', (time_create_dicts2-time_create_dicts0))
print('time_to_process_dicts:',(time_dict2-time_dict0) )
print('time_to_process_lists:',(time_list2-time_list0))
print('time_to_process_dists_incl_creation:',(time_create_dicts2-time_create_dicts0)+(time_dict2-time_dict0))
#####
# Exercise: generating pairs
l = ['ball','clock','glass','table']
# Generate all unique pairs of words that are listed above. 
# The order is not important, so that ['ball','glass'] 
# is considered the same as ['glass','ball'] 
# and only one of these options should be included. 
# The words should be different, so ['ball','ball'] is not allowed. 
# Put all unique combinations into a list, so that you get a list of lists.
l2=[]
for i in l:
    for j in l:
        if i!=j:
            x = [i,j]
            x_inv = [j,i]
            if x_inv not in l2:
                l2.append(x)
print(l2)
#####
# Dot plots Exercise

line1 = 'My care is loss of care, by old care done'
line2 = 'Your care is gain of care, by new care won'

# Program three functions for generating a dot plot

# slyce(line, width), which returns a dictionary. 
# The keys of the dictionary are strings of 'width' characters 
# and the values are lists with the positions of these strings in 'line'.

def slyce(some_line, this_width):

    some_dict={}
    for i in range(0,len(some_line)):
        x = some_line[i:i+this_width]
        
        if len(x)==this_width:
            
            if x not in some_dict:
                some_dict[x]=[i]
            else:
                some_dict[x].append(i)   

    return some_dict
    
d=slyce(line1,5)
print(d[' care'])
print(len(d))
# Slyce function (3/3)
d=slyce(line1,1)
print(len(d))
#####
# Match function
# match(line1, line2, width), which returns a tuple with two lists. 
# These lists will be the x- and y-values, respectively, to generate the plot above. 
# Before programming this function, you may want to try the warm-ups at the bottom of this page.
def match_me(some_line1,some_line2, some_width):
    dic1=slyce(some_line1,some_width)
    dic2=slyce(some_line2,some_width)
    x_val=[]
    y_val=[]
    for i in dic1: 
        if i in dic2:
            #print(i, dic1[i], dic2[i])
            for ii in dic1[i]:
                for jj in dic2[i]:
                    #print(i, dic1[i], dic2[i], ii,jj)
                    x_val.append(ii)
                    y_val.append(jj)
                    
    my_tuple=(x_val, y_val)
    return my_tuple  
out=match_me(line1,line2,5)
print(out)
sum(out[0])
sum(out[1])
# Plot: 
import matplotlib
matplotlib.pyplot.scatter(out[0],out[1])
#####
# Match function warmup (1/2)
# Write a program that prints two lists which contain the information 
# of these combinations: one list with the numbers from l1 and one with 
# the numbers from l2.
l1 = [7, 2, 1, 4, 8, 9]
l2 = [4, 3, 9, 8, 1, 2]
def match_1(some_list1,some_list2):
    my_x=[]
    my_y=[]
    for i in some_list1:
        for j in some_list2:
            #print(i,j)
            my_x.append(i)
            my_y.append(j) 
    tups=(my_x,my_y)
    return(tups)  
out=match_1(l1,l2)
print(sum(out[0]))
print(sum(out[1]))
#####
# Match function warmup (2/2)     
     
l1 = [[4, 5, 8], [3, 2], [6], [2, 9, 6]]
l2 = [[9, 3], [8, 8], [5, 3, 5, 1], [7, 3]]

new_l1=[]
new_l2=[]
for n in range(len(l1)):
    #print(l1[n], l2[n])
    for i in l1[n]:
        for j in l2[n]:
            #print(i,j)
            new_l1.append(i)
            new_l2.append(j)
print(sum(new_l1))
print(sum(new_l2))
#####
# Fetching sequences from Uniprot using Biopython
from Bio import ExPASy, SeqIO

def fetch_genbank(sid):
    #fetches a genbank file (sid = sequence ID) from Uniprot
    try:
        handle = ExPASy.get_sprot_raw(sid)
        seq = SeqIO.read(handle,'swiss')
        SeqIO.write(seq, sid+'.genbank','genbank')
        print(sid,'sequence length',len(seq))
    except Exception:
        print (sid,'not found')

def read_genbank(fname):
    #extracts the organism name and the sequence
    #from a local genbank file
    f = open(fname)
    for p in SeqIO.parse(f,'genbank'):
        break
    f.close()
    return p.annotations['organism'],str(p.seq)
    
#fetch a genbank file for a specific sequence ID 
#and read in the organism and the sequence.

fetch_genbank('B4F440')

organism,seq = read_genbank('B4F440.genbank')

print(organism)
print(seq)
#####
# Exercise: Sequence Alignment: sequence alignment 1(4)

# Compute the dotplot coordinates of Q95A26 (Orangutan) vs Q9T9W0 (Chimpanzee) 
# using subsequences of length 10. 
# If the coordinates are x and y respectively, give sorted(zip(x,y))[40]. 
# You need to enter two integers separated by a space.


fetch_genbank('Q95A26')
orangutan,seq_o = read_genbank('Q95A26.genbank')
print(orangutan,seq_o)

fetch_genbank('Q9T9W0')
chimp,seq_c = read_genbank('Q9T9W0.genbank')
print(chimp,seq_c)

out=match_me(seq_o,seq_c,10)
print(out)

sorted(zip(out[0],out[1]))[40]

#####
# Exercise: Sequence Alignment: sequence alignment 2(4)
print(len(out[1]))

fetch_genbank('P00846')
homo,seq_h = read_genbank('P00846.genbank')

fetch_genbank('Q2I3G9')
ind,seq_i = read_genbank('Q2I3G9.genbank')

fetch_genbank('Q9TA24')
afr,seq_a = read_genbank('Q9TA24.genbank')

m1=match_me(seq_o,seq_c,10)
m2=match_me(seq_o,seq_h,10)
m3=match_me(seq_o,seq_i,10)
m4=match_me(seq_o,seq_a,10)
m5=match_me(seq_c,seq_h,10)
m6=match_me(seq_c,seq_i,10)
m7=match_me(seq_c,seq_a,10)
m8=match_me(seq_h,seq_i,10)
m9=match_me(seq_h,seq_a,10)
m10=match_me(seq_i,seq_a,10)

# This below is probably unnecessary, I overestimated the exercise. 
# =============================================================================
# def subs_10aa(some_match):
#     
#     place_holder=0
#     counter=0
#     ten=0
#     for i in some_match[0]:
# 
#         diff=place_holder-i
#         place_holder=i
# 
#         
#         if diff==(-1):
#             counter+=1
#         else:
#             counter=0
#             
#         if counter==10:
#             ten+=1
#             
#         print(i, place_holder, diff, counter, ten)
#         
#     return(ten)
#     
# 
# out=subs_10aa(m1)+subs_10aa(m2)+subs_10aa(m3)+subs_10aa(m4)+subs_10aa(m5)+\
#     +subs_10aa(m6)++subs_10aa(m7)++subs_10aa(m8)++subs_10aa(m9)++subs_10aa(m10)
# print(out)
# =============================================================================
# answer is simpler: 
tot=m1[0],m2[0],m3[0],m4[0],m5[0],m6[0],m7[0],m8[0],m9[0],m10[0]    
counter=0
for i in tot:
    for j in i: 
        counter+=1
print(counter)
#####
# Exercise: Sequence Alignment: sequence alignment 3(4) + 4(4)
for i in range(len(tot)): 
    print(i+1, len(tot[i]))
#####

#### Maria's code: 

import matplotlib.pyplot as plt
from Bio import ExPASy, SeqIO

####
#functions
####

def slyce(lyne,w):
    dic={}
    for i in range (len(lyne)-w+1):
        frag=lyne[i:i+w]
        if frag not in dic:
            dic[frag]=[]
        dic[frag].append(i)
    return dic

def match (l1,l2,w):
    dic1=slyce(l1,w)
    dic2=slyce(l2,w)
    both = []
    for s in dic1:
        if s in dic2:
            if s not in both:
                both.append(s)
    lis1=[]
    lis2=[]
    for s in both:
        #print (s+' : '+str(dic1[s])+str(dic2[s]))
        for pos1 in dic1[s]:
            for pos2 in dic2[s]:
                lis1.append(pos1)
                lis2.append(pos2)
    return lis1,lis2

def fetch_genbank(sid):
    try:
        handle = ExPASy.get_sprot_raw(sid)
        seq = SeqIO.read(handle,'swiss')
        SeqIO.write(seq, sid+'.genbank','genbank')
        print(sid,'sequence length',len(seq))
    except Exception:
        print (sid,'not found')

def read_genbank(fname):
    f = open(fname)
    for p in SeqIO.parse(f,'genbank'):
        break
    f.close()
    return p.annotations['organism'],str(p.seq)    

def plot(x,y,labelx,labely,w):
    plt.figure()
    plt.plot(x,y,'o')
    plt.xlabel(labelx)
    plt.ylabel(labely)
    plt.title('Dot plot with window size '+str(w))   

  
####
#Test out the procedure using the Shakespeare lines
####

l1 = 'My care is loss of care, by old care done'
l2 = 'Your care is gain of care, by new care won'

x,y = match(l1,l2,5)
print('check step using Shakespear lines:', list(zip(x,y)))
plot(x, y, l1, l2, 5)



####
#Carry out procedure for ATP synthase subunit a in different animals
####

sids = ['P00846','Q95A26','Q9T9W0','Q2I3G9','Q9TA24']#ATPase
#generate genbank files
for sid in sids:
    fetch_genbank(sid)

w = 10
tot_dots = 0
for i in range(len(sids)):
    for j in range(i+1,len(sids)):
        sid1 = sids[i]
        anim1, seq1 = read_genbank(sid1+'.genbank')
        sid2 = sids[j]
        anim2, seq2 = read_genbank(sid2+'.genbank')
        x,y = match(seq1,seq2,w)
        plot(x,y,anim1,anim2,w)
        #for autochecker
        print(anim1+' and '+anim2+':')
        print(len(x),'dots;', 'sorted(zip(y,x)[8]:',sorted(zip(x,y))[4])
        tot_dots += len(x)
        
print('total number of dots:',tot_dots)
plt.show()     

























