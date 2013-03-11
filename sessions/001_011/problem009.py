import math

import listoperations


def pythagtriple(k,m,n):
	a = m**2 - n**2
	b = 2*m*n
	c = m**2 + n**2
	return (k*a, k*b, k*c)
    
def listpythagtriples(K,N,M):
    L = []
    for k in range(K+1):
        for n in range(N+1):
            for m in range(M+1):
                L.append(pythagtriple(k,n,m))
    return L

def sumoftriple(triple):
	return triple[0] + triple[1] + triple[2]    

def prodoftriple(triple):
    return triple[0] * triple[1] * triple[2]

def findtriplewithsum(sum, K,N,M):
	for triple in listpythagtriples(K,N,M):
		if sumoftriple(triple) == sum:
			return triple
		else:
			continue

specialtriple = findtriplewithsum(1000, 10, 20, 30)

print prodoftriple(specialtriple)

