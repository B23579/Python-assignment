def Digits_Magic(): 
    """this function search the large number of 4 digits such that 
    max(x)-min(x) = x"""
    number, number_max, number_min, = 0, 0, 0
    #Magic_number = []
    for i in range(1000,10000):
        number = str(i)
        number_max = "".join(sorted(number, reverse= True))
        number_min = "".join(sorted (number))
        number_max = int(number_max)
        number_min = int(number_min)
        if number_max - number_min == i :
            Magic_number = i
    print("The number which fulfill the condition is ",Magic_number)

Digits_Magic()