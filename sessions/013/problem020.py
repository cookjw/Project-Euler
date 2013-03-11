import listoperations

def sumdigits(number):
    string = str(number)
    L = []
    for k in range(len(string)):
        L.append(int(string[k]))
    return listoperations.listsum(L)

def factorial(number):
    if number == 0:
        return 1
    else:
        answer = 1
        for k in range(1, number+1):
            answer = answer*k
        return answer

   
print sumdigits(factorial(100))