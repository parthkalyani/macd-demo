#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[3]:


data = pd.read_csv("data/AAPL.csv")


# In[6]:


data.tail()


# In[9]:


type(data)


# In[10]:


data.plot()


# In[11]:


data.dtypes


# In[18]:


data['Adj. Close'].plot()


# In[20]:





# In[ ]:




