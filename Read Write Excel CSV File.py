#!/usr/bin/env python
# coding: utf-8

# ## Loading CSV File

# In[4]:


import pandas as pd
df = pd.read_csv('stock_data.csv', header=1)  # set header the first row
#df = pd.read_csv('stock_data.csv', skiprows=1)  # skip the first row, same effect
df


# ## Adding custom header

# In[6]:


df = pd.read_csv('stock_data.csv', header=None, names=['ticker','eps','revenue','price','people'])  # load csv, inform that there is no header, add custom header
df


# ## Limit Number of Rows

# In[7]:


df = pd.read_csv('stock_data.csv', nrows=3)  # load only 3 rows
df


# ## Ignore N/A Cells / Cleaning Data

# In[9]:


df = pd.read_csv('stock_data.csv', na_values=['not available', 'n.a.'])  # specify N/A cell values, will replace them with NaN
df


# ## Cleaning Data with Dict

# In[10]:


df = pd.read_csv('stock_data.csv', na_values={'eps': ['not available', 'n.a.'],
                                             'revenue': ['not available', 'n.a.', -1],
                                              'people': ['not available', 'n.a.']
                                             })  # use a dictionary to specify per column replacements, replace negative revenue with NaN
df


# ## Write to CSV

# In[11]:


df.to_csv('new.csv', index=False)  # will add index column unless specified not to
# can also specify columns: columns=['col1','col2']
# can also skip header: header=False


# ## Load an Excel

# In[20]:


def convert_people_cell(cell):
    # create a function that converts an n.a. cell to a name
    if cell == "n.a.":
        return 'sam walton'
    return cell

def convert_eps_cell(cell):
    if cell == "not available":
        return None
    return cell

df = pd.read_excel("stock_data.xlsx", "Sheet1",
                  converters={
                      'people': convert_people_cell,
                      'eps': convert_eps_cell
                  }) 

                
df


# ## Save an Excel

# In[22]:


df.to_excel('new.xlsx', sheet_name="stocks", startrow=1, startcol=2, index=False)


# ## Combining Two DataFrames as Two Different Sheets

# In[29]:


df = pd.read_csv('stock_data.csv')
df1 = df[0:2]
df1


# In[31]:


df2 = df[2:]
df2


# In[32]:


with pd.ExcelWriter('stocks_combined.xlsx') as writer:
    df1.to_excel(writer, sheet_name="Stocks1")
    df2.to_excel(writer, sheet_name="Stocks2")

