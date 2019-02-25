#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 14:17:14 2018
The purpose of of this script is to analyze the difference between hard coded functions and pythons in built library of functions
@author: omer mirza
"""

import math as m

def omer_fact(n):
    total = 1
    
    if(n == 0):
        return 1
    
    for i in range(n):
        total *=(i+1)
    return total

def omer_e5(x):
    return 1 + (pow(x,1)/omer_fact(1)) +(pow(x,2)/omer_fact(2)) + (pow(x,3)/omer_fact(3)) + (pow(x,4)/omer_fact(4)) + (pow(x,5)/omer_fact(5))

print(omer_fact(4))
print(omer_fact(5))
print(omer_fact(0))
print("*****************")
print(omer_e5(3))
print(omer_e5(1))
print(omer_e5(((-1)/2)))
print(omer_e5(-4))
print("*****************")
print(str(m.exp(3)) + " | " + str(omer_e5(3)))
print(str(m.exp(1)) + " | " + str(omer_e5(1)))
print(str(m.exp(((-1)/2))) + " | " + str(omer_e5(((-1)/2))))
print(str(m.exp(-4)) + " | " + str(omer_e5(-4)))
print("*****************")

print("Absolute error for 3: " + str(abs(m.exp(3)-omer_e5(3))))
print("Relative error for 3: " + str((abs(m.exp(3)-omer_e5(3)))/abs(m.exp(3))))

print("Absolute error for -1/2: " + str(abs(m.exp(((-1)/2))-omer_e5(((-1)/2)))))
print("Relative error for -1/2: " + str((abs(m.exp(((-1)/2))-omer_e5(((-1)/2))))/abs(m.exp(((-1)/2)))))
    
print("Absolute error for 1: " + str(abs(m.exp(1)-omer_e5(1))))
print("Relative error for 1: " + str((abs(m.exp(1)-omer_e5(1)))/abs(m.exp(1))))


print("Absolute error for -4: " + str(abs(m.exp(-4)-omer_e5(-4))))
print("Relative error for -4: " + str((abs(m.exp(-4)-omer_e5(3)))/abs(m.exp(-4))))

#You will find above that for postive numbers the aproximation is quite good, however it falls apart with negative numbers, when compared to the inbuilt function
#the abosolute error does not vary wildly between the in built functions and the hard coded ones, however the relative error has an extreme outlier, due to how summations work when dealing with negative numbers



        

        