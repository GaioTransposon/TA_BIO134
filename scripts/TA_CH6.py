#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 19:07:47 2022

@author: dgaio
"""

# =============================================================================
# # The genetic code
# cdn = {}
# cdn['ttt'] = cdn['ttc'] = 'F phenylalanine'
# cdn['tta'] = cdn['ttg'] = 'L leucine'
# cdn['tct'] = cdn['tcc'] = cdn['tca'] = cdn['tcg'] = 'S serine'
# cdn['tat'] = cdn['tac'] = 'Y tyrosine'
# cdn['taa'] = cdn['tag'] = '* stop'
# cdn['tgt'] = cdn['tgc'] = 'C cysteine'
# cdn['tga'] = '* stop'
# cdn['tgg'] = 'W tryptophan'
# cdn['ctt'] = cdn['ctc'] = cdn['cta'] = cdn['ctg'] = 'L leucine'
# cdn['cct'] = cdn['ccc'] = cdn['cca'] = cdn['ccg'] = 'P proline'
# cdn['cat'] = cdn['cac'] = 'H histidine'
# cdn['caa'] = cdn['cag'] = 'Q glutamine'
# cdn['cgt'] = cdn['cgc'] = cdn['cga'] = cdn['cgg'] = 'R arginine'
# cdn['att'] = cdn['atc'] = cdn['ata'] = 'I isoleucine'
# cdn['atg'] = 'M methionine'
# cdn['act'] = cdn['acc'] = cdn['aca'] = cdn['acg'] = 'T threonine'
# cdn['aat'] = cdn['aac'] = 'N asparagine'
# cdn['aaa'] = cdn['aag'] = 'K lysine'
# cdn['agt'] = cdn['agc'] = 'S serine'
# cdn['aga'] = cdn['agg'] = 'R arginine'
# cdn['gtt'] = cdn['gtc'] = cdn['gta'] = cdn['gtg'] = 'V valine'
# cdn['gct'] = cdn['gcc'] = cdn['gca'] = cdn['gcg'] = 'A alanine'
# cdn['gat'] = cdn['gac'] = 'D aspartic acid'
# cdn['gaa'] = cdn['gag'] = 'E glutamic acid'
# cdn['ggt'] = cdn['ggc'] = cdn['gga'] = cdn['ggg'] = 'G glycine'
# 
# 
# # loop to access dictionary:
# for key, value in cdn.items():
#     print(key, ' : ', value[0])
#     
# 
# my_input = 'atgagtaaaggagaagaacttttcactggagttgttccaattcttgttgaattagatggt'
# my_list=[]
# for base in range(0, len(my_input), 3):
#     
#     my_codon = my_input[base:base+3]
# 
#     if my_codon in cdn:
#         
#         aminoacid = cdn[my_codon][0]
#         my_list.append(aminoacid)
#         
#     else:
#         print('codon does not exist in dictionary')
# 
# my_string = ''.join(my_list)
# print(my_string)
# =============================================================================

# =============================================================================
# # Exercise: Keys in dictionaries, part 1
# l = ['ediks', 29, 'adnec']
# d = {'adcen': 65, 'ikjna': 29, 'ediks': 73, 'zhdis': 76}
# 
# my_list =[]
# for item in l:
#     print(item)
#     
#     if item in d: 
#         my_list.append(1)
#         
#     else: 
#         my_list.append(0)
# 
# print(my_list)
# =============================================================================

# =============================================================================
# # Exercise: Keys in dictionaries, part 2
# l = ['nwnnnwwnnd', 'wdnndnnwwn', 45, 'nwwwnwnnnwd', 'dnwndddnw', 'nnnwdwdndd',
#      'ndnnwwnwnn', 'nwdnnnnnww', 'dnddwndnd', 'wwnwdnnwdw', 'dwndwnnnd', 17, 
#      'nwddwwnnnnw', 'nnwndwwddw', 'wnwnwnwnd', 'wdwwwnnnw', 'nnwnddnnw', 
#      'nwdnndwnww', 81, 'wnwwwwwnnnw', 'nwndnnnnnww', 31]
# d = {'wnwwwwwnnnw': 48, 'nwndnnnnnww': 97, 'nnwdwdddnw': 63, 'nwndnnnnww': 45,
#      'nwdnndnwnww': 39, 'nnwndddnnw': 82, 'wdnndnnwwn': 11, 'nnnwwwwnwdn': 31, 
#      'dnwwwnnddw': 66, 'wnwnwnwnd': 89, 'dwdwwdnndww': 17, 'nnwnddnwnww': 80, 
#      'dndwwnwwwwd': 94, 'nwwdnnwnd': 88, 'nwnnnwwnnd': 58, 'ndnwwnwwwd': 4, 
#      'nwnwdwdnw': 45, 'nwwwnwnnnwd': 70, 'wdnnwnndnnd': 95, 'ndnddnwwwwn': 45, 
#      'nwdnndddwd': 7, 'nwdnnnnnww': 5, 'nnwwnddnnwn': 45, 'nndwdnwwwwd': 29, 
#      'nnwwdwddnww': 17, 'wnnwnnwnn': 24, 'dnwndddnw': 99, 'wwdnwwwndn': 36, 
#      'wwwwwnndwn': 31, 'nwdnndwnww': 43, 'nwnndwwwwnd': 9, 'wdwwnnnnw': 71}
# 
# my_list =[]
# for item in l:
#     print(item)
#     
#     if item in d: 
#         my_list.append(1)
#         
#     else: 
#         my_list.append(0)
# 
# print(my_list)
# =============================================================================

# =============================================================================
# # Exercise: Creating dictionaries 1 (5)
# births = [['darwin','12 February 1809'],['shakespeare','26 April 1564'],\
#           ['cervantes','29 September 1547'],['lincoln','12 February 1809']]
# 
# dicts = {}
# for i in births:
#     key=i[1]
#     value=i[0]
#     if key not in dicts:
#         dicts[key] = [value]
#     else: 
#         dicts[key].append(value)
# print(dicts)
# 
# 
# # Method using zip and dict functions: 
# names=[]
# dates=[]
# for key,value in births:
#     
#     names.append(key)
#     dates.append(value)
#     
# zip_iterator = zip(names, dates) 
# a_dictionary = dict(zip_iterator) 
# print(a_dictionary)
# =============================================================================

# =============================================================================
# # Exercise: Creating dictionaries 2 (5)
# births = [['darwin','12 February 1809'],['shakespeare','26 April 1564'],\
#           ['cervantes','29 September 1547'],['lincoln','12 February 1809']]
# 
# from collections import defaultdict
# 
# names=[]
# dates=[]
# for key,value in births:
#     names.append(key)
#     dates.append(value)
# 
# d = defaultdict(list)
# for key, value in zip(dates, names):
#     d[key].append(value)
# 
# print(dict(d))
# =============================================================================

# =============================================================================
# # Exercise: Creating dictionaries 3 (5)
# person = {}
# person['darwin'] = 'Charles Darwin'
# person['shakespeare'] = 'William Shakespeare'
# person['cervantes'] = 'Miguel de Cervantes'
# person['lincoln'] = 'Abraham Lincoln'
# 
# dicts2 = {}
# for key in person:
#     dicts2[person[key]] = [key]
#     
# print(dicts2)
# =============================================================================

# =============================================================================
# # Referring to values in a list within a dictionary
# d = {'Paul': ['Meier', 20], 'Julia': ['Leutenegger', 23], 'Daniel': ['Brunner', 21]}
# print(d['Paul'][1])
# =============================================================================

# =============================================================================
# #Exercise: Creating dictionaries 4 (5)
# person = {}
# 
# person['darwin'] = ['Charles Darwin',
#                     '12 February 1809','19 April 1882']
# person['shakespeare'] = ['William Shakespeare',
#                     '26 April 1564','23 April 1616']
# person['cervantes'] = ['Miguel de Cervantes',
#                     '29 September 1547','23 April 1616']
# person['lincoln'] = ['Abraham Lincoln',
#                     '12 February 1809','15 April 1865']
# long=[]
# short=[]
# born=[]
# dead=[]
# for key in person:
#     short.append(key)
#     long.append(person[key][0])
#     born.append(person[key][1])
#     dead.append(person[key][2])
# 
# from collections import defaultdict
# d = defaultdict(list)
# for key, value in zip(dead, short):
#     d[key].append(value)
# 
# print(dict(d))
# =============================================================================

# =============================================================================
# # Exercise: Creating dictionaries 5 (5)
# person = {}
# 
# person['darwin'] = ['Charles Darwin',
#                     '12 February 1809','19 April 1882']
# person['shakespeare'] = ['William Shakespeare',
#                     '26 April 1564','23 April 1616']
# person['cervantes'] = ['Miguel de Cervantes',
#                     '29 September 1547','23 April 1616']
# person['lincoln'] = ['Abraham Lincoln',
#                     '12 February 1809','15 April 1865']
# 
# 
# person2={}
# for a in person:
#     #print(a) #short_name
#     #print(person[a][0]) # long_name
#     #print(person[a][1]) # birth
#     #print(person[a][2]) # death
#     
#     if person[a][2] not in person2:
#         #print('yes')
#         person2[person[a][2]]=[person[a][0]]
#     else: 
#         #print('nopes')
#         person2[person[a][2]].append(person[a][0])
#         
# print(person2)
# 
# # =============================================================================
# # # code using lists, defaultdict function and zip function: 
# # long=[]
# # short=[]
# # born=[]
# # dead=[]
# # for key in person:
# #     short.append(key)
# #     long.append(person[key][0])
# #     born.append(person[key][1])
# #     dead.append(person[key][2])
# # 
# # from collections import defaultdict
# # d = defaultdict(list)
# # for key, value in zip(dead, long):
# #     d[key].append(value)
# # 
# # print(dict(d))
# # =============================================================================
# =============================================================================


# =============================================================================
# # Reverse genetic code
# cdn = {}
# cdn['ttt'] = cdn['ttc'] = 'F phenylalanine'
# cdn['tta'] = cdn['ttg'] = 'L leucine'
# cdn['tct'] = cdn['tcc'] = cdn['tca'] = cdn['tcg'] = 'S serine'
# cdn['tat'] = cdn['tac'] = 'Y tyrosine'
# cdn['taa'] = cdn['tag'] = '* stop'
# cdn['tgt'] = cdn['tgc'] = 'C cysteine'
# cdn['tga'] = '* stop'
# cdn['tgg'] = 'W tryptophan'
# cdn['ctt'] = cdn['ctc'] = cdn['cta'] = cdn['ctg'] = 'L leucine'
# cdn['cct'] = cdn['ccc'] = cdn['cca'] = cdn['ccg'] = 'P proline'
# cdn['cat'] = cdn['cac'] = 'H histidine'
# cdn['caa'] = cdn['cag'] = 'Q glutamine'
# cdn['cgt'] = cdn['cgc'] = cdn['cga'] = cdn['cgg'] = 'R arginine'
# cdn['att'] = cdn['atc'] = cdn['ata'] = 'I isoleucine'
# cdn['atg'] = 'M methionine'
# cdn['act'] = cdn['acc'] = cdn['aca'] = cdn['acg'] = 'T threonine'
# cdn['aat'] = cdn['aac'] = 'N asparagine'
# cdn['aaa'] = cdn['aag'] = 'K lysine'
# cdn['agt'] = cdn['agc'] = 'S serine'
# cdn['aga'] = cdn['agg'] = 'R arginine'
# cdn['gtt'] = cdn['gtc'] = cdn['gta'] = cdn['gtg'] = 'V valine'
# cdn['gct'] = cdn['gcc'] = cdn['gca'] = cdn['gcg'] = 'A alanine'
# cdn['gat'] = cdn['gac'] = 'D aspartic acid'
# cdn['gaa'] = cdn['gag'] = 'E glutamic acid'
# cdn['ggt'] = cdn['ggc'] = cdn['gga'] = cdn['ggg'] = 'G glycine'
# 
# #print(cdn)
# 
# new={}
# for a in cdn: 
#     #print(a, cdn[a])
#     
#     long=cdn[a]
# 
#     
#     if long not in new:
#         new[long]=[a]
#     else: 
#         new[long].append(a)
# print(new)
# 
# =============================================================================
# =============================================================================
# # Exercise: Creating strings
# s = 'ztvnenejsncejajdncalkjalymmxndjfbfbvsjdlfjbbaldkjfnlaqeqwqwplnnnel'
# # Print a new string that contains character 0,1,4,5,8,9,12,13
# empty_list = []
# for ss in range(0,len(s),4):
#     
#     empty_list.append(s[ss])
#     empty_list.append(s[ss+1])
# 
# z = "".join(empty_list)
# print(z)
# =============================================================================

# =============================================================================
# s = 'This dog'
# 
# for c in 'aeiou':
#     s=s.replace(c,'-')
# print(s)
# 
# s = 'I am shocked shocked to hear about this'
# 
# t=s.split('shocked')
# print(t)
# 
# u=s.partition('shocked')
# print(u)
# =============================================================================

# # A riddle
# fyle = open('/Users/dgaio/Downloads/riddle.txt')
# all_text_in_string = fyle.read()
# fyle.close()

# # example
# #s = 'I am ***** shocked ##### hear about this'

# # actual string to edit:
# s = all_text_in_string
# #print(s)
# t=s.split('*****')
# #print(t)
# tt = t[1]
# #print(tt)

# u=tt.partition('#####')
# #print(u)
# interesting = u[0]

# import re
# s = re.sub(r'\W+', '', interesting)
# s=s.replace('_', '')
# print(s)

# =============================================================================
# # Number formatting
# from numpy import pi
# p = int(10**4 * pi)
# print('{:d} is an integer'.format(p))
# # 31415 is an integer
# 
# print('{:08d} is an integer'.format(p))
# # 00031415 is an integer
# 
# print('{:f} is a float'.format(pi))
# # 3.141593 is a float
# 
# print('{:015.11f} is a float'.format(pi))
# # 003.14159265359 is a float
# 
# print('{:e} is a float in exp notation'.format(pi))
# # 3.141593e+00 is a float in exp notation
# 
# print('{:019.11e} is a float in exp notation'.format(pi))
# # 3.14159265359e+00 is a float in exp notation
# =============================================================================

# =============================================================================
# # String formatting
# # Exercise: Rewriting strings
# l = "FqrpZcUBhvaOmPoyuBCGIVGtmKAufJXfvaLFroTgnrpmmPbbWNdGIcXGpqjlaNBdIUPgMQnHTm"
# 
# my_list = [l[x:x+5] for x in range(0, len(l),5)]
# my_list2=[]
# 
# for n in my_list:
#     
#     my_index=l.index(n)
#     
#     if (my_index % 2) == 0:
#         upp = n.upper()
#         my_list2.append(upp)
#     else:
#         low = n.lower()
#         my_list2.append(low)
#         
# my_list3 = ''.join(my_list2)
# my_len = len(my_list3)
# my_list4 = my_list3 + ' '*8
# result = f'{my_list4}{my_len}'
# print(result)
# =============================================================================








