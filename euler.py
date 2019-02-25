#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 10:49:19 2018

@author: omer
"""
import numpy as np
from matplotlib import pyplot as plt



def f1(t,y):
    return y - t**2 + 1

def y(t):
    return (t+1)**2 -0.5* np.exp(t)
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

def fOther(t,y):
    return (np.exp(t) * np.cos(t)) 

def ya(t):
    return (t/( 1 + np.log(t)))
def yb(t):
    return (t * (np.tan(np.log(t))))
def yc(t):
    return (-3 + (2 / (1 + np.exp(-2*t))))
def yd(t):
    return ((t**2) + ((1/3) * (np.exp(-5*t))))


def omer_euler(f,a,b,alpha,n):
    myList1 = []
    myList2 = []
    h = (b-a)/n
    t = a
    w = alpha
    myList1.append(w)
    myList2.append(t)
    print(t,w, f(t,w))
    for i in range (1,n + 1):
        #print(f(t,w))
        #print(t, w)
        w = w + (h * f(t,w))
        t = t + h
        
        myList1.append(w)
        myList2.append(t)
        print(t, w, f(t,w)) 

    print('********************')    
    return myList1, myList2

wvals, tvals = np.array(omer_euler(fa, 1, 2, 1, 10))

yvals = y(tvals)

#plt.plot(tvals,wvals, color = "red", linewidth = 3, label = "Aproximate Solution")
#plt.plot(tvals,yvals, color = "blue", linewidth = 3, label = "Exact Solution")
#plt.legend(loc = 'upper left', frameon = False)

#plt.show

#wvals0, tvals0 = np.array(omer_euler(fOther, 0, 5, 1, 1000))
wvals1, tvals1 = np.array(omer_euler(fOther, 0, 5, 1, 500))
wvals2, tvals2 = np.array(omer_euler(fOther, 0, 5, 1, 50))
wvals3, tvals3 = np.array(omer_euler(fOther, 0, 5, 1, 20))
#wvals4, tvals4 = np.array(omer_euler(fOther, 0, 5, 1, 10))
#wvals5, tvals5 = np.array(omer_euler(fOther, 0, 5, 1, 5))


#yvals = yd(tvals)
#plt.plot(tvals0,wvals0, label = "1000")
plt.plot(tvals1,wvals1, linewidth = 3, label = "h = .01")
plt.plot(tvals2,wvals2, linewidth = 3, label = "h = .1")
plt.plot(tvals3,wvals3, linewidth = 3, label = "h = .25")
#plt.plot(tvals4,wvals4, label = "10")
#plt.plot(tvals5,wvals5, label = "5")
#plt.plot(tvals,yvals, color = "blue", linewidth = 3, label = "Exact Solution")
plt.legend(loc = 'lower left', frameon = False)

#plt.show

    