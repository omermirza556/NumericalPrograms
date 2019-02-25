#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 12:24:24 2018

@author: omer mirza
"""
import math as m
def f(x):
    return m.cos(x) - x
def f1(x):
    return x**3 -2*x**2 - 5
def f2(x):
    return x**3 + 3*x**2 -1
def f3(x):
    return x - m.cos(x)
def f4(x):
    return x -.8 -.2*m.sin(x)

def weak(x):
    return (1/x) -2

##This code solves for the equation using the secent method using the specified equations above
    
def omer_sec(p0, p1, tol, maxit):
    for i in range(maxit):
        print(str(i) + ' | ' +str(f(p0)) + ' | ' + str (p0) + ' | ' +str(p1)  )
        if(p0)== 0:
            print('The solution is ' + str(p1))
            return p1
        p = p1 - (f(p1) * (p1-p0)) / (f(p1) - f(p0))
        p0 = p1
        p1 = p
    print('No solution was found')
    return p1

def omer_sec1(p0, p1, tol, maxit):
    for i in range(maxit):
        print(str(i) + ' | ' +str(f1(p0)) + ' | ' + str (p0) + ' | ' +str(p1)  )
        if(p0)== 0:
            print('The solution is ' + str(p1))
            return p1
        p = p1 - (f1(p1) * (p1-p0)) / (f1(p1) - f1(p0))
        p0 = p1
        p1 = p
    print('No solution was found')
    return p1

def omer_sec2(p0, p1, tol, maxit):
    for i in range(maxit):
        print(str(i) + ' | ' +str(f2(p0)) + ' | ' + str (p0) + ' | ' +str(p1)  )
        if(p0)== 0:
            print('The solution is ' + str(p1))
            return p1
        p = p1 - (f2(p1) * (p1-p0)) / (f2(p1) - f2(p0))
        p0 = p1
        p1 = p
    print('No solution was found')
    return p1
def omer_sec3(p0, p1, tol, maxit):
    for i in range(maxit):
        print(str(i) + ' | ' +str(f3(p0)) + ' | ' + str (p0) + ' | ' +str(p1)  )
        if(p0)== 0:
            print('The solution is ' + str(p1))
            return p1
        p = p1 - (f3(p1) * (p1-p0)) / (f3(p1) - f3(p0))
        p0 = p1
        p1 = p
    print('No solution was found')
    return p1
def omer_sec4(p0, p1, tol, maxit):
    for i in range(maxit):
        print(str(i) + ' | ' +str(f4(p0)) + ' | ' + str (p0) + ' | ' +str(p1)  )
        if(p0)== 0:
            print('The solution is ' + str(p1))
            return p1
        p = p1 - (f4(p1) * (p1-p0)) / (f4(p1) - f4(p0))
        p0 = p1
        p1 = p
    print('No solution was found')
    return p1

def omer_sec_weak(p0, p1, tol, maxit):
    for i in range(maxit):
        print(str(i) + ' | ' +str(weak(p0)) + ' | ' + str (p0) + ' | ' +str(p1)  )
        if(p0)== 0:
            print('The solution is ' + str(p1))
            return p1
        p = p1 - (weak(p1) * (p1-p0)) / (weak(p1) - weak(p0))
        p0 = p1
        p1 = p
    print('No solution was found')
    return p1

#The following code executes with the specified values in the book

omer_sec(.5, m.pi/4, 0.000001, 6)
print('***********')
omer_sec1(1,4,0.000001, 6)
print('***********')
omer_sec2(-3,-2,0.000001, 6)
print('***********')
omer_sec3(0,m.pi/2,0.000001, 6)
print('***********')
omer_sec4(0,m.pi/2,0.000001, 6)
print('***********')
omer_sec_weak(1,1.2,0.000001, 100)
print('***********')
omer_sec_weak(1.4,1.45,0.000001, 100)
# I have been running into the divide by zero error if I use too many itterations
# something to note with secent method is that you do not have to find the derivative of the function at every step
#not the case with newton's method        
    