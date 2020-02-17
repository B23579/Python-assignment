def VoweX(word):
    """ this function takes a string as input and returns the number
    of vowels in the string"""
    L= ['a', 'e', 'i', 'o','u']
    summ = 0
    for elm in word :
        if elm in L: 
            summ = summ + 1
    return summ 
a = input("Enter the word   ")
print(" the number of vowels is ",VoweX(a))