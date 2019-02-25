'''
The purpose of this script is to analyze the bisection method
@author omer mirza
'''


#We define the function we will use for the bisection as the one below
def function(x):
    return (pow(x,3)) + (4*pow(x,2)) - 10

#We give a max itteration for our for loop in order to approximate the term in which we will reach a zero value
#It will itteratively give out information in a print statemtent 
def biMeth(a,b, maxIt, tol):
    
    if a*b < 0:
        print('please choose different interval')
        return
    c = (a+b)/2.0 
    for i in range(0,maxIt):
        print(i + 1)
        print(a)
        print(b)
        print(c)
        print(function(c))
        print('**********')
        if function(c) == 0:
            return c
        elif abs(function(c)) < tol:
            print(str(c) + ' is the answer')
            return c
        elif (function(a)*function(c)) < 0:
            b=c
        else:
            a = c
        
        c = (a+b)/2.0
        
    return c


        
biMeth(1,2, 2000, 0.000000001)

#When comparing to Table 2.1 in our text book we get the same answers
    
    
    

