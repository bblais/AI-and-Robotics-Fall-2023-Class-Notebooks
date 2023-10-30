#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *


# ## Functions needed for the final demo of the semester
# 
# - state=read_state()
# - move=get_move(state,player)
# - make_move(move)      
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 

# In[2]:


def Q_move(state,player,info):
    Q=info.Q
    last_state=info.last_state
    last_action=info.last_action
    learning=info.learning
    
    α=info.α  # learning rate
    ϵ=info.ϵ  # how often to take a random move
    γ=info.γ  # memory constant -- how quickly does the table update back in time (earlier in the game)
    
    # \alpha <hit tab>    α
    # \epsilon <hit tab>  ϵ
    # \gamma <hit tab>    γ
    
    if state not in Q:
        actions=valid_moves(state,player)
        Q[state]=Table()
        for action in actions:
            Q[state][action]=0  # initial value of table
    
    if learning:
        if random.random()<ϵ:  # take a random move occasionally to explore the environment
            move=random_move(state,player)
        else:
            move=top_choice(Q[state])
    else:
        move=top_choice(Q[state])
    
    if not last_action is None:  # not the first move
        reward=0
        
        # learn
        if learning:
            Q[last_state][last_action]+=α*(reward +
                        γ*max([Q[state][a] for a in Q[state]]) - Q[last_state][last_action])
    
    return move


# In[ ]:





# In[ ]:





# In[21]:


def get_move(state,player):
    if player==1:
        Q=LoadTable('TTT Q1 Table.json')
    else:
        Q=LoadTable('TTT Q2 Table.json')

    if state not in Q:
        print("State is not in the Q table.",state)
        move=random_move(state,player)
    else:
        move=top_choice(Q[state])
        
    return move


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[9]:


filename='board.txt'
text=open(filename).read()
text


# In[12]:


filename='board.txt'
text=open(filename).read()
text=text.strip()
lines=[line.strip() for line in text.split('\n')]  # get rid of \n

row=lines[0].split()
R,C=len(lines),len(row)
print(f"{R}x{C} board")
state=Board(R,C)
state.board=[int(val) for val in text.split()]
state


# In[16]:


def read_state_from_file(filename):
    text=open(filename).read()
    text=text.strip()
    lines=[line.strip() for line in text.split('\n')]  # get rid of \n
    
    row=lines[0].split()
    R,C=len(lines),len(row)
    print(f"{R}x{C} board")
    state=Board(R,C)
    state.board=[int(val) for val in text.split()]  
    print(state)
    return state


# In[20]:


read_state_from_file('board.txt')


# In[22]:


state=read_state_from_file('board.txt')


# In[23]:


get_move(state,1)


# In[ ]:




