#Python codes
# Reference: https://www.w3resource.com/python-exercises/pandas/python-pandas-data-frame-exercise-62.php
#  https://www.w3resource.com/python-exercises/pandas/python-pandas-data-frame-exercise-63.php
import pandas as pd
#df=pd.read_csv('./../old_dataset.csv',usecols=[0,1])
df=pd.read_csv('./old_dataset.csv') # Columns not mentioned because some rows have no defined columns
# choose the regime of diffuse interface between t,he phases
#df1 = df.iloc[num1:num2] # use with care to use rows from middle of total observations
#df1 = df.iloc[num1:] # Deletes all the preceding rows  to (num1+2)th row
#df1 = df.iloc[:num2] # Deletes all the rows following (num2+2)th row
df1 = df.iloc[2:] # Extract data after the first two rows + index row
output1=df1.to_csv('./lower_two_rows_new_dataset.csv', index=False)
df1 = df.iloc[:2] # Extract data upto the first two rows + index row 
output2=df1.to_csv('./upper_two_rows_new_dataset.csv', index=False)

