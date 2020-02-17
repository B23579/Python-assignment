def SumoverX(number):
    """ This function takes an integer as input and return the sum over all 
    the integer betwen zero and that integer including it"""
    summ = 0
    number = int(number)
    for i in range(number+1): # number + 1 because if we use only number the 
        # not consider the number
        summ = summ + i
    return summ
number = input("enter the number  ")
print(SumoverX(number))