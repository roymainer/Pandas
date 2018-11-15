#!/usr/bin/env python
# coding: utf-8

# ## Pivots
# Pivot is about changing the data **structure** to concentrate on specific values

# In[1]:


import pandas as pd

df = pd.read_csv('weather.csv')
df


# In[6]:


df.pivot(index='date', columns='city')  # now the pivot is the date and the columns are the cities


# In[2]:


df.pivot(index='date', columns='city', values='humidity')  # focus on humidity only


# In[7]:


df.pivot(index='humidity', columns='city', values='humidity')  # the pivot is the same as the selected values


# ## Pivot Table
# **Pivot table** is used to summarize and aggregate data inside dataframe

# In[8]:


df = pd.read_csv('weather2.csv')
df


# In[9]:


df.pivot_table(index='city', columns='date')  # the pivoted data looks much clearer


# In[12]:


df.pivot_table(index='city', columns='date', aggfunc='sum')  # same date values are summed


# ## Grouper
# This example shows how it's possible to group together close values
# In this example there are dates from early May and December

# In[14]:


df = pd.read_csv('weather3.csv')
df


# In[21]:


df['date']=pd.to_datetime(df['date'])  # convert date values from string to datetime type
df
df.pivot_table(index=pd.Grouper(freq='M',key='date'), columns='city')


# In[ ]:




