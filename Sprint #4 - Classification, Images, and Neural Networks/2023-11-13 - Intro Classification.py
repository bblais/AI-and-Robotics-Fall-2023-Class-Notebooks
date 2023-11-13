#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *


# In[2]:


from classy import *


# In[3]:


data=load_excel('data/iris.xls')


# In[4]:


plot2D(data)


# In[5]:


subset=extract_features(data,[0,2])


# In[6]:


plot2D(subset)


# In[ ]:




