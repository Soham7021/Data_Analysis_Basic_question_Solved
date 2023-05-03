import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

a = pd.read_csv("Weather Data.csv",header=0)
b = pd.DataFrame(a)
print(b.head())
print(b.shape)
b['Date/Time'] = pd.to_datetime(b['Date/Time'])
print(b.info())
print(b.head())

# Q) Find all the unique "Wind Speed" values in the data 
print(" ")
uniq = b['Wind Speed_km/h'].unique()
print(uniq)
print(b.nunique())
print(b['Wind Speed_km/h'].nunique())

# Q) Find the number of times when the "Weather is exacly clear"

vlauecount = b.Weather.value_counts()
print(vlauecount)
# or 
vc = b[b.Weather=='Clear']
print(vc)
# or 
vc = b.groupby('Weather').get_group('Clear')
print(vc)

# Q) Find the number of times when th "Wind Speed Was exactly 4 km/h"
print(" ")
ws = b[b['Wind Speed_km/h']==4]
print(ws)
# or 
ws = b.groupby('Wind Speed_km/h').get_group(4)
print(ws)
# or
ws = b['Wind Speed_km/h'].value_counts()
print(ws)

# Q) Find out all the Null Values in the data 
print(b.isnull().sum())

# Q) Rename the column name "Weather" of the dataframe to "Weather Condition"

rname = b.rename(columns={'Weatehr' : 'Weather Condition'})
print(rname)

# Q) What is the mean "Visibility"
print(b.Visibility_km.mean())
# or
print(b.describe())

# Q) What is the Standard Deviation of "Pressure" in this data?
print("The std is : ",b.Press_kPa.std())
#or
print(b.describe())
print(" ")
# Q) Find all the instances when "Snow" was recprded. 
snwc = b[b['Weather']=='Snow']
print(snwc)
# or 
print(" ")
snwc = b[b['Weather'].str.contains('Snow')]
print(snwc)

# Q) Find all instances when "Wind Speed is Above 24" and visibility is 25

wsa = b[(b['Wind Speed_km/h']>24) & (b['Visibility_km']==25)]
print(wsa)

# Q) What is the mean value of each column against each "Weather Condition"?

vlu = b.groupby('Weather').mean()
print(vlu)

# Q) What is the Minimum & Maximum value of each column against each "Weather Condition"
print("_-_-_-_-_-_-_-_-_-_-_")
vlu = b.groupby('Weather').min()
print(vlu)
print(" ")
vlu = b.groupby('Weather').max()
print(vlu)

# Q) find all instances when:
# a) Weather is clear and Relative Humidity is greater than 50

# or 

# b) Visibility is above 40 

inst = b[(b['Weather']=='Clear') & (b['Rel Hum_%']>50) | (b['Visibility_km']>40)]
print(inst)

