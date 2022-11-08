
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 13:10:39 2022

@author: dgaio
"""

my_dir='/Users/dgaio/cloudstor/Gaio/github/TA_BIO134/source_data/'


import numpy as np

# a simple array 
x = np.array(range(10))
print(x)
# [0 1 2 3 4 5 6 7 8 9]


print(len(x),x.shape)
# 10 (10,)

# Adding x to x, will "zip"/map all the values: 
y= x+x
print(y)
# [ 0  2  4  6  8 10 12 14 16 18]

# the operation will be applied to each elemnt of the array 
y=x/2
print(y)
# [0.  0.5 1.  1.5 2.  2.5 3.  3.5 4.  4.5]

# an array is numbers only. "False" will be "translated" to 0 
z=np.array([0,1,False])
print(z)
# [0 1 0]

# You can change single values of the array just like with a list
z[2] += 1
print(z)
# [0 1 1]

# but the value will be rounded if the numbers are integers
z[2] += 0.5
print(z)
# [0 1 1]

# unless you specify from the start that values are floats
z=1.0*z
print(z)
# [0. 1. 1.]
z[2] += 0.5
print(z)
# [0.  1.  1.5]

# a simple array x
x = np.array(range(10))
y=x
print(x)
print(y)
# [0 1 2 3 4 5 6 7 8 9]
# [0 1 2 3 4 5 6 7 8 9]

# as x and y are the same array, if you only change y, you also change x: 
y[1] = -1
print(x)
print(y)
# [ 0 -1  2  3  4  5  6  7  8  9]
# [ 0 -1  2  3  4  5  6  7  8  9]

# but if you copy x saying "y=1*x" then by changing y, you don't change x: 
x = np.array(range(10))
y=1*x
y[1]=-1
print(x)
print(y)

# another way to generate arrays (these are automatically floating points!)
y=np.linspace(0.0,9.0,100)   # both start and endpoint are included ! 
print(y)

# create arrays with more than one dimension.
xx = np.zeros(shape=(3,4),dtype=float)
print(xx)


##############################################################################
# Exercises on arrays (part 1)
# exercise: arrays 1(2)
a = [1, 2, 6, 4]
# multiply all elements by 2:
    
# using for loop: 
for i in range(len(a)):
    a[i] *= 2
print(a)

# using array: 
a = np.array([1, 2, 6, 4])
a=2*a
print(a)
##############################################################################
# exercise: arrays 2(2)
a = [3, 5, 2, 4, 3, 6] 

# using for loop: 
for i in range(1,4): # i    1,2,3
    print(i, a[i])   # a[i] 5,2,4    a[1]=5+10    a[2]=2+10     a[3]=4+10
    a[i] += 10
print(a)

# using array: 
a = np.array([3, 5, 2, 4, 3, 6])
a[1:4]+=10
print(a)
##############################################################################
# Exercise: array copies and synonyms (part 2)
x = np.array([4, 3, 1])
y = x     # x is [4 3 1]     y is [4 3 1]
z = 1*y   # z is: [4 3 1]
y[1] = 6  # y is: [4 6 1], also x , but not z 
z[2] = 7  # z is: [4 3 7]
print(x)
print(y)
print(z)
##############################################################################
# Exercise: data types in arrays
x = np.array([4, 3, 1])  # x is: [4 3 1]
y = 1.0 * x              # y is: [4. 3. 1.], but x did not change 
x[1] += 0.8              # x is: [4 3 1]     because they are integers, nothing after comma is added
y += 0.1                 # y is: [4.1 3.1 1.1]
print(x)
print(y)
##############################################################################
# Movie: Slicing multidimensional arrays
a = np.zeros([4,5])   # 4 is rows, 5 is cols
print(a)
# [[0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]]
a[3,1] = 3
a[2,3] = 2
a[0,2] = 4
a[1,2] = 5
print(a)
# [[0. 0. 4. 0. 0.]
#  [0. 0. 5. 0. 0.]
#  [0. 0. 0. 2. 0.]
#  [0. 3. 0. 0. 0.]]
a[2,:] += 3
print(a)
# [[0. 0. 4. 0. 0.]
#  [0. 0. 5. 0. 0.]
#  [3. 3. 3. 5. 3.]
#  [0. 3. 0. 0. 0.]]
b = 1 * a[:,1:3] + 1 * a[:,2:4]
print(b)
# [[4. 4.]
#  [5. 5.]
#  [6. 8.]
#  [3. 0.]]
##############################################################################
# Exercise: Slicing two-dimensional arrays
a = np.array([[1, 2, 6, 4],[9, 6, 6, 3],[3, 4, 7, 5],[3, 2, 1, 9],[3, 8, 7, 4]])
print(a)
# [[1 2 6 4]
#  [9 6 6 3]
#  [3 4 7 5]
#  [3 2 1 9]
#  [3 8 7 4]]
a[2:4,0:3]=0
print(a)
# [[1 2 6 4]
#  [9 6 6 3]
#  [0 0 0 5]
#  [0 0 0 9]
#  [3 8 7 4]]
##############################################################################
# Question on slicing arrays 1(2)
a = np.zeros([4,5])
a[3,1] = 3
a[2,3] = 2
a[0,2] = 4
a[1,2] = 5
print(a)
# [[0. 0. 4. 0. 0.]
#  [0. 0. 5. 0. 0.]
#  [0. 0. 0. 2. 0.]
#  [0. 3. 0. 0. 0.]]
b = a[:,1:3] + a[:,2:4]
print(b)
# [[4. 4.]
#  [5. 5.]
#  [0. 2.]
#  [3. 0.]]
# c = a[1:3,:-1] + a[:,1:3]
# print(c)
# ValueError: operands could not be broadcast together with shapes (2,4) (4,2) 
##############################################################################
# Question on slicing arrays 2(2)
a = np.zeros([4,5])
a[3,1] = 3
a[2,3] = 2
a[0,2] = 4
a[1,2] = 5
print(a)
# [[0. 0. 4. 0. 0.]
#  [0. 0. 5. 0. 0.]
#  [0. 0. 0. 2. 0.]
#  [0. 3. 0. 0. 0.]]
print(a[3,:-1])         # [0. 3. 0. 0.]
print(a[:,3])           # [0. 0. 2. 0.]
c = a[3,:-1] + a[:,3]   
print(c)                # [0. 3. 2. 0.]
##############################################################################
# MATPLOTLIB
import matplotlib 
import matplotlib.pyplot as pl
import matplotlib.image as img
h = img.imread(my_dir+'Haeckel.png')
#pl.imshow(h)
#pl.show()    # this must be the last line of code. until closed image, restof code won't run 
##############################################################################
# COLOR CHANNELS
print(type(h))
# <class 'numpy.ndarray'>
print(h.shape)
# (1031, 735, 3) vertical, horizontal, RGB channels 
print(type(h[0,0,0]))       # uint8 (0,255) or float32 (0.0,1.0)
# <class 'numpy.float32'>   # float goes from 0.0 to 1.0
print(h)
# uint8 (0,255) or float32 (0.0,1.0)
#isolate the channels. 
h[:,:,0] = 0        # 0 is red, set it to zero. 
#pl.imshow(h)
#pl.show()
h = img.imread(my_dir+'Haeckel.png')
h[:,:,1] = 0        # 1 is green, set it to zero. 
#pl.imshow(h)
#pl.show()
h = img.imread(my_dir+'Haeckel.png')
h[:,:,2] = 0        # 2 is blue, set it to zero. 
#pl.imshow(h)
#pl.show()
h = img.imread(my_dir+'Haeckel.png')
copy = 1*h
h[:,:,0] = copy[:,:,1]  # set the red channel; to what used to be the green channel 
h[:,:,1] = copy[:,:,2]  # set the green channel; to what used to be the blue channel 
h[:,:,2] = copy[:,:,0]  # set the blue channel; to what used to be the red channel 
#pl.imshow(h)
#pl.show()
# make color negatives: 
h = img.imread(my_dir+'Haeckel.png')
h=1-h   # red becomes anti-red , greens become magenta, blues becopme yellows 
#pl.imshow(h)
#pl.show()
##############################################################################
# SMOOTHING 
h = img.imread(my_dir+'Haeckel.png')
#pl.imshow(h)
h=h[150:400,30:420] # y-range (vertical) comes first: 150:400; 30:420 x range; 
#pl.imshow(h)
nsum=0*h     # array of the same size as h, but full of zeros 
P = h.shape[0]
Q = h.shape[1]
for s in range(5): # smoothing the image 5 times 
    for p in range(P-1):   # range(P)=0,249    range(P-1)=0,248
        for q in range(Q-1):   # range(P) is 0 to 249 ; range(P-1) is 0 to 248
            
            nsum[p,q] = h[p+1,q] + h[p-1,q] + h[p,q+1] + h[p,q-1]


    h = (h + nsum/4)/2
#pl.imshow(h)
#pl.show()
##############################################################################
# Creating Images
a=np.array([[[0,0,0],[0,0,0],[0,0,0]],[[1,0,0],[0,1,0],[0,0,1]],\
           [[1,1,0],[1,0,1],[0,1,1]],[[1,1,1],[0.5,0.5,0.5],\
           [1,1,1]]])
#matplotlib.image.imsave('dots.png', a)
#pl.imshow(a)
#pl.show()
# Alternatively, each pixel can also be described by only one value. 
# A colormap is then being used to show the image in pseudocolors:
b=np.array([[  0,  0,  0,  0,  0,  0,  0],\
            [  0,0.3,  0,  0,  0,0.3,  0],\
            [  0,  0,  0,0.8,  0,  0,  0],\
            [  0,  1,  0,  0,  0,  1,  0],\
            [  0,  0,  1,  1,  1,  0,  0],\
            [  0,  0,  0,  0,  0,  0,  0]])
#pl.imshow(b,cmap=pl.cm.jet)
#pl.show()
##############################################################################
# Exercise: image boundaries
h = img.imread(my_dir+'hotspring_pattern.jpg')
#print(len(h),h.shape) # 4080 (4080, 2987, 3)
#pl.imshow(h)
#pl.show()

# What is the mean blue value of the right boundary (= right-most) pixels? 
h_sub1 = h[:,2986:]   # rightmost part 
#print(len(h_sub1),h_sub1.shape)    # 4080 (4080, 1, 3)
#print(h_sub1)
#pl.imshow(h_sub1)
#pl.show(h_sub1)

keep_blue=[]
for i in h_sub1: 
    #print(i)
    for k in i: 
        keep_blue.append(k[2])
        #print(k[0])
        
#print(keep_blue)
print(len(keep_blue))
print(np.mean(keep_blue))   

# What is the mean red value of the pixels at the upper boundary?
h_sub2 = h[0:1,:]   # top part 
#print(len(h_sub2),h_sub2.shape)  # 1 (1, 2987, 3)
#pl.imshow(h_sub2)
#pl.show()

keep_red=[]
for i in h_sub2: 
    #print(i)
    for k in i: 
        keep_red.append(k[0])
        #print(k[2])
        
#print(keep_red)
#print(len(keep_red))
#print(np.mean(keep_red))   
##############################################################################
import matplotlib.pyplot as pl
import matplotlib.image as img

h = img.imread(my_dir+'Haeckel.png')

# print(h)   # will print the array
# print(h[0])    # will print the first row (all three colors given)
# print(h[0,0])    # will print just 1 pixel , first is y then it's x coordinate
# print(h[0,0,0]) # will give R channnel 
# print(h.shape)

print(h)
print('these are the RGB values for the whole first row',h[0])
print('these are the RGB values for the pixel at first row and first column',h[0,0])
print('these is the R channel value of that first pixel (first row first col) ',h[0,0,0])

# for i in h: 
#     print(i[0])  # red
#     print(i[1])  # blue
#     print(i[2])  # green
#     print(i[3])  # transparency
##############################################################################
# Smoothing: video 
import matplotlib.pyplot as pl
import matplotlib.image as img

h = img.imread(my_dir+'Haeckel.png')
#h=h[150:400,30:420]    # y range: 150 to 400; x range: 30 to 420

h=h[220:270,350:380]      # h[220:270,350:380]   
#pl.imshow(h)
#pl.show()

nsum=h*0
print(nsum)

R = h.shape[0]
C = h.shape[1]

for s in range(10):
    for r in range(1, R-1):       # which is is 1, 2 
        for c in range(1, C-1):   # which is is 1, 2 
            print(r,c,"c")        # al possibilities are: 1,1 ; 1,2 ; 2,1 ; 2,2
                                                    
            # sum of the neighbours of one pixel 
            nsum[r,c] = h[r+1,c] + h[r-1,c] + h[r,c+1] + h[r,c-1]
            # nsum[1,1] = h[2,1] + h[0,1] + h[1,2] + h[1,0]      # 1,1 
            # nsum[1,2] = h[2,2] + h[0,2] + h[1,3] + h[1,1]       # 1,2
            # nsum[2,1] = h[3,1] + h[1,1] + h[2,2] + h[2,0]       # 1,2
            # nsum[2,2] = h[3,2] + h[1,2] + h[2,3] + h[2,1]       # 2,2

    h = (h + nsum/4)/2

#pl.imshow(h)
#pl.show()
##############################################################################
# Exercise: smoothing
h = img.imread(my_dir+'stinkbug.png')
#pl.imshow(h)
#pl.show()
print(h)
new=h*1
R, C, color = h.shape
print(new)

for r in range(1, R-1):       # which is is 1, 2 
    for c in range(1, C-1):   # which is is 1, 2 
                                                
        # ave
        new[r,c] = (h[r-1,c+1] + h[r,c+1] + h[r+1,c+1]+\
               h[r-1,c] + h[r,c] + h[r+1,c] +\
               h[r-1,c-1] + h[r,c-1] + h[r+1,c-1])/9

print ('red boundary pixel 5,499:',new[5,499,0])
print ('green, position 181,260:', new[181,260,1])
print ('mean pixel value:',np.mean(new))
##############################################################################
 # Speed 
import time
start = time.time()
# do stuff here 
end = time.time()
print("The time passed is", end - start)
##############################################################################
# Plotting commands
import matplotlib.pyplot as pl
import numpy as np
import numpy.random as ran

halflife = 5.7
tau = halflife/np.log(2)

t = np.linspace(0,20,21)
n = np.exp(-t/tau)
dn = 0.1 * n**.5
noise = ran.standard_normal(len(n)) * dn
n += noise

pl.plot(t,n,'o')
pl.errorbar(t,n,yerr=dn,marker='o',linestyle='none',label='Carbon 14')
pl.xlim(np.amin(t)-0.5,np.amax(t)+0.5)
pl.xlabel('Time (thousands of years)')
pl.ylabel('Relative abundance')
pl.legend()
pl.title('Radioactive decay')

pl.show()
##############################################################################
# Nautilus exercise 
from numpy import linspace, pi, cos, sin
import matplotlib.pyplot as pl

phi = (1+5**.5)/2
n = linspace(0,1,100)
print(n)
x = n**.5 * cos(2*pi*phi*n)
y = n**.5 * sin(2*pi*phi*n)
print(x)

pl.subplot(1,1,1)
pl.plot(x,y,'o',color='yellow',markeredgecolor='yellow')
R = 12
pl.xlim(-R,R)
pl.ylim(-R,R)

ax = pl.gca()   # stands for get-current-axes
ax.set_aspect('equal')   # makes x and y axes equally wide  
ax.xaxis.set_visible(True)
ax.yaxis.set_visible(False)
ax.set_facecolor("black")

pl.show()
##############################################################################





