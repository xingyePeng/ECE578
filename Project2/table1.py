# use file 2023.AS-rel.txt

import pandas as pd
import numpy as np
import pdb
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

np.set_printoptions(suppress=True)
# Find Globle degree
parsed_data=[]

with open("2023-rel.txt") as AS:
    for line in AS:
        values=line.strip().split('|')[:-2]
        #print(values)  
        parsed_data.append(values)
    
my_array=np.array(parsed_data,dtype=int)


# Find unique AS numbers in the first column
AS_unique = np.unique(my_array[:,0])

glbl_allvalue=[]
glbl_alldegree=[]

### Find Globle degree
# Count occurrences of each unique AS number
for value in AS_unique:
    global_degree = np.array([np.count_nonzero(my_array[:] == value)])
    global_value=np.array([value])
    
    glbl_allvalue=np.concatenate((glbl_allvalue,global_value))
    glbl_alldegree=np.concatenate((glbl_alldegree,global_degree))

glbl_array=np.transpose(np.stack((glbl_allvalue,glbl_alldegree)))
#print(glbl_array.shape)

# get the indice based on sorted global degree
sorted_indice=np.argsort(-glbl_array[:,1])
# ASes rank
sorted_array=glbl_array[sorted_indice][:,0]
#print(sorted_array)
# pdb.set_trace()

#Initialize the clique S = {AS1}
S={sorted_array[0]} 

connected_to_all=1
# counter for counting the number
counter=0
# Iterate through ASes in the sorted list
for i in range(1, len(sorted_array)):
    current_AS = sorted_array[i]
    # Find all row index that AS appears
    rows_currentAS=np.where(my_array==current_AS)[0]

 # Check if the current AS is connected to all ASes in S
    for AS in S:
        # Find all the row that AS appears
        rows_AS=np.where(my_array==AS)[0]
        # share common row index

        if np.intersect1d(rows_AS, rows_currentAS).size == 0:
            connected_to_all = False
            break  # No need to check further if not connected
    
        # If current_AS is connected to all ASes in S, add it to S
    if connected_to_all:
        S.add(current_AS)



        """ if (np.intersect1d(rows_AS, rows_currentAS).size > 0):
             # counter for counting the number
             counter=counter+1
             
     
        
    if counter==len(S):
            S.add(current_AS)
            i=i+1 """
            


               
pdb.set_trace()

