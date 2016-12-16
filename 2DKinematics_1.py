# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 22:40:41 2016

@author: William
"""
import numpy as np
import pylab as plt

L_ab = 1.118
A = [0,0]
Bx = []
By = []

def A_B(theta):
    Bx = (L_ab*(np.cos(np.radians(theta))))
    By = (L_ab*(np.sin(np.radians(theta))))
    return (Bx,By)

def Line(coordA, coordB):
    """
    coordA and B are tuples of x,y coordinates
    returns: plot of line connecting A and B
    """
    rise = coordA[1] - coordB[1]
    run = coordA[0] - coordB[0]
    slope = rise/run
    b = 0
    X = np.linspace(coordA[0], coordB[0],10)
    Y = []
    for i in X:
        Y.append(slope*i + b)
    return (X,Y)
    
    
    
fig1 = plt.figure()
for a in range(20,80,5):
#    Bx.append(L_ab*(np.cos(np.radians(a))))
#    By.append(L_ab*(np.sin(np.radians(a))))
    coord = A_B(a)
    plt.plot(coord[0], coord[1], 'b^')
    line = Line(A, coord)
    plt.plot(line[0], line[1], 'g--')
#plt.plot(Bx, By, 'g--', label = 'cubic')
plt.gca().set_aspect('equal', adjustable='box')
#plt.draw()

C = [4,5]
D = [6,10]
line2 = Line(C,D)
plt.figure('line')
plt.plot(line2[0], line2[1], 'r--')
