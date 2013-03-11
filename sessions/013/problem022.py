import listoperations


Alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def Alphaindex(Letter): # requires capital letter!
    return Alphabet.index(Letter)
    
def Alphaposition(Letter): # requires capital letter!
	return Alphaindex(Letter) + 1
    
def Alphavalue(WORD): # requires capital letter!
    L = []
    for Letter in WORD:
        L.append(Alphaposition(Letter))
    return listoperations.listsum(L)

    
f = open("names.txt") # Remember that file must be in Python directory!
document = f.read()
length = len(document)

quotestatus = 0
L = []
for position in range(length):
    if document[position] == "\"":
        if quotestatus % 2 == 0:
            L.append(quotestatus)
            quotestatus = quotestatus + 1 
        elif quotestatus % 2 == 1:
            L.append(quotestatus + 1)
            quotestatus = quotestatus + 1            
    else:
        L.append(quotestatus)        
     

maxquotestatus = listoperations.listmax(L)
M = []
for quotestatus in range(maxquotestatus + 1):
    if quotestatus % 2 == 1:
        M.append(listoperations.getindices(quotestatus, L))
    else:
        continue    


N = []
for wordplace in M:
    word = ""
    for position in wordplace:
        word = word + document[position]
    N.append(word)         


Alphabetical_Namelist = listoperations.sortlist(N)


def Namelist_Position(NAME):
    return Alphabetical_Namelist.index(NAME) + 1

def Namescore(NAME):
    return Alphavalue(NAME) * Namelist_Position(NAME)
    
Namescores = []
for NAME in Alphabetical_Namelist:
    Namescores.append(Namescore(NAME))

print listoperations.listsum(Namescores)







 
