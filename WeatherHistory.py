import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
file="/home/dangerous20/Downloads/weatherHistory.csv"
df=pd.read_csv(file)
df.head(10)
df1=df[['Formatted Date','Apparent Temperature (C)','Humidity']]
df1['Formatted Date']=pd.to_datetime(df1['Formatted Date'],utc=True)
df2=df1.set_index('Formatted Date')
df2.head(10)
df2=df2.resample("MS").mean()
plt.plot(df2)
df_april=df2[df2.index.month==4]
plt.plot(df_april)
'''We can clearly see that there is a sharp rise in temperature in the year of 2009 whereas
   there is a fall in temperature in the year of 2015. Hence we can conclude that global warming
   has caused an uncertainty in temperature over the past 10 years while the average humidity as 
   remained constant throughout the 10 years.'''
