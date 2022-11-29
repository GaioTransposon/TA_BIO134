#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 20:24:47 2022

@author: danielagaio
"""

# Exercise on array indexing

import numpy as np
    
a=np.array([3,5,2,5,6,2])
b=np.array([8,4,1,7,6,8])
for i in range(len(a)):   # 0 1 2 3 4 5 
    #print(b[i])          # 8 4 1 7 6 8 
    #print(a[i])          # 3 5 2 5 6 2 
    if b[i]>=a[i]:        # y n n y y y 
        a[i]+=2           # 5     7 8 4
print(a, 'is a after change ')

#for i in range(len(a)):   # 0 1 2 3 4 5 
    #print(b[i])          # 8 4 1 7 6 8 
    #print(a[i])          # 3 5 2 5 6 2 

a=np.array([3,5,2,5,6,2])
b=np.array([8,4,1,7,6,8])
print(a, 'is a orginal')
print(b, 'is b original')
print(a[a<=b]+2)




#####
# Colored shapes
import matplotlib.pyplot as plt
from numpy import array
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection

triangle_positions = [[0,0],[0.3,0.3],[0.5,0.1]]
quadrilateral_positions = [[0.5,0.1],[0.3,0.3],[0.6,0.5],[0.8,0.4]]
pentagon_positions =[[0.6,0],[0.5,0.1],[0.8,0.4],[0.9,0.3],[0.7,0.02]]

polygs = []
polygs.append(Polygon(triangle_positions))
polygs.append(Polygon(quadrilateral_positions))
polygs.append(Polygon(pentagon_positions))
patches = PatchCollection(polygs)
patches.set_cmap('jet')
patches.set_array(array([1,3,2.5])) #for colors

fig=plt.figure()
panel=plt.gca()
panel.add_collection(patches)
fig.colorbar(patches)
panel.autoscale(True)
panel.set_aspect('equal')
plt.show()
#####
# Color maps 1 (2)
# Try out what the above code does. 
# How can line 15, 'patches.set_array(array([1,3,2.5]))', 
# be altered to draw a red triangle, an orange quadrilateral 
# and a blue pentagon?
# patches.set_array(array([3,2.5,1])) #for colors
# fig=plt.figure()
# panel=plt.gca()
# panel.add_collection(patches)
# fig.colorbar(patches)
# panel.autoscale(True)
# panel.set_aspect('equal')
# plt.show()
#####
# Color maps 2 (2)
# patches.set_array(array([1,1,1])) # all blue
# patches.set_array(array([2.5,2.5,2.5])) # all orange
# patches.set_array(array([3,2,1])) # 3 is red, 2 is green, 1 is blue

# fig=plt.figure()
# panel=plt.gca()
# panel.add_collection(patches)
# fig.colorbar(patches)
# panel.autoscale(True)
# panel.set_aspect('equal')
# plt.show()
#####
# Cell polygons
# Data format: question 3 (3)
# Which value would VP[CV[1][3]][0] have if CV and VP are in list form?
# CV[1]    2.4 7.0
# CV[3]    6.3 7.0
# CV[0]    0.8 5.5
# [[2.4,7.0],[6.3,7.0],[0.8,5,5]]
#####
# Download data: 
import os
home = os.path.expanduser( '~' )
cv = home+"/Downloads/wingdisc/wd-large/cv.txt"
    
cv = open(cv)
cv_lines = cv.readlines()
cv.close()

vp = home+"/Downloads/wingdisc/wd-large/vp.txt"
    
vp = open(vp)
vp_lines = vp.readlines()
vp.close()

# how many vertices does the first cell have?
print(cv_lines[0])
# how many vertices does the last cell have?
print(cv_lines[-1])
# y-coordinate of first vertex? 
print(vp_lines[0])
#####
# Making lists for Vertices positions (vp) and Cell vertices (cv)

# Vertices positions 
my_vp=[]
for i in vp_lines: 
    inner=[]
    i=i.split()
    x=float(i[0])
    y=float(i[1])
    inner.append(x)
    inner.append(y)
    my_vp.append(inner)
print(my_vp)

# Cell vertices 
my_cv=[]
for i in cv_lines: 
    inner=[]
    i=i.split()
    for j in i: 
        j=int(j)
        inner.append(j)
    my_cv.append(inner)
print(my_cv)
#####
# Getting the data in a useful format
# Determine the x,y-positions of the vertices of all cells (µm). 
# Create two lists of lists, one with the x-positions for each of the cells 
# and another one for the y-positions. 
for i in my_cv[0]:
    print(i, my_vp[i])
#####
# Warm-up for data format wing disc

x_positions = [4.6, 4.5, 9.1, 2.2, 6.2, 7.6, 5.4, 9.3, 2.5, 2.6, 7.1, 
               8.9, 4.2, 3.1, 6.2, 1.4, 2.9, 9.7, 3.5, 5.2, 1.1, 9.3]
vertex_numbers = [2, 4, 11, 16, 18]

# Calculate the product of the values in x_positions at the positions given 
# by vertex_numbers. Thus, for the above example, 
# the outcome should be 9.0 (= 1.2*5.0*1.5).

out=1
for i in vertex_numbers:
    out=out*x_positions[i]
print(out)
#####
# Cell areas and centroids
# A_formula= abs(1/2 * (x1*(y2-y3) + \     x1*y2 - x1*y3
#                       x2*(y3-y1) + \     x2*y3 - x2*y1
#                       x3*(y1-y2)))       x3*y1 - x3*y2

# [1,1],[2,3],[4,2]
A = abs(1/2 * (1*(3-2) + 2*(2-1) + 4*(1-3)))

A = abs(1/2 * ((1*3-1*2)+(2*2-2*1)+(4*1-4*3)))
A

A1=(1*3 + 2*2 + 4*1)
A2=(1*2  +  3*4  +  2*1)
abs(A1-A2)/2


#####
# Wing disc: cell areas

x_list=[1,2,4]
y_list=[1,3,2]

def make_combos(l):
    l2=[]
    for i in l:
        for j in l:
            if j!=i:
                x = [j,i]
                x_inv = [i,j]
                if x_inv not in l2:
                    l2.append(x)
    return l2
    
out = make_combos(y_list)
print(out)
            
for i,j in enumerate(x_list):
    for k,l in enumerate(x_list):
        print(i, k)

def get_area(x_list,y_list):
    polygon_n=len(x_list)
    
    combos=make_combos(y_list)
    
    to_sum=0
    for yn,y in enumerate(combos):        
        print(x_list[yn], y, x_list[yn]*y[1], x_list[yn]*y[0], x_list[yn]*y[0]-x_list[yn]*y[1])

        print(x_list[yn]*y[1]-x_list[yn]*y[0])
        

            

            
    
    
    
    
    



# =============================================================================
# my_vp
# my_cv
# print(len(my_vp))
# print(len(my_cv))
# my_dict={}
# 
# counter=0
# for cell in my_cv:
#     counter+=1
#     print(counter,cell)
#     sub_dict={}
#     for i in cell:
#         print(i)
#         sub_dict[i]=[my_vp[i][0]]
#         sub_dict[i].append(my_vp[i][1])
#         print(sub_dict)
#     my_dict[counter]=sub_dict
#     
# print(my_dict)
# 
# for a in my_dict:
#     for b in my_dict[a]:
#         print(a,b, my_dict[a][b])
#         
# my_x=[]
# my_y=[]
# for a in my_vp:
#     print(a)
#     
#     
#     x=float(a[0])
#     y=float(a[1])
#     my_x.append(x)
#     my_y.append(y)
# =============================================================================
    

        





import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection

def get_list(filename, number_type):
    file = open(filename, 'r')
    full = file.readlines()
    file.close()
    lyst = []
    for i, lyne in enumerate(full):
        l = []
        for s in lyne.split():
            if number_type == 'f':
                v = float(s)
            elif number_type == 'i':    
                v = int(s)
            l.append(v)
        lyst.append(l)
    return lyst

def cell_positions(cv, vp, p):
    cp=[]
    for i, c in enumerate(cv):
        cp.append([])
        for v in c:
            if p == 'x':
                cp[i].append(vp[v][0])
            else:
                cp[i].append(vp[v][1])
    return cp
    
def area(cpx, cpy):
    a = len(cpy) * [0]
    for i in range(len(cpy)):
        for j in range(len(cpy[i])):
            a[i] += cpx[i][j] * cpy[i][j-1] - cpx[i][j-1] * cpy[i][j]
        a[i] = a[i] * 0.5
    return np.array(a)
    
def centroid(cpx, cpy, area):
    xcenter = len(cpy) * [0]
    ycenter = len(cpy) * [0]
    for i in range(len(cpy)):
        for j in range(len(cpy[i])):
            xcenter[i] += (cpx[i][j] + cpx[i][j-1]) * (cpx[i][j] * cpy[i][j-1]\
                          -cpy[i][j] * cpx[i][j-1]) / (6 * area[i])
            ycenter[i] += (cpy[i][j] + cpy[i][j-1]) * (cpx[i][j] * cpy[i][j-1]\
                          -cpy[i][j] * cpx[i][j-1]) / (6 * area[i])
    return np.array(xcenter),np.array(ycenter)

def distance_center(xcenter, ycenter):
    dist_cent=(xcenter**2 + ycenter**2)**0.5
    return dist_cent

def plotting(x, y, afit, bfit, size):
    plt.figure()
    plt.plot(x,y,'.')
    x0 = min(x)
    x1 = max(x)
    y0 = afit * x0 + bfit
    y1 = afit * x1 + bfit
    plt.plot([x0,x1],[y0,y1], label = 'linear fit: y = {:.3f}*x + {:.3f}'.format(afit, bfit))
    plt.title('Cell area distribution in the '+size+' wing disc')
    plt.xlabel('Distance to the center of the disc')
    plt.ylabel('Cell area (um2)')
    plt.legend()
    
def statistical_test(areas, dist_center):
    (afit, bfit) = np.polyfit(dist_center, areas, 1)
    dmax = max(dist_center)
    (t,Pt) = scipy.stats.ttest_ind(areas[dist_center<=0.5*dmax], areas[dist_center>0.5*dmax])# axis = None
    return afit, bfit, t, Pt
    
def draw_disc(cpx, cpy, area, size):  
    polygs = []
    for i in range(len(cpx)):
    	polyg = []
    	for j in range(len(cpx[i])):
    		polyg.append([cpx[i][j], cpy[i][j]])
    	polygs.append(Polygon(polyg))
    patches = PatchCollection(polygs)
    patches.set_cmap('jet')
    colors = 1 * area
    colors[colors>14] = 14 # color value for all the mitotic cells (area>14) is set to 14
    patches.set_array(np.array(colors)) #for colors

    fig = plt.figure()
    panel = fig.add_subplot(1,1,1)
    panel.add_collection(patches)
    color_bar = fig.colorbar(patches)
    color_bar.set_label('Cell area (um2)', rotation = 270, labelpad = 15)
    panel.set_xlim(-120, 110)
    panel.set_ylim(-85, 85)
    panel.set_aspect('equal')
    plt.title(size+' wing disc')

def analyze_disc(size):    
    cv = get_list(home+'/Downloads/wingdisc/wd-'+size+'/cv.txt', 'i')
    vp = get_list(home+'/Downloads/wingdisc/wd-'+size+'/vp.txt', 'f')
    cpx = cell_positions(cv, vp, 'x')
    cpy = cell_positions(cv, vp, 'y')
    areas = area(cpx, cpy)
    xcenter, ycenter = centroid(cpx, cpy, areas)
    dist_center = distance_center(xcenter, ycenter)
    afit, bfit, t, Pt = statistical_test(areas, dist_center)
    plotting(dist_center, areas, afit, bfit, size)
    draw_disc(cpx, cpy, areas, size)
    ans = cpx, cpy, areas, xcenter, ycenter, dist_center, afit, bfit, t, Pt
    return ans


cpx_l, cpy_l, area_l, xcenter_l, ycenter_l, dist_center_l, afit_l, bfit_l,t_l, Pt_l = analyze_disc('large')

print ('values for the large disc:')
print ('x-positions first cell in large disc:',cpx_l[0])
print ('y-positions first cell in large disc:',cpy_l[0])
print ('first two cell areas large disc:',area_l[:2])
print ('last area large disc:',area_l[-1])
print ('x-postion centroid first cell in large disc',xcenter_l[0])
print ('y-postion centroid first cell in large disc',ycenter_l[0])
print ('distance to disc center of first cell in large disc',dist_center_l[0])
print ('x-postion centroid first cell in large disc',xcenter_l[1])
print ('y-postion centroid first cell in large disc',ycenter_l[1])
print ('distance to disc center of first cell in large disc',dist_center_l[1])
print ('y-intercept fit distance-area large disc', bfit_l)
print ('slope fit distance-area large disc', afit_l)
print ('t-value large disc', t_l)
print ('t-test p-value large disc', Pt_l)
print ()


cpx_s,cpy_s,area_s,xcenter_s,ycenter_s,dist_center_s,afit_s,bfit_s,\
t_s,Pt_s=analyze_disc('small')
print ('values for the small disc:')
print ('y-intercept fit distance-area small disc', bfit_s)
print ('slope fit distance-area small disc', afit_s)
print ('t-value small disc', t_s)
print ('t-test p-value small disc', Pt_s)

plt.show()
    


        
        









































































