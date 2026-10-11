import numpy as np
import random 

position_found = []
loop_array = 40



def createArray():
    original_set = np.zeros((40,40), dtype= int) #dtype = data type Creating a 2d arrary of zeros
    print(original_set)

#We use the original determine neighbours and update state - to new state
def NewStateArray():
    pass

#Creating the set: 10 - 30% alive rate
def set_creation():
    b = createArray()
    values = []
    sum = 0

    for i in range(5):
        x   = random.randint(10,30)
    if x >= 15:
        values.append(x)
    for i in len(values):
        sum = sum + values[i]
    for r in b :
        for c in b:
           if (sum / (len(values)) >= 15 ):
             b[r,c] = 1
        
    return b   

def neighbours():
    current_matrix = set_creation()
    for r,c  in np.argwhere(current_matrix == 1): #Determine all non-zero elements in an array argwhere finds non-zero position in an array
        position_found.append[r,c]
    for i in position_found:
        print(i)
     
#Determine Each cell - Calculate the number of '1' within a 8 index range     
def underpopulation(): 
    pass 


neighbours()