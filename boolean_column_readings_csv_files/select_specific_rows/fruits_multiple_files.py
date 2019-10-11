#Use append functionality to collect data from multiple files
#jonathansoma.com/lede/foundations-2017/classes/working-with-many-files/class/
#thispointer.com
#marsja.se/pandas-read-csv-tutorial-to-csv/
import pandas as pd
import numpy as np
import glob
#################################################################################
#Creating a list of column
#columns=[0,1,2]
columns=[1]
#* means match anything
# glob can find the full path unlike os, fmatch , for which we need to provide path
csv_files=glob.glob("date*.csv")
csv_files_sorted=sorted(glob.glob("date*.csv"))
#Create an empty list
#frames = []
#################################################################################
#Having a list of filenames, we can convert those into list of dataframes
#Choose only second rows of each file (3rd rows including the headers)
rows_to_keep=[2]
#rows_to_keep=[2,3] #multiple rows
####Iterate over csv files
#for csv_file in csv_files:
    #dfs=pd.read_csv(csv_file, usecols=columns, skiprows=lambda x: x not in rows_to_keep,dtype = object)
    #frames.append(dfs)
####################################################################################################
f_handle=open('Tb-unsortedglob.csv','a')
f_sorted=open('Tb-sortedglob.csv','a')
fname=open('Tb-noglob.dat','a')
#####case _1###########################################
####use glob csv not unsorted file number#############
for csv_file in csv_files:
    df1s=pd.read_csv(csv_file, usecols=columns, skiprows=lambda x: x not in rows_to_keep,dtype = object)
    ########save or append the predicted values
    test1=df1s.to_csv(index=False)
    #f_handle.write('\n'+str(test1))
    #f_handle=open('Tb.csv','a')
    f_handle.write('\n'+str(test1))
    #frames.append(dfs)
#####case _2###########################################
####use glob csv sorted file number#############
for csv_file_sorted in csv_files_sorted:
    df2s=pd.read_csv(csv_file_sorted, usecols=columns, skiprows=lambda x: x not in rows_to_keep,dtype = object)
    ########save or append the predicted values
    test2=df2s.to_csv(index=False)
    #f_handle.write('\n'+str(test1))
    #f_handle=open('Tb.csv','a')
    f_sorted.write(str(test2))
    #frames.append(dfs)
#########case-3#####################################################################################
####instead of glob the number range has been used to maintain order of csv file number#############
#####if range is (1,5), it goes from 1,2,3,4
for number in range(1,5):
    filename="./date0{}.csv".format(number)
    df3s=pd.read_csv(filename, usecols=columns, skiprows=lambda x: x not in rows_to_keep,dtype = object)
    ########save or append the predicted values
    test3=df3s.to_csv(index=False)
    #f_handle.write('\n'+str(test1))
    #f_handle=open('Tb.csv','a')
    fname.write('\n'+str(test3))
    #frames.append(dfs)

