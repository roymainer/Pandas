#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

df = pd.read_csv("weather_data.csv", parse_dates=["day"])  # parse the day to date time format
type(df.day[0])
df.set_index('day', inplace=True)  # set the dates to be the index
df


# In[2]:


new_df = df.fillna(0)
new_df


# In[3]:


new_df = df.fillna({
    'temperature': 0, 
    'windspeed': 0,
    'event': 'no event'
})
new_df


# In[4]:


new_df = df.fillna(method="ffill")  # carry forward NA values from previous cell
new_df
# can also use bfill (back fill), will fill NA with next cell value


# In[5]:


new_df = df.fillna(method="bfill", axis="columns")  # will copy horizontal values instead of vertical
new_df


# In[6]:


new_df = df.interpolate()  # will auto fill the missing data (linear interpolation unless specified)
new_df   


# In[7]:


new_df = df.interpolate(method="time")
new_df


# In[16]:


new_df = df.dropna()  # will ignore any row containing na
new_df


# ## DataFrame Replace

# In[17]:


df = pd.read_csv('weather_data.csv')
new_df = df.replace({
    'temperature': [-999999, -8888888],
    'windspeed': -999999,
    'event': 0}, np.NaN)
new_df


# In[18]:


new_df = df.replace({
    -999999: np.NaN,
    'No Event': 'Sunny'
})
new_df


# In[22]:


new_df = df.replace({
    'temperature':'[A-Za-z]',
    'windspeed':'[A-Za-z]'
    },'', regex=True)
new_df


# In[23]:


df = pd.DataFrame({
    'score': ['exeptional', 'average', 'good', 'poor', 'average', 'exceptional'],
    'student': ['rob', 'maya', 'parhiv', 'tom', 'julian', 'erica']
})

df


# In[25]:


new_df = df.replace(['poor', 'average', 'good', 'exceptional'], [1,2,3,4])
new_df

