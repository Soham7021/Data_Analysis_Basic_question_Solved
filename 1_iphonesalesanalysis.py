# For the iphone sales analysis task, i have collected a dataset containing data about the sales of iphones in india on flipkart . it will be an ideal dataset to analyze the sales of iphones in india.
import numpy as np 
import pandas as pd 
import plotly.express as px
import plotly.graph_objects as go 
data = pd.read_csv("apple_products.csv")
# print(data.head())
# print(data.describe())
# print(data.isnull().sum())

highrated=data.sort_values(by=["Star Rating"],ascending=False)
highrated = highrated.head(10)
# print(highrated['Product Name'])
iphone = highrated['Product Name'].value_counts()
# print(iphone)
label = iphone.index
# print(label)
count = highrated['Number Of Ratings']
# print(count)
fig = px.bar(highrated,x=label,y=count,title="Number of rating of highest rated Iphone")
# fig.show()

# For number of review's 

iphone = highrated['Product Name'].value_counts()
# print(iphone)
label = iphone.index
# print(label)
count = highrated['Number Of Reviews']
# print(count)
fig = px.bar(highrated,x=label,y=count,title="Number of rating of highest rated Iphone")
# fig.show()


figr = px.scatter(data_frame=data,x="Number Of Ratings",y="Sale Price",size="Discount Percentage",title="Relationship between sale price and number of ratings of iphones")
figr.show()

# for discount 

figr = px.scatter(data_frame=data,x="Number Of Ratings",y="Discount Percentage",size="Sale Price",title="Relationship between Discount Percentage and number of ratings of iphones")
figr.show()