#!/usr/bin/env python
# coding: utf-8

# ## Creating DataFrame from CSV

# In[1]:


import pandas as pd
df = pd.read_csv('weather_data.csv')
df


# ## Creating DataFrame from Dictionary

# In[2]:


weather_data = {
    'day': ['1/1/2017','1/2/2017','1/3/2017','1/4/2017','1/5/2017','1/6/2017'],
    'temperature': [32,35,28,24,32,31],
    'windspeed': [6,7,2,7,4,2],
    'event': ['Rain', 'Sunny', 'Snow', 'Snow', 'Rain', 'Sunny']
}
df = pd.DataFrame(weather_data)
df


# In[4]:


print('Shape: ', df.shape)  # prints the table dimensions
row, columns = df.shape
print('Rows: ',row)
print('Columns: ', columns)


# In[5]:


df.head()  # print only the head of the table


# In[6]:


df.tail()  # print the tail of the table


# In[8]:


df[2:5]  # print rows 2 to 5


# In[10]:


df.columns  # print the table columns


# In[15]:


df.day # print the day column as if it was a property
# or
df['day']


# In[21]:


type(df['event'])  # print data type


# In[22]:


df[['event', 'day', 'temperature']]  # print specific columns


# In[23]:


df['temperature'].max()  # print the maximum temperature


# In[24]:


df.describe()  # print data statistics


# In[26]:


df[df.temperature >= 32]  # print all rows where temp >= 32


# In[27]:


df[df.temperature == df['temperature'].max()]  # print the row with the max temp


# In[30]:


df[['day','temperature']][df.temperature == df['temperature'].max()]  # print the row with the max temp, but only specific columns


# In[31]:


df.index  # prints the table index properties


# In[39]:


#df.set_index('day', inplace=True)  # change the index to day column, and modify df
df


# In[40]:


df.loc['1/2/2017']  # prints the specific day details, loc works on index


# In[41]:


df.reset_index(inplace=True)  # reset the table index


# In[42]:


df.set_index('event', inplace=True)  # change index to event column
df.loc['Snow']  # print all rows with Snow

