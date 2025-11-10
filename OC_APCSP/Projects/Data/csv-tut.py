#import necessary libraries - PD, PLT, NP
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np  
import os

#create our data frame using our csv
data = pd.read_csv('apcspb3.csv')

#turn date into a dataframe(df)
df = pd.DataFrame(data)

#Validation 
print('-'*40)
print("Head of the dataframe:") #HotDF = First 5 lines
print(df.head())

print('-'*40)
print('Tail of the dataframe:') #TotDF = Last 5 lines
print(df.tail())

print('-'*40)
print('information about the dataframe:')#info = file types in DF
print(df.info())