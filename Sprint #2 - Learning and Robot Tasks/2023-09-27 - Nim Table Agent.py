#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *
from Game.minimax import *


# ## Nim

# In[18]:


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

# In[19]:


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


# In[20]:


def minimax_move(state,player):

    values,moves=minimax_values(state,player,adjust_values_by_depth=True)
    return top_choice(moves,values)


minimax_agent=Agent(minimax_move)


# In[21]:


def table_move(state,player):

    T=Table()  # start with an empty
    T[6]=Table()
    # T[state][action]
    T[6][3]=-1
    T[6][2]=-1
    T[6][1]=+1
    
    T[5]=Table()
    T[5][3]=-1
    T[5][2]=-1
    T[5][1]=-1    

    move=top_choice(T[state])
    return move


table_agent=Agent(table_move)


# In[22]:


def table_move(state,player):

    T=Table()
    count=1
    for S in range(1,22):
        T[S]=Table()
        for action in [1,2,3]:
            if S==1 and action>1: # not a valid move
                continue
            if S==2 and action>2: # not a valid move
                continue
            
            T[S][action]=-1
    
            if count==1:
                T[S][action]=-1
            elif count==2 and action==1:
                T[S][action]=+1
            elif count==3 and action==2:
                T[S][action]=+1
            elif count==4 and action==3:
                T[S][action]=+1
            else:
                pass
            
        count=count+1
    
        if count>4:
            count=1

    move=top_choice(T[state])
    return move


table_agent=Agent(table_move)


# make the table here -- attach it to the agent



# In[26]:


def table_move(state,player,info):
    T=info.T
    move=top_choice(T[state])
    return move


table_agent=Agent(table_move)


# make the table here -- attach it to the agent
T=Table()
count=1
for S in range(1,22):
    T[S]=Table()
    for action in [1,2,3]:
        if S==1 and action>1: # not a valid move
            continue
        if S==2 and action>2: # not a valid move
            continue
        
        T[S][action]=-1

        if count==1:
            T[S][action]=-1
        elif count==2 and action==1:
            T[S][action]=+1
        elif count==3 and action==2:
            T[S][action]=+1
        elif count==4 and action==3:
            T[S][action]=+1
        else:
            pass
        
    count=count+1

    if count>4:
        count=1

table_agent.T=T


# In[23]:


state=6


# In[24]:


(state-1)%4


# In[10]:


def perfect_move(state,player):
    move=(state-1)%4

    if move==0:  # bad state
        move=1

    return move

perfect_agent=Agent(perfect_move)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[23]:


T=Table()


# In[31]:


T=Table()
count=1
for state in range(1,22):
    T[state]=Table()
    for action in [1,2,3]:
        if state==1 and action>1: # not a valid move
            continue
        if state==2 and action>2: # not a valid move
            continue
        

        
        T[state][action]=-1

        if count==1:
            T[state][action]=-1
        elif count==2 and action==1:
            T[state][action]=+1
        elif count==3 and action==2:
            T[state][action]=+1
        elif count==4 and action==3:
            T[state][action]=+1
        else:
            pass
        
        print(state,action,count)
        
    count=count+1

    if count>4:
        count=1


# In[32]:


T


# In[37]:


top_choice(T[6])


# In[12]:


T


# In[16]:


T[6]=Table()
# T[state][action]
T[6][3]=-1
T[6][2]=-1
T[6][1]=+1

T[5]=Table()
T[5][3]=-1
T[5][2]=-1
T[5][1]=-1


# In[17]:


T


# In[ ]:





# In[ ]:





# In[27]:


g=Game(number_of_games=1)
g.run(perfect_agent,table_agent)
g.report()  


# In[28]:


table_agent.T


# In[30]:


SaveTable(table_agent.T,'nim_table.json')


# In[ ]:




