#!/usr/bin/env python
# coding: utf-8

# #### installing some required libraries

# In[1]:


#pip install seaborn==0.11.0


# In[2]:


#pip install datashader


# In[3]:


#pip install contextily


# # 1. Import Libraries

# In[4]:


import pandas as pd
import numpy as np
import os
import plotly.express as px
import matplotlib.pyplot as plt
from shapely.geometry import Point
import geopandas as gpd
from geopandas import GeoDataFrame
import contextily as ctx
from bokeh.plotting import figure, show
import folium
import datetime
import seaborn as sns
import datashader as ds
import datashader.transfer_functions as tf
from colorcet import fire, kbc, bmw, gray


# **Connect Google drive with google colab**

# In[5]:


#from google.colab import drive
#drive.mount('/content/drive')


# Loading the dataset and creating a dataframe.

# In[6]:


#df = pd.read_csv('/content/drive/MyDrive/Capstone_Project/UK_Accident.csv')
df = pd.read_csv('./UK_Accident.csv')
print(df)


# # 2. Initial Data Analysis

# ## A. Dataset Overview

# In[7]:


df.head()


# Information aboout the columns.

# In[8]:


df.info()


# Shape of dataframe

# In[9]:


df.shape


# In[10]:


list(df.columns.values)


# # B. Data Cleaning

# #### Removing some unwanted columns

# In[11]:


df.drop(['Unnamed: 0','Accident_Index','LSOA_of_Accident_Location','Location_Northing_OSGR','Location_Easting_OSGR'], axis = 1, inplace = True)
df.head()


# #### Removing some null values from dataset.

# In[12]:


df.dropna(subset=['Longitude','Time','Pedestrian_Crossing-Human_Control','Pedestrian_Crossing-Physical_Facilities'], inplace=True)


# In[13]:


print(df.isnull().sum()) #showing how many null values in the column.


# In[14]:


#df.corr()


# In[15]:


fig, ax = plt.subplots(figsize=(20,10))
sns.heatmap(df.corr(), annot=True)
fig.show()


# The graph shows the correlation between all the features or variables in the dataset. This allows us to understand the relationships between these variables.
# 
# This graph can help us in feature engineering and data analysis because it guides decisions related to feature selection, creation and model development.

# #### Change week days number into day of week

# In[16]:


days = {1:'Sunday', 2:'Monday', 3:'Tuesday', 4:'Wednesday', 5:'Thursday', 6:'Friday', 7:'Saturday'}
df['week_days'] = df['Day_of_Week'].map(days)


# #### Rearrange and change area types

# In[17]:


df['Urban_or_Rural_Area'] = df['Urban_or_Rural_Area'].replace([3], 2, inplace=False)
area_type = {1:'Urban', 2:'Rural'}
df['area_type'] = df['Urban_or_Rural_Area'].map(area_type)


# #### Get month and day of month from date column

# In[18]:


df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['Day of Month'] = df['Date'].dt.day
df['Month'] = df['Date'].dt.month


# #### GET hours from Hour column

# In[19]:


def hour(string):
    s=string[0:2]
    return int(s)
df['Hour']=df['Time'].apply(lambda x: hour(x))


# Within the dataset, three distinct levels of accident severity were originally categorized as "1 - fatal," "2 - serious," and "3 - slight."
# 
# However, for analysis purposes, these have been consolidated into two categories: "1 - slight" and "2 - fatal/serious."

# In[20]:


df['Accident_Severity'] = df['Accident_Severity'].replace([1], 2, inplace=False)
df['Accident_Severity'] = df['Accident_Severity'].replace([3], 1, inplace=False)


# In[21]:


df.head()


# # C. Visualization

# # I. Severity of accident

# In[22]:


df_accidents = df['Accident_Severity'].value_counts()[df.Accident_Severity.unique()]
df_accidents


# In[23]:


# Create a pie chart using Matplotlib
accident_severity = df['Accident_Severity'].value_counts()
df_accident_severity = pd.DataFrame(accident_severity)
df_accident_severity = df_accident_severity.reset_index()
df_accident_severity.columns = ['Accident Severity', 'Total']
#plt.style.use("dark_background")
plt.figure(figsize=(6, 6))
explode = [0, 0.1]
colors = ['#de425b','#83af70']
plt.pie(df_accident_severity['Total'], labels=df_accident_severity['Accident Severity'], autopct='%1.1f%%', startangle=140, colors=colors, explode = explode)
plt.title('Accident Severities 1-Slight 2-Fatal/Serious')
plt.axis('equal')
sns.set(style="darkgrid")
sns.despine()
sns.set_palette('Set3')
plt.legend(df_accident_severity['Accident Severity'], title="Accident Severity", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
plt.show()


# Based on the visualization, it can be inferred that a substantial majority, approximately 85%, of accidents are categorized as "slight," while the remaining 15% of accidents are classified as "serious" or "fatal."

# # II. TIME OF THE ACCIDENTS

# ### I. Accidents occured throught the Years

# In[24]:


sns.set(style="darkgrid")                                 #creating bar graph using seaborn
plt.figure(figsize=(15,5))
yearplot = sns.countplot(x='Year',data=df)
yearplot.set(xlabel='Years', ylabel='Count')
for p in yearplot.patches:
    height = p.get_height()
    yearplot.text(p.get_x()+p.get_width()/2.,
      height + 3,
      '{:1.2f}'.format((height/len(df))*100)+'%',
      ha="center")
plt.show()


# The data illustrates a discernible downward trend in accident rates as the years progress.

# ### II. Accidents happend on months

# In[25]:


sns.set(style="darkgrid")                               #creating bar graph using seaborn
plt.figure(figsize=(15,5))
monthplot = sns.countplot(x='Month',data=df)
monthplot.set(xlabel='Month', ylabel='Count')
for p in monthplot.patches:
    height = p.get_height()
    monthplot.text(p.get_x()+p.get_width()/2.,
      height + 3,
      '{:1.2f}'.format((height/len(df))*100)+'%',
      ha="center")
monthplot.set(xticklabels=['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC'])
plt.show()


# It's evident that the accident rates exhibit a relatively consistent pattern across all months.

# ### III. Accidents occured on days of week

# In[26]:


sns.set(style="darkgrid")                                 #creating bar graph using seaborn
plt.figure(figsize=(15,5))
weekplot = sns.countplot(x='week_days',data=df)
weekplot.set(xlabel='Day of week', ylabel='Count')
for p in weekplot.patches:
    height = p.get_height()
    weekplot.text(p.get_x()+p.get_width()/2.,
      height + 3,
      '{:1.2f}'.format((height/len(df))*100)+'%',
      ha="center")
plt.show()


# The data reveals that Friday has the highest frequency of accidents, while Sunday consistently ranks as the day with the lowest occurrence.

# ### IV. Accidents based on day of month

# In[27]:


acc_months = df['Day of Month'].value_counts()
df_month_acc = pd.DataFrame(acc_months)
df_month_acc = df_month_acc.reset_index()
df_month_acc.columns = ['Day of Month', 'Total']
fig = px.bar(df_month_acc, y='Total', x='Day of Month', text_auto='.2s',hover_data=['Total'], color='Total', title="Accidents across different days of the month")
fig.show()
#template="plotly_dark"


# This graph provides a reference for the distribution of accidents across different days of the month.

# ### V. Accidents based on time of the day

# In[28]:


sns.set(style="whitegrid")                                 #creating bar graph using seaborn
plt.figure(figsize=(20,8))
Hourplot = sns.countplot(x='Hour',data=df)
Hourplot.set(xlabel='Hour', ylabel='Count')
for p in Hourplot.patches:
    height = p.get_height()
    Hourplot.text(p.get_x()+p.get_width()/2.,
      height + 3,
      '{:1.2f}'.format((len(df)/1000))+'k',
      ha="center")
plt.show()


# As evident from the data, the majority of accidents tend to coincide with peak hours during the day.

# ### Heatmap with the concentration of accidents by month over the years

# In[29]:


#plt.style.use("dark_background")
df['Ones']=1                                #creating heat map using seaborn
table = pd.pivot_table(df, values='Ones', index=['Month'],columns=['Year'], aggfunc=np.sum)
plt.figure(figsize=(15,7))
yticks = np.array(['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC'])
sns.set(rc={"axes.labelsize":20},font_scale=1)
sns.heatmap(table, yticklabels=yticks,linewidths=.1,annot=False,cmap='magma')
plt.show()


# The heatmap's color intensity darkens as you progress through the years and months, indicating a decreasing trend in accident rates over time within each month.

# ## Accidents in different Weather Conditions

# In[30]:


df_conditions = df[['Light_Conditions','Weather_Conditions','Road_Surface_Conditions',]]


# In[31]:


df_weather_accident = df.groupby(['Accident_Severity', 'Weather_Conditions'], as_index=False).size()
df_weather_severity = pd.DataFrame(df_weather_accident)
df_weather_severity.columns = ['Accident Severity', 'Weather Conditions', 'Count']
fig = px.bar(df_weather_severity, x='Weather Conditions', y='Count', hover_data=['Accident Severity'], color='Accident Severity', labels={'Count':'Total Accidents'}, height=600, width=1000, text_auto=True)
fig.show()
#template="plotly_dark"


# Here you can see the accidents in different weather conditions also it shows the type of accident severity. Majority of the accidents are occured in Fine weather Conditions.

# ## Accidents in different Light Conditions

# In[32]:


sns.set(style="darkgrid")                           #creating bar graph using seaborn
plt.figure(figsize=(20,5))
lightplot = sns.countplot(x='Light_Conditions',data=df_conditions)
lightplot.set(xlabel='Light conditions', ylabel='Count',xticklabels=['Daylight','Darkness Light-Lit','Darkness unknown light','Darkness Light-Unlit Light Conditions','Darkness-No light'])
for p in lightplot.patches:
    height = p.get_height()
    lightplot.text(p.get_x()+p.get_width()/2., height + 3, '{:1.2f}'.format((height/len(df))*100)+'%', ha="center")
plt.show()


# The highest frequency of accidents takes place during daylight conditions which means.

# ## Accident occured by Road Surface Conditions

# In[33]:


sns.set(style="darkgrid")                           #creating bar graph using seaborn
plt.figure(figsize=(15,8))
roadplot = sns.countplot(x='Road_Surface_Conditions',data=df_conditions)
roadplot.set(xlabel='Road Surface conditions', ylabel='Count', xticklabels=['Wet','Dry','Frost','Snow','Flood','Normal'])
for p in roadplot.patches:
    height = p.get_height()
    roadplot.text(p.get_x()+p.get_width()/2.,
      height + 3,
      '{:1.2f}'.format((height/len(df))*100)+'%',
      ha="center")
plt.show()


# This graph provides a clear indication that various road surface conditions do not appear to be a significant contributing factor to accidents, as the majority of accidents occur on dry road surfaces.

# ## Accident in Urban or Rural Area

# In[34]:


# Create a pie chart using Matplotlib
area_type = df['area_type'].value_counts()
df_area = pd.DataFrame(area_type)
df_area = df_area.reset_index()
df_area.columns = ['Area Type', 'Total']
#plt.style.use("dark_background")
plt.figure(figsize=(6, 6))
explode = [0, 0.1]
colors = ['#003f5c','#bc5090']
plt.pie(df_area['Total'], labels=df_area['Area Type'], autopct='%1.1f%%', startangle=140, colors=colors, explode = explode)
plt.title('Accident on Different area')
plt.axis('equal')
sns.set(style="darkgrid")
sns.despine()
sns.set_palette('Set3')
plt.legend(df_area['Area Type'], title="Area Type", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
plt.show()


# Two-thirds of all accidents transpire in urban areas, while the remaining one-third transpire in rural areas.

# ## Did Police Officer Attend Scene of Accident?

# In[35]:


# Create a pie chart using Matplotlib
attend = df['Did_Police_Officer_Attend_Scene_of_Accident'].value_counts()
df_attend = pd.DataFrame(attend)
df_attend = df_attend.reset_index()
df_attend.columns = ['Police', 'Total']

#plt.style.use("dark_background")
fig1, ax1 = plt.subplots()
colors = ['#004c6d','#6996b3']
ax1.pie(df_attend['Total'], labels=df_attend['Police'], colors = colors, autopct='%1.1f%%', startangle=90)
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
ax1.axis('equal')
plt.tight_layout()
plt.title('Did Police Officer Attend Scene of Accident?')
plt.show()


# Over a span of ten years, approximately 80% of accidents underwent police investigation.

# ## Accidents on different road types.

# In[36]:


# Create a pie chart using Matplotlib
road_types = df['Road_Type'].value_counts()
df_road = pd.DataFrame(road_types)
df_road = df_road.reset_index()
df_road.columns = ['Road Type', 'Total']

fig = px.bar(df_road, x='Total',y='Road Type',orientation='h')
fig.show()


# The majority of accidents occurred on single carriageway roads.

# ## Accidents on different speed limits.

# In[37]:


df_speed = df.groupby(['Speed_limit'], as_index=False).size()
df_speeds = pd.DataFrame(df_speed)
df_speeds.columns = ['Speed limit', 'Count']
#df_speeds
fig = px.line(df_speeds, x='Speed limit', y='Count', markers=True)
fig.show()


# Approximately 1 million, of accidents occurred when the speed limit was set at 30. This suggests that adherence to or violations of this specific speed limit may play a crucial role in the occurrence of accidents.

# # Accidents on different Junction Control.

# In[38]:


sns.set(style="darkgrid")                           #creating bar graph using seaborn
plt.figure(figsize=(15,5))
areaplot = sns.countplot(x='Junction_Control',data=df)
areaplot.set(xlabel='Junction Control Type', ylabel='Count')
for p in areaplot.patches:
    height = p.get_height()
    areaplot.text(p.get_x()+p.get_width()/2.,
      height + 3,
      '{:1.2f}'.format((height/len(df))*100)+'%',
      ha="center")
plt.show()


# The data reveals that half of the accidents occurred at "give way" or "uncontrolled" junction control types, with "No junction control" contributing to 40% of these cases, and "traffic signal" accounting for 10% of the accidents.

# # Accidents happened between how many vehicles?

# In[39]:


acc_vehicle = df.groupby(['Number_of_Vehicles'], as_index=False).size()
df_acc_vehicle = pd.DataFrame(acc_vehicle)
df_acc_vehicle.columns = ['Number of Vehicles', 'Count']
fig = px.line(df_acc_vehicle, x='Number of Vehicles', y='Count', markers=True)
fig.show()


# Most of the accidents are occured between 2 vehicles.

# ## Accidents placed in UK

# In[40]:


cvs = ds.Canvas(plot_width=1000, plot_height=1000)
aggs = cvs.points(df, x='Longitude', y='Latitude')
coords_lat, coords_lon = aggs.coords['Longitude'].values, aggs.coords['Latitude'].values


# In[41]:


coordinates = [[coords_lon[0], coords_lat[0]],
               [coords_lon[-1], coords_lat[0]],
               [coords_lon[-1], coords_lat[-1]],
               [coords_lon[0], coords_lat[-1]]]
img = tf.shade(aggs, cmap=fire, how='eq_hist', alpha=255)[::-1].to_pil()


# In[42]:


dfs = np.array_split(df, 4)
for index, df in enumerate(dfs):
    globals()['df%s' % index] = pd.DataFrame(df)


# In[43]:


color_continuous = [
    (0.0, 'blue'), (0.005, 'lightgreen'), (0.1, 'gray'), (0.3, 'yellow'), (0.4, 'red'), (0.5, 'darkgreen'),
    (0.6, "green"), (0.7, "pink"), (0.8, "magenta"),
    (0.9, "silver"), (1, "orange")
]
fig = px.scatter_mapbox(df3[:1], lon = df3['Longitude'], lat = df3['Latitude'], zoom=4, color=df3['Number_of_Vehicles'], width = 1000, height = 900, title = "Accidnets in UK", color_continuous_scale = color_continuous)
fig.update_layout(mapbox_style = 'carto-darkmatter')
fig.update_layout(mapbox_layers=[
                      {
                    "sourcetype": "image",
                    "source": img,
                    "coordinates": coordinates
                      }
                  ])
fig.update_layout(margin = {'r':0, 't':50, 'l':0, 'b':10})
fig.show()


# This figure illustrates the geographic distribution of accidents in the United Kingdom, with the number of cars involved indicated by color.

# # Overview of EDA

# ### (1) The overview of Exploratory Data Analysis says that the amount of accidents are drcreasing over the years.
# 
# ### (2) Most of the accidents occured in Peak hours of the day.
# 
# ### (3) Most of the accidents are happened in urban areas. 
# 
# ### (4) Most of the accidents are done on single carriageway roads.
# 
# ### (5) Most accidents occur during dry weather, in daylight conditions, and when the weather is fine. These may not be weather-related accidents; instead, they may be caused by inattentive driving, speeding, problems with road design, or other human and infrastructure causes.
