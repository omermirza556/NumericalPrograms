#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 19:39:56 2018

@author: omer
"""
#IT IS IMPORTANT TO NOTE THAT ORDER OF OPPERATIONS MATTERS

import math as m

#The following methods return the equations we plan on using 
def f1(x):
    return m.sin(x)
def f2(x):
    return (x**3) - (4*(x**2)) + (1)

#This method aproximates the derivative of the function at a point 
#with the forward difference formula
def dfdx_fw(function, xi, h):
    return (function(xi + h) - function(xi))/ h

#This method aproximates the derivative of the function at a point 
#with the  Backwards difference formula
def dfdx_bw(function, xi, h):
    return ((function(xi)) - (function(xi - h))) / h


#This method aproximates the derivative of the function at a point 
#with the first derivative central difference formula
def dfdx_ce(function, xi, h):
    return (function(xi + h) - function(xi - h)) / (2*h)

#This method aproximates the Second derivative of the function at a point 
#with the Second derivative central difference formula
def d2fdx2_ce(function, xi, h):
    return ((function(xi + h)) - (2*function(xi)) + (function(xi - h)))/(h**2)
# The following is the results of our work, seperated by equations 
print('***************')
print(dfdx_fw(f1, m.pi/3, .1))
print(dfdx_bw(f1, m.pi/3, .1))
print(dfdx_ce(f1, m.pi/3, .1))
print(d2fdx2_ce(f1, m.pi/3,.1))
print('***************')
print(dfdx_fw(f2, 1, .1))
print(dfdx_bw(f2, 1, .1))
print(dfdx_ce(f2, 1, .1))
print(d2fdx2_ce(f2, 1, .1))
print('***************')



