#!/usr/bin/env python
# coding: utf-8

# In[5]:


from Game import *
from Game.minimax import *


# ## TTT

# In[6]:


def initial_state(): 
    """ returns  - The initial state of the game"""
    state=Board(3,3)
    return state

def show_state(state):
    """prints or shows the current state"""
    state.show_locations()
    print(state)

def update_state(state,player,move):
    """returns  - the new state after the move for the player"""

    
    new_state=state
    new_state[move]=player

    return new_state

def valid_moves(state,player):
    """returns  - a list of the valid moves for the state and player"""

    moves=[]


    for location in range(9):
        if state[location]==0:
            moves.append(location)


    return moves

def win_status(state,player):
    """    returns  - 'win'  if the state is a winning state for the player, 
               'lose' if the state is a losing state for the player,
               'stalemate' for a stalemate
               None otherwise
    """

    # 0  1  2 
    # 3  4  5 
    # 6  7  8 

    if state[0]==state[1]==state[2]==player:
        return 'win'
    if state[3]==state[4]==state[5]==player:
        return 'win'
    if state[6]==state[7]==state[8]==player:
        return 'win'
    if state[0]==state[3]==state[6]==player:
        return 'win'
    if state[1]==state[4]==state[7]==player:
        return 'win'
    if state[2]==state[5]==state[8]==player:
        return 'win'
    if state[0]==state[4]==state[8]==player:
        return 'win'
    if state[6]==state[4]==state[2]==player:
        return 'win'

    
    if not valid_moves(state,player):
        return 'stalemate'



# ## Agents

# In[7]:


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


# In[8]:


state=initial_state()
show_state(state)
values,moves=minimax_values(state,1)
values,moves


# In[9]:


state=initial_state()
state[0]=1
state[1]=2
show_state(state)
values,moves=minimax_values(state,1)
values,moves


# In[13]:


def minimax_move(state,player):

    values,moves=minimax_values(state,player,maxdepth=5)
    return top_choice(moves,values)


minimax_agent=Agent(minimax_move)


# In[14]:


def heuristic(state,player):
    value=0  # fix this...
    return value  # between -1 and 1 represents the value of the state    


# In[15]:


g=Game(number_of_games=1)
g.run(minimax_agent,random_agent)
g.report()   


# In[ ]:





# In[16]:


g=Game(number_of_games=1)
g.display=False
g.run(minimax_agent,random_agent)
g.report()   


# In[20]:


g=Game(number_of_games=100)
g.display=False
g.run(random_agent,random_agent)
g.report()   


# In[ ]:




