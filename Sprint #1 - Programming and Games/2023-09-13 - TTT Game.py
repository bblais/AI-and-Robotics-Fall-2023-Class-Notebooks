#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *


# ## Tic Tac Toe

# - what is a state? Board of integers 0 = empty, 1 = X , 2 = O
# - what is a move? single number (location)
# - what is the initial state? Board of all zeros
# - what are the valid moves?  all of the locations where the state[location]==0
# - from a move and a state, what's the new state?  new state has either 1 or 2 (player) replace the value at the move location
# - what constitutes a win/lose/stalemate? 3 in a row of the player in the board == 'win'  'stalemate' no moves left

# In[2]:


state=Board(3,3)
state


# In[4]:


state=Board(4,6)
state


# In[5]:


state.show_locations()


# In[10]:


state[8]=2
state


# In[11]:


if state[8]==0:
    print("Not")
else:
    print("Bob")


# In[12]:


state[8]


# In[13]:


state[1,2]


# In[14]:


def initial_state(): 
    """ returns  - The initial state of the game"""
    state=Board(3,3)
    return state


# In[15]:


initial_state()


# In[16]:


def show_state(state):
    """prints or shows the current state"""
    print(state)


# In[17]:


def update_state(state,player,move):
    """returns  - the new state after the move for the player"""

    
    new_state=state
    new_state[move]=player

    return new_state


# In[18]:


state=initial_state()
state=update_state(state,1,3)
state


# In[19]:


state.show_locations()


# In[20]:


state=update_state(state,2,8)
state


# In[ ]:




