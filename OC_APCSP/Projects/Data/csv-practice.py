#import necessary libraries - PD, PLT, NP
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np  


#create our data frame using our csv
data = pd.read_csv('xmas.csv')

#turn date into a dataframe(df)
df = pd.DataFrame(data)

'''
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
print('Spirit Values:')
print(df['Spirit'].value_counts())

#see how pie relates to nap time
print('_-'*40)
print('Average Spirit time by Music start choice:')
print(df.groupby('Spirit')['MStart'].mean())
'''

# lets actaully start coding our visualizations now


#PIE choice bar graph
df['Spirit'].value_counts().plot(kind='bar', color=['blue','orange','green','red', ], edgecolor='black')

#scatter plot of NAP vs PIE
#df.plot.scatter(df['Spirit'], df['MStart'])

#extra 
plt.title('Favorite Pie Choice')
plt.xlabel('Pie Type')
plt.ylabel('# of People')
plt.xticks(rotation=45)
plt.tight_layout()
#end of extra 
plt.show()
