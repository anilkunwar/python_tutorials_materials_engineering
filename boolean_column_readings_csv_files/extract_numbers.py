#tested in python 3.6.5
import pandas as pd
#import numpy as np
################################useful for reading timestep outputs reading from paraview
###################################################
#####write time (wt) is the dataframe for temperature (variable)
wt=pd.read_csv('temperature.csv',usecols=[0])
wt["number"]=wt["value"].str.extract('(\d+)').astype(float)
time_output=wt.to_csv('temperature_result.csv', index=False)
#print the second column [1] number 
temperature_value=wt["number"].min() # this works as there is no other data in the value column [0]
#temperature_value=wt["number"].max() # this works as there is no other data in the value column [0]
print(str(temperature_value))

