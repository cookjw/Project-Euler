import listoperations




def collatz(n):
    if n % 2 == 0:
        return n/2
    if n % 2 == 1:
        return 3*n + 1
        
def collatzseq(n):
        L = [n]
        while n != 1:
	    n = collatz(n)	
            L.append(n)            
        return L

def collatzlength(n):
    return len(collatzseq(n))



M = collatzlength(2)
for n in range(2, 1000000):
    if collatzlength(n) > M:
        M = collatzlength(n)
        A = n
        print n, M
    if n % 1000 == 0:
        print n, M
print A
    
# L = []
# for n in range(2, 1000000):
    # L.append(collatzlength(n))

# M = listoperations.listmax(L) 
# print M
# print L.index(M)
   


