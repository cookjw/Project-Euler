import listoperations

def sumdigits(number):
    string = str(number)
    L = []
    for k in range(len(string)):
        L.append(int(string[k]))
    return listoperations.listsum(L)

   
print sumdigits(2**1000)
    
        