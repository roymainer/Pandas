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

# In[16]:


temp_df = pd.DataFrame({
    'city': ['mumbai', 'delhi', 'bangalore'],
    'temperature': [32, 45, 30]})
wind_speed_df = pd.DataFrame({
    'city': ['mumbai', 'delhi', 'bangalore'],
    'windspeed': [80, 60, 78]})
df = pd.concat([temp_df, wind_speed_df], axis=1)  # when axis=1, the new data is concatenated as new columns
df


# ## Combine DF and Series

# In[18]:


s = pd.Series(['Rain','Dry','Rain'], name='event')
s


# In[19]:


df = pd.concat([temp_df, s], axis=1)
df


# In[ ]:




