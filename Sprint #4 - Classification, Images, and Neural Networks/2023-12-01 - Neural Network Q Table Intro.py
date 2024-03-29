#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *


# In[4]:


def initial_state():
    return Board(3,3)

def valid_moves(board,player):

    empty=[]
    for i in range(9):
        if board[i]==0:
            empty.append(i)

    return empty

def update_state(board,player,move):
    board[move]=player
    return board

def check_three_in_a_row(row):

    if row[0]==1 and row[1]==1 and row[2]==1:
        return 1
    elif row[0]==2 and row[1]==2 and row[2]==2:
        return 2
    else:
        return 0

def win_status(board,player):
    # in ttt, after a move, that player can either win or stalemate
    # they can't lose after their own move
    
    if check_three_in_a_row( [board[0],board[1],board[2] ])==player:
        return 'win'

    if check_three_in_a_row( [board[2],board[5],board[8] ])==player:
        return 'win'

    if check_three_in_a_row( [board[3],board[4],board[5] ])==player:
        return 'win'

    if check_three_in_a_row( [board[6],board[7],board[8] ])==player:
        return 'win'

    if check_three_in_a_row( [board[0],board[3],board[6] ])==player:
        return 'win'

    if check_three_in_a_row( [board[1],board[4],board[7] ])==player:
        return 'win'

    if check_three_in_a_row( [board[0],board[4],board[8] ])==player:
        return 'win'

    if check_three_in_a_row( [board[6],board[4],board[2] ])==player:
        return 'win'


    # stalemate
    tie=True
    for i in range(9):
        if board[i]==0:
            tie=False

    if tie:
        return 'stalemate'



    return None


# In[14]:


state=Board(3,3)
player=1
state[0]=1
state[3]=2
state[4]=1
state[8]=2
state


# In[15]:


Q=Table()


# In[16]:


if state not in Q:
    actions=valid_moves(state,player)
    Q[state]=Table()
    for action in actions:
        Q[state][action]=0  # initial value of table

Q


# In[22]:


Q[state]


# In[23]:


Q[initial_state()]


# In[17]:


from Game.numpynet_tables import NumpyNetTable


# In[18]:


def all_possible_moves():
    all_moves=[]
    for move in range(9):
        all_moves.append(move)
            
    return all_moves


# length 9 with +1, -1, 0
def state_to_X(state):  
    import numpy as np
    N2=len(state)
    arr=np.zeros((1,N2))  # number of samples, size
    for i in range(N2):
        if state[i]==0:
            arr[0,i]=0
        elif state[i]==1:
            arr[0,i]=1
        elif state[i]==2:
            arr[0,i]=-1
                     
    return arr


# In[19]:


state_to_X(state)


# In[20]:


initial_X=state_to_X(initial_state())
all_moves=all_possible_moves()


# In[21]:


print(state)
print(initial_X)

QNN=NumpyNetTable(state_to_X,all_possible_moves(),
                {
                    'input':initial_X.shape[1],               # number of inputs
                    'hidden':[(81,'relu'),],
                    'hidden':[(81,'relu'),],
                    'output':(len(all_moves),'linear'),  # number of moves
                    'cost':'mse',
                },
                        verbose=False)


# In[24]:


QNN[state]


# In[25]:


QNN[initial_state()]


# In[28]:


possible_moves=all_possible_moves()
target=[]
for i,move in enumerate(possible_moves):
    
    if move not in valid_moves(state,player):
        target.append(-1)
    else:
        target.append(1)
target


# In[29]:


QNN[state]=target


# In[30]:


QNN[state]


# In[ ]:




