import listoperations

f = open("problem011array.txt") # Note: file must be in directory where python.exe is located, not directory where this script is located (in contrast to import commands).

lines = f.readlines()

def line_to_numlist(line): # converts individual line from string of text to list of numbers
        L = []    
        for n in range(len(line)):
            if line[n] == " " or line[n] == "\n":
                L.append(int(line[n-2]+line[n-1]))
            else:
                 continue
        return L


def createarray(lines):  # makes a list of the lists of numbers (i.e. the rows of the array), equivalent to a numerical array.      
    L = []
    for line in lines:
        L.append(line_to_numlist(line))
    return L
    

def horizontalproducts(array): # lists the horizontal products
    L = []
    number_of_rows = len(array)
    number_of_columns = len(array[1])
    for i in range(number_of_rows):
        for j in range(number_of_columns - 4):
            L.append(array[i][j]*array[i][j+1]*array[i][j+2]*array[i][j+3])
    return L

def verticalproducts(array): # lists the vertical products 
    L = []
    number_of_rows = len(array)
    number_of_columns = len(array[1])
    for i in range(number_of_rows - 4):
        for j in range(number_of_columns):  
            L.append(array[i][j]*array[i+1][j]*array[i+2][j]*array[i+3][j])
    return L                

def updiagonalproducts(array): # lists the products on "positive-slope" diagonals
    L = []
    number_of_rows = len(array)
    number_of_columns = len(array[1])
    for i in range(number_of_rows - 4):
        for j in range(number_of_columns - 4):
            if i >= 3 and j < number_of_columns - 4:
                L.append(array[i][j]*array[i-1][j+1]*array[i-2][j+2]*array[i-3][j+3])            
            else:
                continue
    return L
            
            
def downdiagonalproducts(array): # lists the products on "negative-slope" diagonals
    L = []
    number_of_rows = len(array)
    number_of_columns = len(array[1])
    for i in range(number_of_rows - 4):
        for j in range(number_of_columns - 4):
            if i < number_of_rows - 4 and j < number_of_columns - 4:
                L.append(array[i][j]*array[i+1][j+1]*array[i+2][j+2]*array[i+3][j+3])
            else:
                continue
    return L   
    
    
def diagonalproducts(array): # lists all the diagonal products
    return updiagonalproducts(array) + downdiagonalproducts(array)

def adjacentproducts(array): # combines all of the above into a single list
    return horizontalproducts(array) + verticalproducts(array) + diagonalproducts(array)


array = createarray(lines)
print listoperations.listmax(adjacentproducts(array))
    
        

