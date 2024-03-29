#!/usr/bin/env python
# coding: utf-8

# In[3]:


from Game import *
from Game.minimax import *


# ## TTT

# In[4]:


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

# In[5]:


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


def table_move(state,player,info):
    T=info.T

    # make/adjust the table

    if state not in T:
        # add a row to the table for each move
        T[state]=Table()
        values,moves=minimax_values(state,player)

        for value,action in zip(values,moves):
            T[state][action]=value
    
    move=top_choice(T[state])
    return move


# In[9]:


table_agent=Agent(table_move)
table_agent.T=Table()


# In[10]:


values=[1,20,-3,4]
moves=['bob','sally','frank','jill']

for value,action in zip(values,moves):
    print("the value is:",value)
    print("the action is:",action)    


# In[11]:


def minimax_move(state,player):
    values,moves=minimax_values(state,player)
    return top_choice(moves,values)


minimax_agent=Agent(minimax_move)


# In[12]:


g=Game(number_of_games=1)
g.run(minimax_agent,table_agent)
g.report()   


# In[13]:


table_agent.T


# In[15]:


SaveTable(table_agent.T,"TTT Table.json")


# In[ ]:




