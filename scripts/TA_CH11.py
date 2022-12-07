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
print(a, 'is a orginal')
for i in range(len(a)):   # 0 1 2 3 4 5 
    #print(b[i])          # 8 4 1 7 6 8 
    #print(a[i])          # 3 5 2 5 6 2 
    if b[i]>=a[i]:        # y n n y y y 
        a[i]+=2           # 5     7 8 4
print(a, 'is a after change ')


a=np.array([3,5,2,5,6,2])
b=np.array([8,4,1,7,6,8])
print(a, 'is a orginal')
a[a<=b]+2 

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

# Download data

import os

def get_list(some_file):
    #transfer the data from the file into a list
    home = os.path.expanduser( '~' )
    cv_or_vp = home+some_file
    cv_or_vp=open(cv_or_vp)
    lines = cv_or_vp.readlines()
    
    my_list=[]
    for line in lines:
        line=line.strip()
        line=line.split()
        my_list.append(line)
        
    out=[]
    
    if all(len(sub) == 2 for sub in my_list): # then it's vertices
        # Vertices positions, x and y separate 
        for i in my_list: 
            x=float(i[0])
            y=float(i[1])
            xy=[x,y]
            out.append(xy)
        
    else: 
        # it's cell vertices, so parse as follows: 
        for i in my_list: 
            inner=[]
            for j in i: 
                j=int(j)
                inner.append(j)
            out.append(inner)
            
    return out 
  

vp=get_list("/Downloads/wingdisc/wd-large/vp.txt")
cv=get_list("/Downloads/wingdisc/wd-large/cv.txt")
   
# how many vertices does the first cell have?
print(cv[0])
# how many vertices does the last cell have?
print(cv[-1])
# y-coordinate of first vertex? 
print(vp[0])


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

# Determine the x,y-positions of the vertices of all cells (µm). 
# Create two lists of lists, one with the x-positions for each of the cells 
# and another one for the y-positions. 

def cell_positions(cv, vp, x_or_y):
    #get the x,y-positions of the vertices per cell
    cp=[]
    for i, c in enumerate(cv):
        cp.append([])
        for v in c:
            print(c)
            if x_or_y == 'x':
                cp[i].append(vp[v][0])
            else:
                cp[i].append(vp[v][1])
    return cp

x_list=cell_positions(cv,vp,'x')
y_list=cell_positions(cv,vp,'y')

##### 

#calculate cell areas
def polygonArea(my_x_list, my_y_list):
    
    area = 0.0
    
    n=len(my_x_list)

    j = n - 1
    for i in range(0,n):
        print(i)

        area += (my_x_list[j] + my_x_list[i]) * (my_y_list[j] - my_y_list[i])
        j = i   # j is previous vertex to i
    area=area/2
    
    return abs(area)

print("area of first cell is: ", polygonArea(x_list[0],y_list[0]))
print("area of second cell is: ", polygonArea(x_list[1],y_list[1]))
print("area of last cell is: ", polygonArea(x_list[-1],y_list[-1]))

##### 

import scipy

# Cell centroids and distance to centre (0,0)

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
    cv = get_list('wingdisc/wd-'+size+'/cv.txt', 'i')
    vp = get_list('wingdisc/wd-'+size+'/vp.txt', 'f')
    cpx = cell_positions(cv, vp, 'x')
    cpy = cell_positions(cv, vp, 'y')
    areas = polygonArea(cpx, cpy)
    xcenter, ycenter = centroid(cpx, cpy, areas)
    dist_center = distance_center(xcenter, ycenter)
    afit, bfit, t, Pt = statistical_test(areas, dist_center)
    plotting(dist_center, areas, afit, bfit, size)
    draw_disc(cpx, cpy, areas, size)
    ans = cpx, cpy, areas, xcenter, ycenter, dist_center, afit, bfit, t, Pt
    return ans


cpx_l, cpy_l, area_l, xcenter_l, ycenter_l, dist_center_l, afit_l, bfit_l,\
t_l, Pt_l = analyze_disc('large')
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