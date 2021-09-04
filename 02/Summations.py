"""
The purpose of this program is to sum numbers and compute the everage 

This is accomplished by iterating downward a len(list) to zero

Parameters
----------
    input : list
        This is our input list of numbers

    total : int 
        this is the total number of numbers in input

    count : int 
        this is our iterator value, and should always be set equal
        to total

    sumVal : int or float 
        this is our summation, and is complete once count = 0

    average : float 
        this is the mean of our summation, taken accordingly

            sum of values / number of values 

Yields
------
    Sum : int or float 
    Average : float

"""


def Summation(input):
    total = len(input)                          # total number of entries
    count = total                               # set iterator equal total
    sumVal = 0                                  # reset sum

    while count > 0:                            # downwards iteration
        for i in range(total):                  # for all entries in input
            sumVal += input[i]                  # add current entry to sum
            count -= 1                          # down count

    average = sumVal / total                    # compute average

    print("The Sum of %s is : " %(input)) 
    print(sumVal) 
    print("The Average is : %s" %(average))
    return sumVal
    return average

# input values 
input = [1,55,12,33,64,76,87,41,100,-21,-50] 

Summation(input) 
