#!/usr/bin/env python
# coding: utf-8

# ![image.png](attachment:a6dbdc8d-2f36-4dff-b639-08ddf338b2c6.png)

# In[1]:


from Game import *
from Game.minimax import *


# In[5]:


def initial_state():
    state=Board(4,4)

    #state[0]=state[2]=state[13]=state[15]=1

    for i in [0,2,13,15]:
        state[i]=1
        
    for i in [1,3,12,14]:
        state[i]=2

    return state

def show_state(state):
    print(state)

def valid_moves(state,player):

    moves=[]

    # single move is a start,end pair
    
    for i in range(16):
        # down
        if i not in [12,13,14,15] and state[i]==player and state[i+4]==0:
            moves.append( [i,i+4] )
        # up
        if i not in [0,1,2,3] and state[i]==player and state[i-4]==0:
            moves.append( [i,i-4] )
        # right
        if i not in [3,7,1,15] and state[i]==player and state[i+1]==0:
            moves.append( [i,i+1] )
        # left
        if i not in [0,4,8,12] and state[i]==player and state[i-1]==0:
            moves.append( [i,i-1] )


    return moves


def update_state(state,player,move):

    start,end=move

    new_state=state
    new_state[start]=0
    new_state[end]=player

    return new_state



def win_status(state,player):
    #  0  1  2  3 
    #  4  5  6  7 
    #  8  9 10 11 
    # 12 13 14 15 

    if player==1:
        other_player=2
    else:
        other_player=1

    # horizontal
    for i in [0,1,4,5,8,9,12,13]:
        if state[i]==state[i+1]==state[i+2]==player:
            return 'win'
    # vertical
    for i in [0,1,2,3,4,5,6,7]:
        if state[i]==state[i+4]==state[i+8]==player:
            return 'win'

    # diagonal-right
    for i in [0,1,4,5]:
        if state[i]==state[i+5]==state[i+10]==player:
            return 'win'
            
    # diagonal-left
    for i in [2,3,6,7]:
        if state[i]==state[i+3]==state[i+6]==player:
            return 'win'


    if not valid_moves(state,other_player):
        return 'stalemate'
    


# In[6]:


def random_move(state,player):    
    moves=valid_moves(state,player)
    return random.choice(moves)

random_agent=Agent(random_move)

def human_move(state,player):
    print("Player ", player)
    state.show_locations()
    print("Your valid moves are: ",valid_moves(state,player))
    valid_move=False
    while not valid_move:
        move=eval(input('What is your move? (e.g. [2,6]'))

        if move in valid_moves(state,player):
            valid_move=True
        else:
            print("Illegal move.")

    return move
human_agent=Agent(human_move)


# In[8]:


state=initial_state()
state


# In[15]:


start,end=random_move(state,2)
start,end


# In[16]:


state.rc_from_index(start)


# In[4]:


def minimax_move(state,player):

    values,moves=minimax_values(state,player,maxdepth=5)
    return top_choice(moves,values)


minimax_agent=Agent(minimax_move)


# In[16]:


g=Game(number_of_games=1)
g.run(minimax_agent,random_agent)
g.report()  


# In[ ]:




