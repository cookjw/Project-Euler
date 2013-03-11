
    
# NOTE: This code produces the right answer at n = 999,999 instead of n = 1,000,000 for some reason. (Figure out??)


def lexnext(entry):
    if [i for i in range(len(entry)-1) if entry[i] < entry[i+1]] != []:
        I = max([i for i in range(len(entry) -1) if entry[i] < entry[i+1]])
        a = entry[I]
        b = min([x for x in entry[I+1:] if x > entry[I]])
        entry[entry.index(b)] = a
        entry[I] = b        
        entry[I+1:] = sorted(entry[I+1:])
        return entry
    else:
        
        print "Error! at %s" % entry
        print entry

entry = [0,1,2,3,4,5,6,7,8,9]

n = 1

# print len(entry)
# print lexnext(entry)

# while n < 1000001:
    # # if n > 1 and entry == [0,1,2,3,4,5,6,7,8,9]:
        # # print "Error at %s, %s !" % (n, entry)    
    # entry = lexnext(entry)
    # n = n+1
    # if n % 1000 == 0 or n == 999999:
        # print n, entry
        
while n < 1000000:
    n = n+1
    entry = lexnext(entry)

    
    
print n, entry

# print lexnext(entry)
    
# print lexnext([6,1,2,3,4,9,8,7,5])

# print lexnext([6,8,2,3,4,5,1,9,7])

# print lexnext([0,1,2,3,4,5,6,8,9,7])


#[2,7,8,3,9,1,5,4,6,0]