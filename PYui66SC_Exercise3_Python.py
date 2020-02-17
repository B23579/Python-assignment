
def longest (sentence):
    """ This function takes a sentence as input and return
    the longest word in string"""
    import copy
    T = list()
    T1 = list()
    tab_Rang = list()
    sentence = sentence.split() # we use this function to trabsform the senten
    # as a list
    len_stc = len(sentence)

    for i in range (len_stc):
        a=len(sentence[i])
        T.append(a)
    # this loop help us to transform the previour liste as a liste of len of
    #  word which contain sentence after split
    
    T1 = copy.copy(T) # whithout the function copie, 
    #if we use "=", when will motify the list T the the list T1 will be
    #automaticaly modify, thus it is forbidden to use it when we want to do the copie of the list 
    
    """ ours goal into the next step is the onbtain the rang per oder
     decreasing of all numbers which containt T after that, we replace
     this the rang of all number at same index and use it 
     to obtain the big number or the longest word into the sentence"""
     
    # Classement des valeurs du tableau par ordre croissant
    sorted(T, reverse = True)
    
    # Delet of the multiples value into the list
    i, k, out, n = 0, 1, 1, len(T)

    while out != 2:
            if k < n :
                    if T[i] == T[k] :
                            T.pop(k)
                            k = 1
                            i = 0
            else : 
                    out = 2
                    
            n = len(T) # take the new lenght of T after supression
            k = k + 1
            i = i + 1
    # rank of the number
    k = len(T)
    l= len(T1)
    rang = 0
    for i in range(l):
            for j in range(k):
                    if T1[i] == T[j] :
                            rang =T.index(T[j])+1
                            tab_Rang.append(rang)
    #Indix of element which have the rank 1
    tabindex = list()
    for i in range(len(tab_Rang)):
        if tab_Rang[i] ==1 : 
            tabindex.append(i)
    lis_long_word = list()
    for i in range(len(tabindex)):
        a = tabindex[i] 
        lis_long_word.append(sentence[a])
    return lis_long_word

sentence = str("")
print("Enter a sentence")
sentence = input()
print(longest(sentence))