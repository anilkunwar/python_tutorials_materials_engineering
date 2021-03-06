# Tested using python 3.6.5
# This python program uses pandas and its dataframe to calculate the 
# temperature difference at the two ends of a phase at the datapoints touched by a x-line (arrow AB)
# References
##########################################################################################################
#http://www.datasciencemadesimple.com/get-minimum-value-column-python-pandas/
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.subtract.html
#https://stackoverflow.com/questions/48350850/subtract-two-columns-in-dataframe
#https://medium.com/dunder-data/selecting-subsets-of-data-in-pandas-39e811c81a0c
#https://medium.com/dunder-data/selecting-subsets-of-data-in-pandas-39e811c81a0c
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html
#https://datatofish.com/export-dataframe-to-csv/
# Several python functions illustrated
#https://www.dev2qa.com/python-pandas-read-write-csv-file-and-convert-to-excel-file-example/
#https://www.geeksforgeeks.org/saving-a-pandas-dataframe-as-a-csv/
#https://www.geeksforgeeks.org/boolean-indexing-in-pandas/
#https://medium.com/dunder-data/selecting-subsets-of-data-in-pandas-6fcd0170be9c
#http://pandas.pydata.org/pandas-docs/stable/user_guide/io.html
#https://www.shanelynn.ie/select-pandas-dataframe-rows-and-columns-using-iloc-loc-and-ix/
#https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
#https://programminghistorian.org/en/lessons/working-with-text-files
#https://www.quora.com/How-do-I-write-the-output-of-a-function-to-a-text-file-in-python
#https://stackoverflow.com/questions/50893146/what-is-the-correct-format-to-write-float-value-to-file-in-python
##########################################################################################################
#Python codes
import pandas as pd
df=pd.read_csv('phi_temperature.csv',usecols=[0,1])
# choose the regime of diffuse interface between the phases
criteria_1=df['phi']>=0.5
criteria_2=df['phi']<1.0
criteria_all=criteria_1 & criteria_2
df=df[criteria_all]
output=df.to_csv('./selected_result.csv', index=False)
#lower temperature for the phase with phi=1.0
right_edge=df['temperature'].min()
# high temperature for the phase with phi=1.0
left_edge=df['temperature'].max()
delta_temperature=left_edge-right_edge
print(delta_temperature)
# writing the output to the external file
fname=open('temperature_output.dat','w')
fname.write('the temperature difference is:' +str(delta_temperature))
# To append something additional on an existing file
#fname=open('temperature_output.dat','a')
#fname.write('\n' + 'the temperature difference is:' +str(delta_temperature))
fname.close


