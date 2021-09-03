import math 

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
