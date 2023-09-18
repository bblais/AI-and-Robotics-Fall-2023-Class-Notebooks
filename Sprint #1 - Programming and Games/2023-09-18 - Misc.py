#!/usr/bin/env python
# coding: utf-8

# In[2]:


from Game import *


# ## Debug Dodgem

# In[3]:


state=Board(3,3)
state[1]=state[3]=1


# In[4]:


state


# In[5]:


state.show_locations()


# In[25]:


def valid_moves(state,player):

    moves=[]

    if player==1:
        for start in [0,1,3,4,6,7]:
            if state[start]==1 and state[start+1]==0:
                moves.append( [start,start+1] )

        

    elif player==2:
        pass # fill this in


    return moves


# In[26]:


state=Board(3,3)
state[1]=state[3]=1
state


# In[27]:


valid_moves(state,1)


# ## Debug Goblet

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


# In[ ]:





# ## Debug 3d ttt

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


# ## debug connect-3 and connect 4

# In[21]:


state=Board(4,5)
for i in range(20):
    state[i]=random.choice([0,1,2])
state


# In[22]:


state.show_locations()


# In[ ]:


for loc in [0,1,2,3,4,5,6,7,8,9]:
    if state[loc]==player and state[loc+5]==player and state[loc+10]==player:
        return 'win'


# ## debug breakthrough

# In[37]:


state=Board(5,5)
for i in range(25):
    state[i]=random.choice([0,1,2])
player=1
if player==1:
    other_player=2
else:
    other_player=1
    
state


# In[42]:


state[15]=1
state[19]=2


# In[43]:


state


# In[31]:


state.show_locations()


# In[49]:


moves=[]

for location in range(20):
    if state[location]==player and state[location+5]==0:
        moves.append([location,location+5])

    if location not in [0,5,10,15,20] and state[location]==player and state[location+4]==other_player:
        moves.append([location,location+5])

    # if state[location]==player and state[location+4]==other_player:
    #     moves.append([location,location+4])


# In[50]:


moves


# In[ ]:




