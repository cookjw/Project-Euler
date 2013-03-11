import listoperations
import math

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
    
def primenumber(N): # Nth prime number
    n = 10
    while len(primesieve(n)) <= N - 1:
        n = n*1000

    if len(primesieve(n)) >= N:
        return primesieve(n)[N-1]

        
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