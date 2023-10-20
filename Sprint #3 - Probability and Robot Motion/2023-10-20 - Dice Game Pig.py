#!/usr/bin/env python
# coding: utf-8

# In[13]:


from Game import *


# ## Rules of Pig

# - Player choose a move: hold or roll
# 
# - if roll
#     - roll a single die (1-6)
#     - if value == 1:
#        - turn total = 0
#        - can't roll again 
#     - else:
#        - value is added turn total 
#        - can roll again = choose between hold and roll
# - if hold
#     - turn total is added to your total score
#     - next player
#  
# - game ends when 1 player reaches max score (100)
# 
# 
# 
# - What is a state? player 1 total score, player 2 total score,turn total, last dice roll
# - What is a move?

# In[24]:


def valid_moves(state,player):
    player1_score,player2_score,turn_total,last_die=state

    if turn_total==0:
        return ['roll']
    else:
        return ['hold','roll']


# In[25]:


def initial_state():
    state=[0,0,0,0]
    return state


# In[26]:


state=initial_state()
player1_score,player2_score,turn_total,last_die=state


# In[27]:


def show_state(state):
    player1_score,player2_score,turn_total,last_die=state
    print("Player 1's score is ",player1_score)
    print("Player 2's score is ",player2_score)
    print("Last die roll was ",last_die)
    print("Turn total is ",turn_total)



# In[28]:


show_state(state)


# In[29]:


def update_state(state,player,move):
    player1_score,player2_score,turn_total,last_die=state

    
    if move=='hold':
        if player==1:
            player1_score+=turn_total
        else:
            player2_score+=turn_total
            
        turn_total=0
        last_die=0

    elif move=='roll':

        dice=random.randint(1,6)  # generates a "random" number between 1 and 6
        last_die=dice
        
        if dice==1:
            turn_total=0
        else:
            turn_total+=dice

    
    else:
        raise ValueError("You can't get there from here.")   


    new_state=player1_score,player2_score,turn_total,last_die
    return new_state


# In[30]:


def win_status(state,player):
    player1_score,player2_score,turn_total,last_die=state

    max_score=21
    if player==1:
        if player1_score+turn_total>max_score:
            return "win"

    if player==2:
        if player2_score+turn_total>max_score:
            return "win"


# In[31]:


def repeat_move(state,player,move):
    player1_score,player2_score,turn_total,last_die=state

    # return True if you get another turn, otherwise False

    if turn_total>0:
        return True
    else:
        return False


# ## Agents

# In[32]:


def random_move(state,player):    
    moves=valid_moves(state,player)
    return random.choice(moves)

random_agent=Agent(random_move)


# In[34]:


def human_move(state,player):
    print("Player ",player)

    while True:
        s=input('hold or roll?')
    
        first_character=s[0]
        if first_character=='h':
            return "hold"
        if first_character=='r':
            return "roll"

human_agent=Agent(human_move)


# In[39]:


human_move([0,0,0,0],1)


# In[33]:


g=Game()

g.run(random_agent,random_agent)


# In[ ]:




