import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

data = pd.read_csv('Cars Data1.csv')
# print(data.head(5))

# Q) Find all Null Value in the dataset . if there is any Null value in any column, then fill if with the mean of that column 

print(data.isnull().sum())
fill = data['Cylinders'].fillna(data['Cylinders'].mean(),inplace=True)#inplace do the permanent changes 
print(data.isnull().sum())
'''fill = data.fillna(data.mean(),inplace=True)
print(data.isnull().sum())'''
# data.dropna(inplace=True)
# print(data.isnull().sum())

# Q) Check What are the different types of Make are ther in our dataset. and what is the count of each Make in the data? 
print(data['Make'].unique())
print(data['Make'].value_counts())

# Q) Show all the records where Origin is Asia or Europe 
origin = data[(data['Origin']=='Asia') | (data['Origin']=='Europe')]
print(origin)
# or 
origin = data[data['Origin'].isin(['Asia','Europe'])]
print(origin)

# Q) Remove all the records(rows) where Weight is above 4000
rmv = data[~(data['Weight'] > 4000)]#'~' this sign is to remove the element's
print(rmv)
print(data)

# Q) Increase all the values of "MPG_City" coumn by 3 
data['MPG_City'] = data['MPG_City'] + 3
print(data['MPG_City'])
# or 
'''data['MPG_City'] = data['MPG_City'].apply(lambda x:x+3)
print(data['MPG_City'])'''