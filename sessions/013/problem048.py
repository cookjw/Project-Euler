import numberoperations


def zapgauss(n):
    total = 0
    for k in range(1, n+1):
        total += k**k
    return total
    
print numberoperations.last10digits(zapgauss(1000))