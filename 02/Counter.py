import math 

"""
This program is designed to count the given numbers

The context of the counting algorithm per book has a pass-fail threshhold, given that the
numbers originally represented test scores

Parameters
----------
    input : list
        our input list of numbers 
        Example : [1,3,6,78,3,1,443]         

    passMark : int 
        The pass-fail threshhold  

    total : int 
        total number of entries 

    count : int
        our iterator value to compare against total 

    pass : int
        current number of passing entries 
    
    current : float
        current entry

    total : integer
        total number of entries 

"""

def PassCount(input,passMark): 
    total = len(input)                              # define total
    print("Total Number of Entries : %s" %(total))  # output total
    passit = 0                                        # initialize count
    count = 1                                       # initialize iterator 

    while count < total:                                # while iterator less than total length        

        for i in input:                             # for every entry in input 
            count += 1                                  # add to iterator 

            if input[i] >= passMark:                # what if number pass threshhold ? 
                passit += 1                           # add passing 
            
    print("Number of Passing Entries : %s" %(passit)) 
    # END FUNCTION 

input = [3,4,5,6,1,3,4,5]     
passMark = 3

PassCount(input,passMark)
