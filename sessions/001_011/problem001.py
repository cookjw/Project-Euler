# largest multiple

def largest_multiple(k, n):
        if n % k == 0:
	    return (n / k - 1)*k
	else:
	    return (n / k) * k

# Gauss

def Gauss(n):
    if n == 0:
        return 0
    else:
        return n + Gauss(n-1)

# Gauss-multiple

def Gauss_multiple(n, k):
    return k * Gauss(n)


# Bounds for Gauss-multiple

def howhighwego(k, n):
    return largest_multiple(k,n) / k

# Operation of the program

def problem_one(a,b,c):    
    return Gauss_multiple(howhighwego(a,c), a) + Gauss_multiple(howhighwego(b,c) , b)
    
# def problem_one(a,b,c):
    # ac = howhighwego(a,c)
    # bc = howhighwego(b,c)
    # aca = Gauss_multiple(ac, a)
    # bcb = Gauss_multiple(bc, b)
    
    
    
    
def problem1(n):
    total = 0
    for x in range(n):
       if  x % 3 ==0 or x % 5 == 0:
           total = total + x
       else:
           continue
    return total

# for x in range(1,100):
   # if problem1(x) != problem_one(3,5,x):
      # print x

      
# for x in range(1,100):
    # if problem1(x) == problem_one(3,5,x):
        # print x


print howhighwego(3,17)
print howhighwego(5,17)
print Gauss_multiple(5,3) + Gauss_multiple(3,5)

print Gauss_multiple(5,3) == 0 + 3 + 6 + 9 + 12 + 15
print Gauss_multiple(3,5) == 0 + 5 + 10 + 15


        

        
        
    
    
    

    



