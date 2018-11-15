#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
df = pd.read_csv(r'c:\users\rmainer\desktop\nyc_weather.csv')
df


# In[3]:


df['Temperature'].max()  # finds the maximum cell value in Tempertature column


# In[4]:


df['EST'][df['Events']=='Rain']  # prints all dates when it rained


# In[6]:


df.fillna(0, inplace=True)  # replace any Nan with 0
df['WindSpeedMPH'].mean()  # the mean wind speed

