#!/usr/bin/env python
# coding: utf-8

# In[4]:


get_ipython().run_line_magic('matplotlib', 'inline')
from mplturtle import *


# In[6]:


reset(figsize=(3,3))
forward(50)
right(90)
forward(50)


# In[8]:


reset(figsize=(3,3))
forward(50)
right(30)
forward(50)


# In[9]:


def house(length):
    pass


# In[ ]:


reset()
house(30)
forward(30)
house(30)


# In[ ]:


bob=30
reset()
house(bob)
forward(bob)
house(bob)


# In[ ]:





# In[12]:


reset(figsize=(3,3))
forward(60)
penup()
forward(60)
pendown()
right(90)
forward(60)


# ## Stairs 
# ![image.png](attachment:c0be9706-239f-4d49-aa0a-fe37b36b4310.png)

# In[21]:


reset(figsize=(3,3))
forward(50)
right(90)
forward(50)


# In[22]:


def step():
    forward(50)
    right(90)
    forward(50)  


# In[25]:


reset(figsize=(3,3))
step()
step()
step()


# In[26]:


def step():
    forward(50)
    right(90)
    forward(50)  
    left(90)


# In[27]:


reset(figsize=(3,3))
step()
step()
step()


# In[28]:


reset(figsize=(3,3))
for i in range(10):
    step()


# In[38]:


def step(length=50):
    forward(length)
    right(90)
    forward(length)  
    left(90)


# In[31]:


reset(figsize=(3,3))
for i in range(10):
    step(20)   # length=20

for i in range(10):
    step(60)


# In[33]:


reset(figsize=(3,3))
step(20)   # length=20


# In[37]:


reset(figsize=(3,3))
step(60)   # length=60


# In[ ]:




