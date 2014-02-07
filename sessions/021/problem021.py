import listoperations


def d(n):
    L = []
    for i in range(1,n):
        if n%i == 0:
            L.append(i)
    return listoperations.listsum(L)
    
    
def amicablelist(n):
    A = []
    for k in range(1,n):
        if d(k) < n:
            if d(d(k)) == k and d(k) != k:
                A.append(k)
    return A            
                    
        
        


print listoperations.listsum(amicablelist(10000))

   
        
        
    


        
