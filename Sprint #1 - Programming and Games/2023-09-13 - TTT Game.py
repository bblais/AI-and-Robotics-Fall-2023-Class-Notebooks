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


# In[3]:


state=Board(4,6)
state


# In[4]:


state.show_locations()


# In[5]:


state[8]=2
state


# In[6]:


if state[8]==0:
    print("Not")
else:
    print("Bob")


# In[12]:


state[8]


# In[13]:


state[1,2]


# In[8]:


def initial_state(): 
    """ returns  - The initial state of the game"""
    state=Board(3,3)
    return state


# In[15]:


initial_state()


# In[7]:


def show_state(state):
    """prints or shows the current state"""
    state.show_locations()
    print(state)


# In[9]:


state=initial_state()
show_state(state)


# In[12]:


def update_state(state,player,move):
    """returns  - the new state after the move for the player"""

    
    new_state=state
    new_state[move]=player

    return new_state


# In[11]:


state=initial_state()
state=update_state(state,1,3)
state


# In[19]:


state.show_locations()


# In[20]:


state=update_state(state,2,8)
state


# In[17]:


def valid_moves(state,player):
    """returns  - a list of the valid moves for the state and player"""

    moves=[]


    for location in range(9):
        if state[location]==0:
            moves.append(location)


    return moves


# In[18]:


state=initial_state()
state[0]=1
state[1]=1
state[4]=2
state[5]=2
state[8]=1
state


# In[19]:


valid_moves(state,1)


# In[ ]:





# In[ ]:





# In[13]:


a=[ 4,5,'bob',4545,3432.2332]
a


# In[14]:


a[2]


# In[15]:


a.append('something')
a


# In[16]:


a=[]
for i in range(4):
    a.append(2*i)

a


# In[20]:


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



# In[21]:


state=initial_state()
for i in range(9):
    state[i]=1
show_state(state)
win_status(state,1)


# In[22]:


# bad test for stalemate
state=initial_state()
for i in range(9):
    state[i]=i
show_state(state)
win_status(state,1)


# In[23]:


state=initial_state()
for i in range(9):
    state[i]=i+10
show_state(state)
win_status(state,1)


# In[26]:


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


# In[25]:


human_agent=Agent(human_move)
random_agent=Agent(random_move)


g=Game(number_of_games=1)
g.run(human_agent,random_agent)
g.report()   # state the percentage of wins, ties, etc...


# In[ ]:




