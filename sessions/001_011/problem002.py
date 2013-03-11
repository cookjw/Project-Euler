def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n-2) + fib(n-1)

        
# for n in range(1,11):
    # print (n, fib(n))

    
    

# print fib(32)    
# print fib(33)



def problem2(x):
    n = 1
    while fib(n) <= x:
        n = n+1
    bound = n
    total = 0
    for n in range(1, bound):
        if n % 2 == 0:
            total = total + fib(n)
        else:
            continue
    return total
            
print problem2(10)


def problemtwo(x):
    n = 1
    while fib(n) <= x:
        n = n+1    
    bound = n
    total = 0
    for n in range(1,bound):
        if fib(n) % 2 == 0:
            total = total + fib(n)
        else:
            continue
    return total

print problemtwo(4000000)

# 1, 2, 3, 5, 8, 13, 21, 34, 
