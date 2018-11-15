#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd

india_weather = pd.DataFrame({
    'city': ['mumbai', 'delhi', 'bangalore'],
    'temperature': [32, 45, 30],
    'humidity': [80, 60, 78]
})
india_weather

us_weather = pd.DataFrame({
    'city': ['new_york', 'chicago', 'orlando'],
    'temperature': [21, 14, 35],
    'humidity': [68, 65, 75]
})
us_weather


# ## Concatenate

# In[9]:


df = pd.concat([india_weather, us_weather], keys=['india','us'])  # ignore original index
df


# In[11]:


df.loc['india']


# ## Combine Two Similar DFs

# In[22]:


temp_df = pd.DataFrame({
    'city': ['mumbai', 'delhi', 'bangalore','city1'],
    'temperature': [32, 45, 30, 29]})
wind_speed_df = pd.DataFrame({
    'city': ['mumbai', 'delhi', 'bangalore', 'city2'],
    'windspeed': [80, 60, 78, 65]})
df = pd.concat([temp_df, wind_speed_df], axis=1)  # when axis=1, the new data is concatenated as new columns
df


# ## Combine DF and Series

# In[18]:


s = pd.Series(['Rain','Dry','Rain'], name='event')
s


# In[19]:


df = pd.concat([temp_df, s], axis=1)
df


# ## Merge
# Merge looks at the value of the city and merges instead of concatenates

# In[23]:


df = pd.merge(wind_speed_df, temp_df, on='city')  # intersects the data
df


# In[26]:


df = pd.merge(wind_speed_df, temp_df, on='city', how="outer")  # outer will make a union of the values
df


# In[ ]:


df = pd.merge(wind_speed_df, temp_df, on='city', how="right")  # right will take all data from "right" dataframe
df

