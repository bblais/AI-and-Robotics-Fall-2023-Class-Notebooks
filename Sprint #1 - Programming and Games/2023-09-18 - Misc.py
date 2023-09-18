#!/usr/bin/env python
# coding: utf-8

# In[2]:


from Game import *


# In[3]:


state=Board(3,3)
state[1]=state[3]=1


# In[4]:


state


# In[5]:


state.show_locations()


# In[ ]:


def valid_moves(state,player):

    moves=[]

    if player==1:
        for start in [0,1,3,4,6,7]:
            if state[start]==1 and state[start+1]==0:
                moves.append( [start,start+1] )

        

    elif player==2:
        pass # fill this in


    return moves


# In[ ]:





# In[ ]:





# In[8]:


state=Board(4,4)
for i in range(16):
    state[i]=random.choice([1,2])

state


# In[9]:


state.show_locations()


# In[10]:


s=0
player=1
for i in range(4):
   if state[i]==player:
       s+=1

if s==3:
    print("yay!")


# In[12]:


move=9
r,c=state.rc_from_index(move)
r,c


# In[13]:


for c in range(4):
   if state[r,c]==player:
       s+=1


# In[16]:


state=Board(3,3,3)
for i in range(27):
    state[i]=random.choice(range(9))
state


# In[15]:


state.show_locations()


# In[18]:


def win_status(state,player):
    subboard=Board(3,3)
    for i,location in enumerate([2,5,8,11,14,17,20,23,26]):
        subboard[i]=state[location]

    if ttt_win_status(subboard,player):
        return ttt_win_status(subboard,player)

    for i,location in enumerate([9,10,11,...]):
        subboard[i]=state[location]

    if ttt_win_status(subboard,player):
        return ttt_win_status(subboard,player)


    # check diagonals

    # check stalemate


# In[ ]:




