#References:
#https://stackoverflow.com/questions/33768122/python-pandas-dataframe-how-to-multiply-entire-column-with-a-scalar
#https://towardsdatascience.com/pandas-tips-and-tricks-33bcc8a40bb9
#https://www.pybloggers.com/2018/11/pandas-read-csv-tutorial/
#https://realpython.com/python-csv/
#https://chrisalbon.com/python/data_wrangling/pandas_saving_dataframe_as_csv/
import pandas as pd
################################reading input cfd variables##############################################
df=pd.read_csv('./fluid.csv', usecols=[0,1,2,3,4])
print("original data:", df)
#####################modifying the data of "pressure" columns##############################
####################converting pressure from bar to Pascal#################################
df.loc[:, 'pressure'] *=1.0E+05 #converting pressure from bar to Pascal
print("modified data:",df)
#####################exporting the modified cfd variable data##################################
output_cfd=df.to_csv('./modified_fluid.csv', index=False)

