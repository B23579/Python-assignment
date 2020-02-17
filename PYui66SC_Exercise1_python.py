def Revex(word): 
    """ This function takes a string as input and return a new string whit 
    the letter in reverse oder"""
    l1=list()
    l2=list()
    for i in word:
        l1.append(i)
        l2=l1[::-1]
    l2=''.join(l2)
    return l2
word = input("Enter a word" )
print(Revex(word))