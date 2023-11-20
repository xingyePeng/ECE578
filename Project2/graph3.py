# use file routeviews-rv2-20231116-140.txt
import pandas as pd
import numpy as np
import pdb
import matplotlib.pyplot as plt

parsed_data=[]
with open ("routeviews-rv2-20231116-140.txt") as AS:
    for line in AS:
        values=line.strip().split('\t')
        #print(values)  
        parsed_data.append(values)
    
my_array=np.array(parsed_data)


# Find unique AS numbers in the first column
AS_unique = np.unique(my_array[:,2])



for value in AS_unique:
      if(my_array[:,2] == value):
           IP_unique= set(my_array[:, 0]) 
           for i in IP_unique:
                if(my_array[:0]==i):
                     
          
         
pdb.set_trace()