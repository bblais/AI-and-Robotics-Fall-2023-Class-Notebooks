#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *
from Game.minimax import *


# In[2]:


def initial_state():
    state=Board(4,4)

    #state[0]=state[2]=state[13]=state[15]=1

    for i in [0,2,13,15]:
        state[i]=1
        
    for i in [1,3,12,14]:
        state[i]=2

    return state


# In[3]:


state=initial_state()


# In[4]:


state


# In[5]:


state[2]


# In[6]:


state[5]


# In[7]:


count=0
for i in range(16):
    if state[i]==1:
        count=count+1

count


# In[8]:


def number_of_pieces(state,player):
    count=0
    for i in range(16):
        if state[i]==player:
            count=count+1

    return count


# In[9]:


number_of_pieces(state,1)


# In[10]:


state


# In[11]:


state[5]=2
state


# In[12]:


number_of_pieces(state,2)


# In[13]:


player=2


# In[ ]:


if player==2:
    value=(number_of_pieces(state,2)-number_of_pieces(state,1))/(number_of_pieces(state,2)+number_of_pieces(state,1))


# In[16]:


state


# In[14]:


player=2

if player==1:
    other_player=2
else:
    other_player=1

value=(number_of_pieces(state,player)-number_of_pieces(state,other_player))/(number_of_pieces(state,player)+number_of_pieces(state,other_player))


# In[15]:


value


# In[ ]:




