# Tested using python 3.6.5
# This python program uses pandas and its dataframe to calculate the 
# temperature difference at the two ends of a phase at the datapoints touched by a x-line (arrow AB)
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


