def sortlist(list):
    length = len(list)
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



def switchindex(n):
    return -n - 1

def string_reverse(string):
    length = len(string) - 1
    string_init = string[length]
    stringbuilder_list = [string_init]
    string_so_far = string_init
    for n in range(1, length + 1):
        stringbuilder_list.append(string_so_far + string[switchindex(n)])
        string_so_far = stringbuilder_list[n]
    if string_so_far == stringbuilder_list[length]:
        return string_so_far
    else:
        print "Sorry, didn't work."

def palindromecheck(string):
	return string_reverse(string) == string  


def listpalindromes(n):
	L = []
	for k in range(n+1):
		K = str(k)
		if palindromecheck(K) == True:
			L.append(k)
	        else:
		    continue
	return L


def threedigit_factorization(n):
	factorization_check  = False
        for k in range(100, 1000):
		if n % k != 0:
			continue
		else:
			m = n / k
			M = str(m)
			if len(M) == 3:
				factorization_check = True
			        break
			else:
				continue
	return factorization_check
    
    
def eligible_palindromes(n):
	L = []
	for pal in listpalindromes(n):
		if threedigit_factorization(pal) == True:
			L.append(pal)
	        else:
			continue
	return L
    
def problem4(n):
	return listmax(eligible_palindromes(n))
    
print problem4(1000000)
    
    
    
