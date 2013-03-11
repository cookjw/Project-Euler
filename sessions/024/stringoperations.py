def switchindex(n):
    return -n - 1
    

# def string_reverse(string):
    # length = len(string) - 1
    # string_init = string[length]
    # stringbuilder_list = [string_init]
    # string_so_far = string_init
    # for n in range(1, length + 1):
        # stringbuilder_list.append(string_so_far + string[switchindex(n)])
        # string_so_far = stringbuilder_list[n]
    # if string_so_far == stringbuilder_list[length]:
        # return string_so_far
    # else:
        # print "Sorry, didn't work."
        
def string_reverse(string):
	letters = [x for x in string]
	backwards = [letters[-i-1] for i in range(len(letters))]
	return ''.join(backwards)


# def remove_initial_letter(string):
    # length = len(string)
    # stringlist = []
    # for letter in string:
        # stringlist.append(letter)
    # newstring = ""
    # for index in range(1,length):
        # newstring = newstring + stringlist[index]
    # return newstring
    
    
def remove_initial_letter(string):
    return ''.join([x for x in string[1:]])
    
    
# def totalsplit(string):
    # L = []
    # for letter in string:
        # L.append(letter)
    # return L
    
def totalsplit(string):
    return [x for x in string]
    
def switch(string, index1, index2):
	return string[:index1] + string[index2] + string[index1+1:index2] + string[index1] + string[index2+1:]