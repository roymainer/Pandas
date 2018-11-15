#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_csv('weather_by_cities.csv')
df


# ## Grouping
# This will seperate the data into groups depending on given key
# In this example we will:
# 1. Divid the data into cities
# 2. Run analytics on the results and combine them into the same DataFrame

# In[6]:


g = df.groupby('city')  # group the data by city key
g


# In[4]:


for city, city_df in g:
    print(city)
    print(city_df)


# In[5]:


g.get_group('mumbai')  # will return a DataFrame


# In[7]:


g.max()  # get the maximum temperature in each of the cities


# In[9]:


g.mean()


# In[10]:


g.describe() # get all results at once


# In[14]:


import matplotlib
get_ipython().run_line_magic('matplotlib', 'inline')
g.plot()


# In[ ]:





# In[ ]:




