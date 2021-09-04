import math 
"""
This function exchanges two variables for each other

Parameters
----------
    binit : float
        This is simply b, but used for assertion testing
    ainit : float
        This should be a, but used only for assertion testing 
    a : float
        input 1
    b : float
        input 2 
    temp : float
        our placeholder to store numbers without losing them permanently 
"""

def ExchangeTwoVariable(a,b): 
    binit = b       # for assertion test
    ainit = a       # for assertion test

    temp = 0        # temporary variable space
    temp = a        # temp to a 
    a = b           # a to b 
    b = temp        # b to temp 
    assert (a != ainit) 
    assert (b != binit) 
    print("Unit Tests Passed !!!") 
    print("A originally was %s, but now is %s" %(ainit,a))
    print("B originally was %s, but now is %s" %(binit,b))

a = 3
b = 12 

ExchangeTwoVariable(a,b)
