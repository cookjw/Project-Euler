def Gauss(n):
	if n == 0:
		return 0
	else:
		return n + Gauss(n-1)
        

def squareGauss(n):
	if n == 0:
		return 0
	else:
		return n**2 + squareGauss(n-1)

print (Gauss(100))**2 - squareGauss(100)        