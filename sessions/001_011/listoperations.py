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


def sortlist(list):
    length = len(list)       
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
    
def listsum(list):
    length = len(list)
    total = list[0]
    for i in range(1,length):
        total = total+list[i]
    return total
    
def listprod(list):
    length = len(list)
    product = list[0]
    for i in range(1,length):
        product = product*list[i]
    return product
        