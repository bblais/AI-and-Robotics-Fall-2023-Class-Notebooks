#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *


# ## Nim
# 
# - what is a state?  single number (number of sticks)
# - what is a move? single number (how many sticks to pick up)
# - what is the initial state?  21
# - what are the valid moves?  move 1,2, or 3
# - from a move and a state, what's the new state?  new_state = state-move
# - what constitutes a win/lose/stalemate?   state==0 ==> lose,  state==1 ==> win
# 

# In[3]:


def initial_state(): 
    """ returns  - The initial state of the game"""
    return 21


# In[4]:


initial_state()


# In[5]:


def valid_moves(state,player):
    """returns  - a list of the valid moves for the state and player"""

    if state==2:
        return [1,2]
    elif state==1:
        return [1]
    else:
        return [1,2,3]


# In[6]:


valid_moves(17,1)


# In[7]:


valid_moves(2,1)


# In[8]:


valid_moves(1,1)


# In[9]:


def show_state(state):
    """prints or shows the current state"""
    print("There are",state,"sticks.")


# In[10]:


show_state(17)


# In[11]:


def update_state(state,player,move):
    """returns  - the new state after the move for the player"""

    new_state=state-move

    return new_state


# In[12]:


update_state(17,2,3)


# In[13]:


update_state(17,2,5)


# In[14]:


update_state(3,2,5)


# In[15]:


def win_status(state,player):
    """    returns  - 'win'  if the state is a winning state for the player, 
               'lose' if the state is a losing state for the player,
               'stalemate' for a stalemate
               None otherwise
    """

    if state==0:
        return 'lose'

    if state==1:
        return 'win'


    return None
    


# In[16]:


def random_move(state,player):    
    moves=valid_moves(state,player)
    return random.choice(moves)

random_agent=Agent(random_move)

def human_move(state,player):
    print("Player ", player)
    valid_move=False
    while not valid_move:
        move=int(input('What is your move? '))

        if move in valid_moves(state,player):
            valid_move=True
        else:
            print("Illegal move.")

    return move


# In[17]:


human_move(2,1)


# In[18]:


random_move(17,1)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[19]:


human_agent=Agent(human_move)
random_agent=Agent(random_move)


g=Game(number_of_games=1)
g.run(human_agent,random_agent)
g.report()   # state the percentage of wins, ties, etc...


# In[ ]:









