import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

df = pd.read_csv("Police Data.csv")
print(df.isnull().sum())
# Q) Remove the column that only contains missing values 

new_df = df.drop(columns='country_name')
print(new_df.head(5))

# Q) For Speeding, were Men or Women stopped more often? 

Speeding = df[df.violation == 'Speeding'].driver_gender.value_counts()
print(Speeding)
''' M    25517
    F    11686
    Name: driver_gender, dtype: int64'''


# Q) Does gender affect who gets searched during a stop ? 

search = df[df.search_conducted == True].driver_gender.value_counts()
print(search)
''' M    2113
    F     366
    Name: driver_gender, dtype: int64'''

# OR 

search = df.groupby('driver_gender').search_conducted.sum()
print(search)

# Q) What is the mean stop_duration ? 
print(df.describe())
'''as we can see the data type of the stop duration is not int so we will have to first convert it to the int , thus doing that we cannot do it directly because it is diffrent type of string that the number mentioned there are not clear thus first we will find the all uniq values of the stop_duration and using map we will convert it to the integer type'''

print(df.stop_duration.value_counts)
df['stop_duration'] = df['stop_duration'].map({'0-15 Min':7.5,'16-30 Min':24,'30+ Min':45})
print(df['stop_duration'].mean())
'''ans is : 12.187420698181345'''


# Q) Comapare the age distribution for each violation 

violation = df.groupby('violation').driver_age.describe()
print(violation)