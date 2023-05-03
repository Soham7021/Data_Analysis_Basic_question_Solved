# Screen time analysis is the task of analyzing and creating a report on which applications and websites are used by the user for how much time, apple devices have one of the best ways of creating a screen time report. 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import plotly.express as px 
import plotly.graph_objects as go 

data = pd.read_csv("Screentime - App Details.csv")
# print(data.head())
# print(" ")
# print(data.isnull().sum())
# print(data.describe())
fig = px.bar(data_frame=data, x ="Date", y="Usage", color="App",title="Usage Graph")
fig.show()

# for notification 
fig = px.bar(data_frame=data, x ="Date", y="Notifications", color="App",title="Notification Graph")
fig.show()

# for times opened 
fig = px.bar(data_frame=data, x ="Date", y="Times opened", color="App",title="Times Opened Graph")
fig.show()


fig = px.scatter(data_frame=data, x = "Notifications", y = "Usage", size="Notifications", trendline="ols",title="Relationship Bet number of notification and amount of usage")
fig.show()