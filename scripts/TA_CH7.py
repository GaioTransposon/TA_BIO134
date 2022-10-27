#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 10:58:51 2022

@author: dgaio
"""

# =============================================================================
# # Exercise: writing a function
# l = [5.75, 5.37, 2.45, 8.22, 7.45, 1.89, 3.82, 2.49]
# 
# def average(my_list):
#     
#     counter=0
#     my_sum=0
#     for item in my_list:
#         counter+=1
#         my_sum=my_sum+item
#     my_avg=my_sum/counter        
#     return(my_avg)
# 
# m = average(l)
# print(m)
# =============================================================================

# =============================================================================
# # Exercise: returning more than one variable
# l = [5.75, 5.37, 2.45, 8.22, 7.45, 1.89, 3.82, 2.49]
# 
# def sum_average(my_list):
#     
#     counter=0
#     my_sum=0
#     for item in my_list:
#         counter+=1
#         my_sum=my_sum+item
#     my_avg=my_sum/counter        
#     return(my_sum, my_avg)
# 
# summe, mean = sum_average(l)
# print(int(summe * mean))
# =============================================================================

# =============================================================================
# # Exercise: function and printing
# 
# def test_square(a,b):
#     
#     aa = a**2
#     bb = b
#     
#     if aa < bb:
#         c='The square of {} is smaller than {}'.format(a, b)
#     
#     else:
#         c='The square of {} is not smaller than {}'.format(a, b)
#         
#     return(c)
# 
# 
# d=test_square(4, 17)
# print(d)
# 
# d=test_square(4, 16)
# print(d)
# =============================================================================


# =============================================================================
# # Refactoring 1
# # Adjust the code for the proteomics exercise in such a way 
# # that it uses a function to create the initial lists with 
# # all biosequence names for a tissue.
# brain = open('/Users/danielagaio/Downloads/proteomics/human_brain_proteins.csv')
# plasma = open('/Users/danielagaio/Downloads/proteomics/human_plasma_proteins.csv')
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
# brain_IDs = get_IDs(brain_lines)
# plasma_IDs = get_IDs(plasma_lines)
# =============================================================================


# =============================================================================
# # Refactoring 2
# # Adjust the code further such that it contains a function 
# # that takes two file names as an input and returns the 
# # three lists with common and unique proteins as output. 
# # A function can only return one output variable, 
# # which can be dealt with by creating a tuple containing 
# # the three lists. Note that it is possible to call a function 
# # from within another function.
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
# def proteome_function(file_brain, file_plasma):
#     
#     all_lists=[]
#     
#     brain = open(file_brain)
#     plasma = open(file_plasma)
#     
#     brain_lines = brain.readlines()[1:]
#     plasma_lines = plasma.readlines()[1:]
# 
#     brain_IDs = get_IDs(brain_lines)
#     plasma_IDs = get_IDs(plasma_lines)
#     
#     
#     only_brain = list(set(brain_IDs) - set(plasma_IDs))
#     only_brain.sort()
#     
#     only_plasma = list(set(plasma_IDs) - set(brain_IDs))
#     only_plasma.sort()
#     
#     both = list(set(brain_IDs).intersection(plasma_IDs))
#     both.sort()
#     
#     all_lists = [only_brain, only_plasma, both]
#     
#     my_tuple=tuple(all_lists)
#     return(my_tuple)
#     
# 
# a= '/Users/danielagaio/Downloads/proteomics/human_brain_proteins.csv'
# b='/Users/danielagaio/Downloads/proteomics/human_plasma_proteins.csv'
# c=proteome_function(a,b)
# print(c)
# print(type(c))
# =============================================================================


# =============================================================================
# # Exercise: Genbank to fasta - function
# my_dir='/Users/dgaio/cloudstor/Gaio/github/TA_BIO134/source_data/'
# 
# def gen_to_fasta(my_file):
#     
# 
#     # Making the header for the fasta file:
#     global my_dir 
#     file_with_path=my_dir+my_file
# 
#     f = open(file_with_path)
#     f_lines = f.readlines()
#     #return(f_lines[0])
# 
# 
#     # get gene name from file name: 
#     x = my_file.split('.')
#     gene_name=x[0]
#     #return(gene_name)
# 
#     second_line = f_lines[1]
#     second_line = second_line.split()
#     second_line=second_line[1:len(second_line)]
#     second_line=' '.join(second_line)
#     #return(second_line)
# 
#     out='>' + gene_name + ' ' + second_line + ';'
#     #return(out)
# 
#     # to get aminoacids lines and excluding the other lines: 
#     my_list=[]
#     for fi in f_lines:
# 
#         fi=fi.strip()
#         fi=fi.split()
#         
#         if fi[0].isdigit():
#             my_list.append(fi)
#             
#             
#         new_list=[]
#         for item in my_list:
#             
#             item[0]=' ' # replace digits with empty space
#             joined=''.join(item) # join elements of list into single string
#             joined=joined.strip() # get rid of leftover space 
#             joined=joined.upper() # make to uppercase/capitalization of aminoacids 
#             new_list.append(joined)
#     #return(new_list)   
#      
#     # pre-pend header to list
#     new_list.insert(0, out)
#     
#     # writing file, line by line: 
#     output_file_name=my_dir+gene_name+'.fasta.txt'
#     with open(output_file_name, 'w') as fp:
#         for item in new_list:
#             # write each item on a new line
#             fp.write("%s\n" % item)
#         print('Done')
# 
#     #return(new_list)       
# 
# 
# # executing function:
# return_object=gen_to_fasta('P42677.genbank.txt')
# print(return_object)
# =============================================================================

# =============================================================================
# # Exercise: Fasta to genbank - function
# # write a function: 
#     # input=fasta
#     # output=genbank
# # rules: 
#     # ONE line before "ORIGIN" (ORIGIN should be second line)
#     # the rest: line number + 60 aminoacids (groups of 10)
#     # aminoacids must be lowercase 
#     # 8 spaces on the left before amino acids (digit included)
# 
# my_dir='/Users/dgaio/cloudstor/Gaio/github/TA_BIO134/source_data/'
# 
# def fasta_to_genbank(my_fasta):
#     
#     global my_dir 
#     file_with_path=my_dir+my_fasta
# 
#     f = open(file_with_path)
#     f_lines = f.readlines()
#     #return(f_lines[0])
# 
#     # get gene name from file name: 
#     x = my_fasta.split('.')
#     gene_name=x[0]
#     #return(gene_name)
#     
#     # body: 
#     header=f_lines[0]
#     second_line='.\n'
#     third_line='ORIGIN\n'
#     last_line='//'
#     
#     # amino acid sequence: 
#     aa_list=[]
#     for aa_line in f_lines[1:len(f_lines)]: # to avoid taking the header along
#         #print(aa_line)
#         #print(len(aa_line)) # it shows that there is not just 60 aa per line, it varies
#         aa_line=aa_line.strip()
#         aa_list.append(aa_line)
# 
#     # join lines of aminoacids 
#     aa_list=''.join(aa_list)
#     #return(aa_list)
# 
#     # split in groups of n=10 amino acids: 
#     split_aa = []
#     for i in range(0, len(aa_list), 10):
#         split_aa.append(aa_list[i : i + 10])
#     #return(split_aa)
# 
#     # split in groups of 6: 
#     split_aa_groups=[]
#     for groups in range(0, len(split_aa), 6):
#         split_aa_groups.append(split_aa[groups : groups + 6])
#     #return(split_aa_groups)
# 
#     # prepare the digits here: 
#     my_digits=[]
#     for i in range(0,len(aa_list),60):
#         my_digits.append(i+1)
# 
# 
#     # pre-pend the digits ! 
#     for num,item in enumerate(split_aa_groups):
#         x=str(my_digits[num])
#         item.insert(0, x)
#         #print(item)
#         
# 
#     new_aa_groups=[]
#     for item in split_aa_groups:
#         joined=' '.join(item) # join elements of list 
#         joined=joined.lower() # make to uppercase/capitalization of aminoacids 
#         new_aa_groups.append(joined)
#     #return(new_aa_groups)
# 
# 
#     # pre-pend:
#     new_aa_groups.insert(0, third_line)
#     new_aa_groups.insert(0, second_line)
#     new_aa_groups.insert(0, header)
# 
# 
#     # append:
#     new_aa_groups.append(last_line)
#         
# 
#     # writing file, line by line: 
#     output_file_name=my_dir+gene_name+'.genbank.txt'
#     with open(output_file_name, 'w') as fp:
#         for item in new_aa_groups:
#             # write each item on a new line
#             fp.write("%s\n" % item)
#         print('Done')    
#         
#     return(new_aa_groups)
# 
# 
# # executing function:
# return_object=fasta_to_genbank('Q9NSA3.fasta.txt')
# print(return_object)
# 
# 
# # Maria's code: 
# def fasta_to_genbank(sid):
#     fyle_fasta = open(sid + '.fasta.txt')
#     fyle_genbank = open(sid + '.genbank.txt', 'w')
#     list_fasta = fyle_fasta.readlines()[1:]
#     s = 'dummy header\nORIGIN\n'
#     number = 1
#     for line in list_fasta:
#         line = line.strip().lower()
#         s += '{:9d}'.format(number)
#         for i in range(0, 60, 10):
#             if len(line[i:i+10])>0:
#                 s += ' '+line[i:i+10]
#         s += '\n'
#         number += 60
#     s += '//'
#     print(s)
#     fyle_genbank.write(s)
#     fyle_fasta.close()
#     fyle_genbank.close()
# 
# fasta_to_genbank('B4F440')
# 
# =============================================================================
  
# =============================================================================
# # Exercises: Standard deviation and Standard error
# 
# # average function
# def average(my_list):
#     
#     counter=0
#     my_sum=0
#     for item in my_list:
#         counter+=1
#         my_sum=my_sum+item
#     my_avg=my_sum/counter        
#     return(my_avg)
# 
# # standard deviation function
# def standarddev(a_list):
#     t=[]
#     sum_dist=0
#     counter=0
#     for i in a_list:
#         
#         # Step 1: Find the mean.
#         ave=average(a_list)
#         
#         # Step 2: For each data point, find the square of its distance to the mean.
#         dist=(i-ave)**2
# 
#         # Step 3. Calculate the mean of the squared differences. This is the sample variance. 
#         sum_dist=sum_dist+dist
# 
#         # Step 4: Divide by the number of data points minus 1.
#         n=len(a_list)
#         almost=sum_dist/(n-1)
#     
#         # Step 5: Take the square root.
#         s=almost**0.5
#         
#     return(s)
# 
# # standard error function
# # The standard error of the mean is the standard deviation 
# # divided by the square root of the number of measurements.
# def SE(b_list):
#     
#     sd=standarddev(b_list)
#     n=len(b_list)
#     n_square=n**0.5
#     
#     se=sd/n_square
#     
#     return(se)
#     
# 
# l = [5.75, 5.37, 2.45, 8.22, 7.45, 1.89, 3.82, 2.49]
# 
# x=SE(l)
# print(x)
# =============================================================================









