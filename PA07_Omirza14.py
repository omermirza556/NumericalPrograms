#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 11:12:49 2018

@author: Omer Mirza
"""
import numpy as np
from matplotlib import pyplot as plt


#The following are our aproximations for the equations listed below

# 0 <= t < = 2, y(0) = 0.5, h = 0.2
def f1(t,y):
    return y - t**2 + 1

# 1 <= t <= 2, y(1) = 1, h = 0.1
def fa(t,y):
    return ((y/t) - ((y/t)**2))

# 1<= t <= 3, y(1) = 0, h =0.2
def fb(t,y):
    return (1 + (y/t) + ((y/t)**2))

# 0<= t <= 2, y(0) = -2, h = 0.2
def fc(t,y):
    return (-1*(y+1)*(y+3))

# 0 <= t <= 1, y(0) = (1/3), h = 0.1
def fd(t,y):
    return ((-5*y) + (5*t**2) + (2*t))

# 0 <= t <= 5, y(0) = 1 , h = 0.25, h = 0.1, h = 0.01
def fOther(t,y):
    return (np.exp(t) * np.cos(t))

# The following are the actual equations 
def y(t):
    return (t+1)**2 -0.5* np.exp(t)

def ya(t):
    return (t/( 1 + np.log(t)))

def yb(t):
    return (t * (np.tan(np.log(t))))

def yc(t):
    return (-3 + (2 / (1 + np.exp(-2*t))))

def yd(t):
    return ((t**2) + ((1/3) * (np.exp(-5*t)))) 

# The following method will be using Runge Kutta to calculate an aprox. for our graphs
def RK4(f,a,b,alpha,n):
    
    wList = []
    tList = []
    
    h = (b-a) / n
    t = a
    w = alpha
    
    wList.append(w)
    tList.append(t)
    
    for i in range (0,n):
        
        print('t: ' + str(t) + ', w: ' + str(w))
        
        k1 = h * f(t,w)
        k2 = h * f(t + 0.5 * h, w + 0.5 * k1)
        k3 = h * f(t + 0.5 * h, w + 0.5 * k2)
        k4 = h * f(t + h, w + k3)
        
        t = t + h
        w = w + (k1 + k2*2 + k3*2 + k4 )/6
        
        
        tList.append(t)
        wList.append(w)
        
    print('t: ' + str(t) + ', w: ' + str(w))
        
    return tList, wList

tList, wList = RK4(f1, 0, 2, 0.5, 10)
yList = []
for element in tList:
    yList.append(y(element))
    

aTList, aWList = RK4(fa, 1, 2, 1, 10)
aYList = ya(aTList)

bTList, bWList = RK4(fb, 1, 3, 0, 10)
bYList = yb(bTList)

cTList, cWList = RK4(fc, 0, 2, -2, 10)
cYList = []

for element in cTList:
    cYList.append(yc(element))

dTList, dWList = RK4(fd, 0, 1, (1/3), 10)
dYList = []

for element in dTList:
    dYList.append(yd(element))
    
otherTList,otherWList = RK4(fOther, 0, 5, 1, 500)
other1TList,other1WList = RK4(fOther, 0, 5, 1, 50)
other2TList,other2WList = RK4(fOther, 0, 5, 1, 20)


#plt.plot(otherTList,otherWList, linewidth = 2, label = "h = .01")
#plt.plot(other1TList,other1WList, linewidth = 2, label = "h = .1")
#plt.plot(other2TList,other2WList, linewidth = 2, label = "h = .25")

#plt.plot(otherTList,otherWList)
#plt.plot(other1TList,other1WList)
#plt.plot(other2TList,other2WList)
    
plt.plot(tList, wList)
plt.plot(tList,yList)

#plt.plot(aTList,aWList)
#plt.plot(aTList,aYList)

#plt.plot(bTList,bWList)
#plt.plot(bTList,bYList)

#plt.plot(cTList,cWList)
#plt.plot(cTList,cYList)

#plt.plot(dTList,dWList)
#plt.plot(dTList,dYList)
#bTList, bWList = RK4(fb, 1, 3, 0, 10)
#cTList, cWList = RK4(fc, 0, 2, -2, 10)
#dTList, dWList = RK4(fd, 0, 1, (1/3), 10)

plt.legend(loc = 'lower left', frameon = False)





    



