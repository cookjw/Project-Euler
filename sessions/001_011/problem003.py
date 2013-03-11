import math

# List Operations

def checkorder(somelist):
        somelength = len(somelist)
        rightorder = True
        for index in range(somelength - 1):
            if somelist[index] <= somelist[index + 1]:
                continue
            else:
                rightorder = False
                break 
        return rightorder  


def sortlist(list):
    length = len(list)        
    while checkorder(list) == False:     
        for index in range(length - 1):
            if list[index] <= list[index + 1]:
                continue
            else:
                a = list[index]
                b = list[index + 1]
                list[index] = b
                list[index + 1] = a
                        
    return list


def listmax(list):
    newlist = sortlist(list)
    maxindex = len(newlist) - 1
    return newlist[maxindex]

# Factoring Operations

def primesieve(n): # Sieve of Eratosthenes
	A = []
	for k in range(n+1):
		A.append(True)
	for i in range(2, int(math.sqrt(n+1) + 1)):
		if A[i] == True:
			for j in range(i**2, n+1, i):
				A[j] = False
	B = []
	for i in range(2,n+1):
		if A[i] == True:
			B.append(i)
	return B

def smallestprimefactor(n):
	for p in primesieve(int(math.sqrt(n)+1)):
		if n % p == 0:
			return p
		        break
        

def smallestprimefactor2(n):
	if smallestprimefactor(n) == None:
		return n
	else:
		return smallestprimefactor(n)

def firstquotient(n):
	return n / smallestprimefactor2(n)

def divisionsteps(n):
	N = n
	while N > 1:
		print firstquotient(N)
		N = firstquotient(N)

def factorize(n):
	F = []
	N = n
	while N > 1:
		F.append(smallestprimefactor2(N))
		N = firstquotient(N)
	return F

def largestprimefactor(n):
	return listmax(factorize(n))
    
Nput = input("Of what number would you like to find the largest prime factor?\n")

print largestprimefactor(Nput)

























# import math



# def primesieve(n):
    # A = {}
    # for k in range(2,n+1):
        # A[k]= True
    # for i in range(2,int(math.sqrt(n))+1):
        # if A[i] == True:
            # for j in range(i**2, n+1, i):
                # A[j] = False
    # B = []
    # for i in range(2,n+1):
        # if A[i] == True:
            # B.append(i)
        # else:
            # continue
    # return B    

        

# def sortlist(list):
    # length = len(list)
    # def checkorder(somelist):
        # somelength = len(somelist)
        # rightorder = True
        # for index in range(somelength - 1):
            # if somelist[index] <= somelist[index + 1]:
                # continue
            # else:
                # rightorder = False
                # break 
        # return rightorder   
         
    # while checkorder(list) == False:     
        # for index in range(length - 1):
            # if list[index] <= list[index + 1]:
                # continue
            # else:
                # a = list[index]
                # b = list[index + 1]
                # list[index] = b
                # list[index + 1] = a
                        
    # return list    

# def listmax(list):
    # newlist = sortlist(list)
    # maxindex = len(newlist) - 1
    # return newlist[maxindex]

    
# def primefactors(N):
    # C = []
    # M = N    
    # while M > 1: 
        # for k in range(2, int(math.sqrt(M)+2)):
            # for p in primesieve(100*k):
                # if M % p != 0:
                    # continue
                # else:
                    # C.append(p)
                    # break
            # M = M/p
            # break 
    # return C
    
# def maxprimefactor(N):
    # return listmax(primefactors(N))
    
# Nput = input("Of what number would you like to find the largest prime factor?\n")
    
# print maxprimefactor(Nput)

        
        

    