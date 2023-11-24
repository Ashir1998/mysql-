#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import pymysql
from sqlalchemy import create_engine


# In[2]:


#Load Data
df = pd.read_csv('./vgsales-2016.csv')
df.head()


# In[3]:


#Find how many records this data frame has
df.shape


# In[4]:


#How many elements are there?
df.size


# In[5]:


#What are the column names?
df.columns


# In[6]:


#What types of columns we have in this data frame?
df.dtypes


# In[7]:


df.info()


# In[ ]:




