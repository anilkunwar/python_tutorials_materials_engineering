import pandas as pd
################################reading input em variables##############################################
df=pd.read_csv('./fluid.csv', usecols=[0,1,2,3,4])
print("original data:", df)
df.loc[:, 'pressure'] *=1.0E+05 #converting pressure from bar to pascal
print("modified data:",df)
output_em=df.to_csv('./modified_fluid.csv', index=False)

