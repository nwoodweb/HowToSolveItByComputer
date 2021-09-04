import math
import numpy as np
import matplotlib as plt 

"""
This function performs the euler numerical approximation for differntial equations:

        given dy/dx, y(x0) = y0, and a "step size" for iterations

            y = y0 + h * f(x0,y0)
Parameters
-----------
    xinit : float
        our initial x value

    yinit : float

    xmax : float
        our desired x value 
    
    stepSize : float : >= 0 
        our step size for iteration, theoretically defined as h in textbooks 

    diffFunc : equation
        our differential equation 

--------------
End Parameters

Yields
------
    Final approximation at xmax  

"""

def EulerApproximation(xinit,yinit,stepSize,diffFunc,xmax):
    for i in range(xmax): 
        ynew = yinit + stepSize * diffFunc      # performs the euler approximation y = y0 + h * f(x,y) 
        yinit = ynew                            # assigns new y for iteration 
        xinit = xinit + stepSize                # assigns new x for iteration
        yfinal = ynew
    print("Final Y Approximation at x = %s : %s" %(xmax,yfinal))     # prints new value 
    return yfinal


xmax=30
xinit = 3
yinit = 10 
stepSize = 0.01
diffFunc = np.sin(yinit) + np.cos(xinit**2) + xinit**3


EulerApproximation(xinit,yinit,stepSize,diffFunc,xmax)
