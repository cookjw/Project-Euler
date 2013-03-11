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
    