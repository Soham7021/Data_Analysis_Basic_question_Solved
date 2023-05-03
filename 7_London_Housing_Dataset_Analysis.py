import numpy as np 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('London_Housing_Data.csv')
print(df.head())
print(df.count())
print(df.isnull().sum())
sns.heatmap(df.isnull())
# plt.show()
print(" ")
# Q1) Conver the DataType of "Date" column to Date-time format
print(df.dtypes)
df['date'] = pd.to_datetime(df['date'])
print(df.dtypes)
print(" ")
print(" ")

# Q2) Add a new column 'year' in the dataframe which contains years only. 

df['year'] = df['date'].dt.year # this will add one new column naming year and select only years from the date column and add it to the year column we can also change the year column to the month and day using dt.month and dt.day
print(df.head())

# Q3) Remove the columns 'year' from the dataframe. 
df.drop(['year'],axis=1,inplace = True)
print(df.head())
print(" ")
print(" ")
# Q4) Show all the records where 'No fo Crimes' is 0. and how many such records are there
print(df[df.no_of_crimes == 0])
print(len(df[df.no_of_crimes == 0]))

#Q5) What is the minimum and maximum average price per year in england 

df['year'] = df['date'].dt.year
df1 = df[df.area == 'england']
print(df1.groupby('year').average_price.max())
print(df1.groupby('year').average_price.min())
print(df1.groupby('year').average_price.mean())
