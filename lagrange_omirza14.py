#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 09:14:30 2018

@author: omer
"""
import numpy as np
import matplotlib.pyplot as plt

def omer_lagrange (xdata, ydata, xvalue):
    n = xdata.size
    px = 0
    for k in range (0,n):
        l = 1
        for j in range (0,n):
            if j!=k:
                l = l * (xvalue - xdata[j])/(xdata[k] - xdata[j])
                print(str(l) + " | " + str(px) )
                print('****************')
        px = px + ydata[k] * l
        
    return px

x1=np.array([0, np.pi/3, 2*np.pi/3, np.pi, 4*np.pi/3, 5*np.pi/3, 2*np.pi])
y1=np.array([0, (3**0.5)/2, (3**0.5)/2, 0, -(3**0.5)/2,-(3**0.5)/2,0])

omer_lagrange(x1,y1,np.pi/8)

#print(np.sin(np.pi/8))

print(str(abs(omer_lagrange(x1,y1,np.pi/8) - np.sin(np.pi/8) ) / np.sin(np.pi/8)) + " is the relative error")

xvals = np.linspace(0,2*np.pi, 100)
yvals1 = omer_lagrange(x1,y1, xvals)
yexact = np.sin(xvals)

plt.plot(xvals, yvals1, xvals, yexact)
plt.show()


