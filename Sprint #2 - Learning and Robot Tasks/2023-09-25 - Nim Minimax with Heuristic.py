#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *
from Game.minimax import *


# ## Nim

# In[2]:


def initial_state(): 
    """ returns  - The initial state of the game"""
    return 21

def valid_moves(state,player):
    """returns  - a list of the valid moves for the state and player"""

    if state==2:
        return [1,2]
    elif state==1:
        return [1]
    else:
        return [1,2,3]

def show_state(state):
    """prints or shows the current state"""
    print("There are",state,"sticks.")

def update_state(state,player,move):
    """returns  - the new state after the move for the player"""

    new_state=state-move

    return new_state


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
    


# ## Agents

# In[3]:


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

human_agent=Agent(human_move)


# In[4]:


state=120
values,moves=minimax_values(state,1)
values,moves


# In[ ]:





# In[5]:


state=120
values,moves=minimax_values(state,1,adjust_values_by_depth=True)
values,moves


# In[6]:


state=1000
values,moves=minimax_values(state,1,adjust_values_by_depth=True)
values,moves


# In[5]:


state=1000
values,moves=minimax_values(state,1,maxdepth=5)
values,moves


# In[4]:


def heuristic(state,player):

    is_even=  state%2==0

    if is_even:
        return -.5
    else:
        return 0.5

    return value  # between -1 and 1 represents the value of the state


# In[10]:


state=1000
values,moves=minimax_values(state,1,maxdepth=5)
values,moves


# In[ ]:





# In[5]:


state=20
values,moves=minimax_values(state,1)
values,moves


# In[6]:


def minimax_move(state,player):

    values,moves=minimax_values(state,player,adjust_values_by_depth=True)
    return top_choice(moves,values)


minimax_agent=Agent(minimax_move)


# In[7]:


g=Game(number_of_games=1)
g.run(minimax_agent,random_agent)
g.report()  


# In[ ]:




