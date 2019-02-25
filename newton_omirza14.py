import math as m

''' 

Omer Mirza

Newton Method algorithm

'''

#This function returns an equation solved for a given x value
def f(x):
    return m.cos(x) - x

#This function returns an equation solved for a given x value
#NOTE: This funciton is the derivative to the above funciton
def df(x):
    return (-(m.sin(x))) - 1

#THE FOLLOWING FUNCTIONS EXPOSE THE ISSUE WITH THE NEWTON METHOD WHICH WILL BE EXPLAINED BELOW
    
#This function returns an equation solved for a given x value
def badF(x):
    return (1/x) -2
#This function returns an equation solved for a given x value
#NOTE: This funciton is the derivative to the above funciton
def badDF(x):
    return (-1/x**2)

#NOTE THE FOLLOWING METHODS COULD HAVE BEEN CONDENSED INTO ONE METHOD, BUT IT IS TWO FOR READABILITIES SAKE

#This method performes the newton method on the first function in the program
def omer_newton(p0, tol, maxIt):
    
    for i in range(0, maxIt):
        p1 = p0 - (f(p0)/df(p0))
        print('We are at: ' , p1)
        #print('We are at', p0)
        if(abs(f(p1)) < tol):
            print('ZERO FOUND AT', p1)
            return p1
        p0 = p1
    print('we were unable to find a zero')
 
#This method exposes the issue with the newton method, i.e. that we cannot divide by zero
    #it demonstrates that not all equations can be solved with this method
def omer_bad_newton(p0,tol, maxIt):
    for i in range(0, maxIt):
        p1 = p0 - (badF(p0)/badDF(p0))
        print('We are at: ' , p1)
        #print('We are at', p0)
        if(abs(badF(p1)) < tol):
            print('ZERO FOUND AT', p1)
            return p1
        p0 = p1
        
#METHOD CALLS     
omer_newton((m.pi/4), 0.00000001, 100000)
omer_bad_newton(1, 0.00000001, 100000)

