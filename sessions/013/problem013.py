import listoperations

def first10digits(number):
    string = str(number)
    first10 = ""
    for k in range(10):
        first10 = first10 + string[k]
    return first10

f = open("problem013array.txt")

lines = f.readlines()

L = []
for line in lines:    
    intline = int(line)
    L.append(intline)   

    
sum = listoperations.listsum(L)
print first10digits(sum)
    