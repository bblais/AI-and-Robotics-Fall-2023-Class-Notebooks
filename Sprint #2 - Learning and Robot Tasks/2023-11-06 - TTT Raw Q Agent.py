#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *
from Game.minimax import *
from tqdm import tqdm


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


def Q_move(state,player,info):
    Q=info.Q

    if state not in Q:
        return random_move(state,player)

    move=top_choice(Q[state])
    return move


# In[7]:


def convert_json_to_shelve(json_fname,shelve_fname):
    shelve_fname=shelve_fname.replace(".db","")
    import shelve
    from tqdm import tqdm
    Q=LoadTable(json_fname)
    d = shelve.open(shelve_fname)
    for state in tqdm(Q):
        d[str(state)]=Q[state]
    d.close()    


# In[8]:


convert_json_to_shelve("TTT Q1 Table.json","TTT Q1 Table.db")


# In[18]:


def Q_move(state,player,info):
    Q_fname=info.Q.replace(".db","")  #omit the db -- it gets added automatically...yuck
    import shelve
    d = shelve.open(Q_fname) 
    try:
        actions=d[str(state.immutable())]
        move=top_choice(actions)
    except KeyError:
        move=random_move(state,player)

    
    d.close()
    
    return move


# In[20]:


Q1_agent=Agent(Q_move)
Q1_agent.Q="TTT Q1 Table.db"


# In[21]:


def minimax_move(state,player):
    values,moves=minimax_values(state,player,display=False)
    return top_choice(moves,values)


minimax_agent=Agent(minimax_move)


# In[22]:


agent1=Q1_agent
agent2=minimax_agent

g=Game(number_of_games=100)
g.display=False
result=g.run(agent1,agent2)
g.report()


# In[ ]:




