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

def primenumber(N):
    n = 10
    while len(primesieve(n)) <= N - 1:
        n = n*1000

    if len(primesieve(n)) >= N:
        return primesieve(n)[N-1]

        
print primenumber(10001)
        