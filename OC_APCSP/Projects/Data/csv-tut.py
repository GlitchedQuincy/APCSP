#import necessary libraries - PD, PLT, NP
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np  


#create our data frame using our csv
data = pd.read_csv('OC_APCSP\Projects\Data\cspb3.csv')

#turn date into a dataframe(df)
df = pd.DataFrame(data)

#Validation 
print('_-'*40)
print("Head of the dataframe:") #HotDF = First 5 lines
print(df.head())

print('_-'*40)
print('Tail of the dataframe:') #TotDF = Last 5 lines
print(df.tail())

print('_-'*40)
print('information about the dataframe:')#info = file types in DF
print(df.info())

print('_-'*40)
print('Statistical Summary of the dataframe:') #StatDF = Statistical summary of DF
print(round(df.describe(),1))

#see value counts of pie choices 
print('_-'*40)
print('Pie Value Counts:')
print(df['PIE'].value_counts())

#see how pie relates to nap time
print('_-'*40)
print('Average Nap time by Pie choice:')
print(df.groupby('PIE')['NAP'].mean())