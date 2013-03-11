

def max(number1, number2):
    if number1 >= number2:
        return number1
    elif number1 <= number2:
        return number2
    else:
        print "Numerical comparison error!"
        
def min(number1, number2):
    return - max(- number1, -number2)



def Gauss(n):
    return n*(n+1) / 2
    
# def Gauss(n):
    # sum = 0
    # for k in range(n+1):
        # sum = sum + k
    # return sum
    
    
def factorial(n):
    if n == 0:
        return 1
    elif n > 1:
        prod = 1
        for k in range(1,n+1):
            prod = prod*k
        return prod
    else:
        print "Factorial input error!"
        
def first10digits(number):
    string = str(number)
    first10 = ""
    for k in range(10):
        first10 = first10 + string[k]
    return first10   
    
    
def last10digits(number):
    string = str(number)
    last10 = ""
    for k in range(10):
        last10 = last10 + string[-10+k]
    return last10
        
        

   
    
 