#jonathansoma.com/lede/foundations-2017/classes/working-with-many-files/class/
#https://thispointer.com/python-pandas-how-to-convert-lists-to-a-dataframe/
#marsja.se/pandas-read-csv-tutorial-to-csv/
#https://pandas.pydata.org/pandas-docs/version/0.20/merging.html
import pandas as pd
import numpy as np
import glob
#* means match anything
# glob can find the full path unlike os, fmatch , for which we need to provide path
csv_files=glob.glob("date*.csv")
#Having a list of filenames, we can convert those into list of dataframes
#Choose only second rows of each file (3rd rows including the headers)
#https://stackoverflow.com/questions/39339142/pandas-read-csv-and-keep-only-certain-rows-python
rows_to_keep=[2]
#rows_to_keep=[2,3] #multiple rows
dfs=[pd.read_csv(csv_file, skiprows=lambda x: x not in rows_to_keep) for csv_file in csv_files]
#df=pd.append(dfs)
df=pd.concat(dfs,sort=False)
#df=pd.concat(dfs,sort=True)
type(dfs)
print(dfs)
df.to_csv("MultipleDfs.csv", index=False)
