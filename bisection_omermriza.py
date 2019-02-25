#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 14:09:56 2018

@author: omer
"""
import sys

maxInt = sys.maxint

def doMath(x):
    return (x**3 + 4*(x**2) - 10)

def biMeth(a,b,tol):
    fa = doMath(a)
    fb = doMath(b)
    
    if fa*fb >= 0:
        print('choose a different a & b')
    else:
        for i in range(1, maxInt):
            an = a
            bn = b
            pn = (an+bn)/2
            print(i + ',' + an + ', ' + bn + ',' + pn)
            fp = doMath(pn)
            if fp == 0:
                print('Solution is ', pn)
        if fp*fa > 0:
            a = pn
            b = bn
            fa = fp
            
        if fp*fb> 0:
            a = an
            b = pn
            fb = fp
        
 

