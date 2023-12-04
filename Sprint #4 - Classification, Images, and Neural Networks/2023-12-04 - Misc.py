#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *


# In[2]:


state=Board(4,4)


# In[3]:


state


# In[4]:


state.show_locations()


# In[7]:


def all_possible_moves(player):
    moves=[]

    if player==1:
        for i in range(4,16):
            moves.append([i,i-4])
            if not i in [4,8,12]:
                moves.append([i,i-5])
            if not i in [7,11,15]:
                moves.append([i,i-3])
    elif player==2:
        for i in range(12):
            moves.append([i,i+4])
            if not i in [0,4,8]:
                moves.append([i,i+5])
            if not i in [3,7,11]:
                moves.append([i,i+3])
    else:
        raise ValueError("You can't get there from here")


    return moves
    


# In[ ]:





# In[8]:


all_possible_moves()

