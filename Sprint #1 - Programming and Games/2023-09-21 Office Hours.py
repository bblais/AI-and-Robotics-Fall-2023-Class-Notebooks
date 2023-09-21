#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *


# In[3]:


state=Board(4,4)
state


# In[4]:


state.show_locations()


# In[5]:


for i in range(4):
    state[i]=2
    state[i+12]=1
state


# In[6]:


moves=[]
if player==1:
    for location in range(4,16):
        if state[location]==1 and state[location-4]==0:
            moves.append(  [location,location-4]  )
    
    for location in [4,5,6,8,9,10,12,13,14 ]:
        if state[location]==1 and (state[location-3]==0 or state[location-3]==2):
            moves.append(  [location,location-3]  )

moves


# In[ ]:




