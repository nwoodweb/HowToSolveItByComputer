import math
import numpy as np
import matplotlib as plt 


def EulerApproximation(xinit,yinit,stepSize,diffFunc,xmax):
    for i in range(xmax): 
        ynew = yinit + stepSize * diffFunc      # performs the euler approximation y = y0 + h * f(x,y) 
        yinit = ynew                            # assigns new y for iteration 
        xinit = xinit + stepSize                # assigns new x for iteration
    print("Final Y Approximation at x = %s : %s" %(xmax,yinit))     # prints new value 
                

xmax=30
xinit = 3
yinit = 10 
stepSize = 0.12
diffFunc = np.sin(yinit) + np.cos(xinit**2)


EulerApproximation(xinit,yinit,stepSize,diffFunc,xmax)
