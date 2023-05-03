import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt

df = pd.read_csv('covid_19_data.csv')
print(df.head())
print(df.count())
print(" ")
print(df.isnull().sum())
sns.heatmap(df.isnull())
plt.show()

# Q) Show the number of confirmed, deaths and recovered cases in each Region 
print(df.groupby('Region').sum().head(50))
print("or")
print(df.groupby('Region')['Confirmed'].sum().sort_values(ascending=False))
print("or")
print(df.groupby('Region')['Confirmed','Recovered'].sum())

# Q) Remove all the records where Confiremd cases is less than 10 

df = df[~(df.Confirmed < 10)]
print(df.info())
'''To check the values are removed or not, you will find the value at the 18th place is missing which was having confirmed less than 10'''
print(df.head(20))

# Q) In Which Region, maximum number of Confirmed cases were recored ?

print(df.groupby('Region').Confirmed.sum().sort_values(ascending=False).head(20))

# Q) In which Region, minimum number of Deaths cases were recorded ?
print(df.groupby('Region').Deaths.sum().sort_values(ascending=True).head(20))

# Q) How manu Confirmed,Deaths and recovered cases were reported from India till 29 April 2020 ?

print(df[df.Region == 'India'])

# Q) Sort The entire data wrt No. of Confirmed cases in ascending order 

print(df.groupby('Region').Confirmed.sum().sort_values(ascending=True))
print("OR")
print(df.sort_values(by = ['Confirmed'],ascending=True))

# Q) Sort The entire data wrt No. of Confirmed cases in decending order 

print(df.groupby('Region').Recovered.sum().sort_values(ascending=False))
print("OR")
print(df.sort_values(by = ['Recovered'],ascending=False))