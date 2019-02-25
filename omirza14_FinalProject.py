#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 12:13:29 2018

@author: Omer Mirza, Ethan McCready
"""

import numpy as np
import math as m
from matplotlib import pyplot as plt
# =============================================================================
# Below are the functions used for the initial question
# =============================================================================
def p(x):
    return -2/x
def q(x):
    return 2/(x**2)    
def r(x):
    return (m.sin(m.log(x))) / x**2

def y2(x):
    return p(x), q(x), r(x)

def exactSolHelper(x,c1,c2):
    return  c1*x + (c2/x**2) - (3/10)*m.sin(m.log(x)) - (1/10) * m.cos(m.log(x))

def exactSol(x):
    return exactSolHelper(x, (11/10) - ((1/70) * (8 - 12*m.sin(m.log(2)) - 4*m.cos(m.log(2)))), (1/70) * (8 - 12*m.sin(m.log(2)) - 4*m.cos(m.log(2))))

def exactArray(array):
    exact = []
    for e in array:
        exact.append(exactSol(e))
    return exact

# =============================================================================
#  Below are the functions used for part b
# =============================================================================
    
def pb(x):
    return 0
def qb(x):
    return 4
def rb(x):
    return 4*x

def exact_sol_b(x):
    return m.e**2*(m.e**4 - 1)**(-1)*(m.e**(2*x) - m.e**((-2)*x)) + x
def exact_array_b(array):
    exact = []
    for e in array:
        #print(exact_sol_b(e))
        exact.append(exact_sol_b(e))
    return exact

# =============================================================================
# below are the functions used for question 7
# =============================================================================

c1 = 7.7042537 * 10**4
c2 = 7.9207462 * 10**4
a = 2.3094010 * 10**(-4)
b = -4.1666666* 10**(-3)
c = -1.5625 * 10**5
e = 3.0*10**7
s = 1000
i = 625
Q = 100
l = 120

def p7(x):
    return 0
def q7(x):
    return (s)/((e)*(i))
def r7(x):
    return (Q*x)/(2*(e)*(i))*(x-l)

def exact_sol_7(x):
    return ((c1* m.e**(a*x)) + (c2 * m.e**(-a*x)) + (b*(x - l)*x) + c)
def exact_array_7(array):
    exact = []
    for e in array:
        #print(exact_sol_7(e))
        exact.append(exact_sol_7(e))
    return exact
    

# =============================================================================
# this method prints all of our values and then plots them on the graph
# =============================================================================
def doAllCalc(w,x,y):
    for e in w:
        print(e)
    print('****************')
    for e in y:
        print(e)    
    print('****************')    
    if(len(y) == len(w)):
        for i in range(0,len(w)):
            print(abs(w[i] - y[i]))
            
        print('****************')  
    for e in x:
        print(e)
            
    w_numpy = np.array(w)
    y_numpy = np.array(y)
    x_numpy = np.array(x)
    
    plt.plot(x_numpy, w_numpy, label = 'Aprox')
    plt.plot(x_numpy, y_numpy, label = 'Exact')
    plt.legend(loc = 'upper left', frameon = False)
    

# =============================================================================
# this is the finite differnce method for aproximation
# =============================================================================
def finite_difference(p, q, r, n, alpha, beta, a, b ):
    aArray = []
    bArray = []
    cArray = []
    dArray = []
    
    h = (b-a) / (n + 1)
    x = a + h
    ai = 2 + h**2 * q(x)
    bi = -1 + (h/2)* p(x)
    di = -h**2*r(x) + (1 + (h/2) * p(x)) * alpha
    
    aArray.append(ai)
    bArray.append(bi)
    cArray.append(None) #NOTE: I added this so it doesn't mess with the iteration.
    dArray.append(di)
  
    for i in range (2, n):
        x = a + (i * h)
        ai = 2 + h**2*q(x)
        bi = -1 + (h/2) * p(x)
        ci = -1 - (h/2) * p(x)
        di = -h**2*r(x)
        aArray.append(ai)
        bArray.append(bi)
        cArray.append(ci)
        dArray.append(di)
     
    x = b - h
    ai = 2 + h**2*q(x)
    ci = -1 - (h/2) * p(x)
    di = -h**2*r(x) + (1 - (h/2) * p(x)) * beta
    aArray.append(ai)
    bArray.append(None)# same here
    cArray.append(ci)
    dArray.append(di)
    
    lArray = []
    uArray = []
    zArray = []
    
    li = aArray[0]
    ui = bArray[0] / aArray[0]
    zi = dArray[0] / li
    
    lArray.append(li)
    uArray.append(ui)
    zArray.append(zi)
    
    for i in range(2, n):
        li = aArray[i-1] - cArray[i-1] * uArray[i-2]
        ui = bArray[i-1] / li
        zi = (dArray[i-1] - cArray[i-1]* zi)/li

        
        lArray.append(li)
        uArray.append(ui)
        zArray.append(zi)
    li = aArray[n-1] - cArray[n-1] * uArray[n-2]
    zi = (dArray[n-1] - cArray[n-1] * zArray[n-2]) / li
    

    
    lArray.append(li)
    uArray.append(None) # ditto
    zArray.append(zi)
    
    wArray = []
    xArray = []
    wNot = alpha
    wNPlusOne = beta
    w = zArray[n-1]
    wArray.append(wNPlusOne)
    wArray.append(w)
    
    

    for i in range (n -1, 0, -1):
        w = zArray[i-1] - uArray[i - 1]*w
        wArray.append(w)
    
    wArray.append(wNot)
        
    for i in range (0, n + 2):
        x = a + i * h
        xArray.append(x)
        
    wrArray = []
    for e in reversed(wArray):
        wrArray.append(e)
        
    return wrArray,xArray
        
# =============================================================================
# these are method calls
# =============================================================================
w,x = finite_difference(p,q,r,9,1,2,1,2)
y = exactArray(x)



wb,xb = finite_difference(pb,qb,rb, 3, 0, 2, 0, 1)
yb = exact_array_b(xb)



w7, x7 = finite_difference(p7,q7,r7,19,0,0, l,0)
y7 = exact_array_7(x7)

# =============================================================================
# the following display the data and the graphs. NOTE: you can only keep one uncommented at a time
# =============================================================================
#doAllCalc(w,x,y)
#doAllCalc(wb,xb,yb)
doAllCalc(w7,x7,y7)



    

    