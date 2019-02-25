#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 13:25:02 2018

@author: omer mirza
"""
import math as m

#The following is the functions we will be using for our code
def f1(x):
    return x * m.log(x)
def f2(x):
    return m.sqrt(1 + m.cos(x)**2)
# The following is the method for the midpoint rule
def comp_midpoint(f,a,b,n):
    h = (b-a)/n
    
    sum = 0.0
    x = a + h/2
    
    while (x < b):
        sum += h * f(x)
        x += h
        
    return sum
    
# THe following is the method for the trapezoidal rule
def trap_midpoint(f,a,b,n):
    h = (b - a) / n
    
    sum = (h / 2) * (f(a) + f(b))
    for i in range (1 , n):
        sum += h * f(a + n*h)
        
    return sum
# The following is the print statements for the above methods
print('**********************')
print (comp_midpoint(f1, 1.0, 2.0, 1))
print (comp_midpoint(f1, 1.0, 2.0, 4))
print (comp_midpoint(f1, 1.0, 2.0, 10))
print (comp_midpoint(f1, 1.0, 2.0, 50))
print (comp_midpoint(f1, 1.0, 2.0, 100))
print('**********************')
print (trap_midpoint(f1, 1.0, 2.0, 1))
print (trap_midpoint(f1, 1.0, 2.0, 4))
print (trap_midpoint(f1, 1.0, 2.0, 10))
print (trap_midpoint(f1, 1.0, 2.0, 50))
print (trap_midpoint(f1, 1.0, 2.0, 100))
print('**********************')
print (comp_midpoint(f2, 0.0, 48.0, 1))
print (comp_midpoint(f2, 0.0, 48.0, 4))
print (comp_midpoint(f2, 0.0, 48.0, 10))
print (comp_midpoint(f2, 0.0, 48.0, 50))
print (comp_midpoint(f2, 0.0, 48.0, 100))
print('**********************')
print (trap_midpoint(f2, 0.0, 48.0, 1))
print (trap_midpoint(f2, 0.0, 48.0, 4))
print (trap_midpoint(f2, 0.0, 48.0, 10))
print (trap_midpoint(f2, 0.0, 48.0, 50))
print (trap_midpoint(f2, 0.0, 48.0, 100))
print('**********************')

# With the composite midpoint rule we end up creating rectangles for every itteration
# With the trapezoidal method we construct trapazoids for every itteration.
# The result of this is that the trapezoid is much more accurate compared to the midpoint due to the fact that the trapezoids arc stays closer to the apparent arc of the curve
# With the midpoint formula it ends up becoming off slightly and then increasingly more so later on, especially when the area under the arc being seperated by only one point.
 
