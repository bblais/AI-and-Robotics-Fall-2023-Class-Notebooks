#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *
from Game.minimax import *


# ## TTT

# In[2]:


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


def skittles_move(state,player,info):
    S=info.S
    last_state=info.last_state
    last_action=info.last_action

    # make/adjust the table

    if state not in S:
        # add a row to the table for each move
        S[state]=Table()
        moves=valid_moves(state,player)
        for action in moves:
            S[state][action]=3  # number of skittles/beads for each move
    
    move=weighted_choice(S[state])

    if move is None:  # there are no skittles in this row
        if last_state:
            S[last_state][last_action]=S[last_state][last_action]-1
            if S[last_state][last_action]<0:
                S[last_state][last_action]=0

        move=random_move(state,player)

    
    return move


# In[5]:


def skittles_after(status,player,info):
    S=info.S
    last_state=info.last_state
    last_action=info.last_action

    if status=='lose':
        if last_state:
            S[last_state][last_action]=S[last_state][last_action]-1
            if S[last_state][last_action]<0:
                S[last_state][last_action]=0
                
    # does this double-count the learning if you lose on your own turn        
    


# In[6]:


skittles_agent=Agent(skittles_move)
skittles_agent.S=Table()
skittles_agent.post=skittles_after


# In[17]:


def minimax_move(state,player):
    values,moves=minimax_values(state,player,display=False)
    return top_choice(moves,values)


minimax_agent=Agent(minimax_move)


# In[18]:


g=Game(number_of_games=1)
g.run(minimax_agent,skittles_agent)
g.report()   


# In[14]:


skittles_agent.S


# In[15]:


SaveTable(skittles_agent.S,"TTT Skittles.json")


# ## Run for more times

# In[20]:


g=Game(number_of_games=100)
g.display=False
g.run(minimax_agent,skittles_agent)
g.report()   


# In[21]:


g=Game(number_of_games=1000)
g.display=False
g.run(minimax_agent,skittles_agent)
g.report()   


# In[22]:


g=Game(number_of_games=10000)
g.display=False
g.run(minimax_agent,skittles_agent)
g.report()   


# In[23]:


SaveTable(skittles_agent.S,"TTT Skittles 10000.json")


# In[ ]:




