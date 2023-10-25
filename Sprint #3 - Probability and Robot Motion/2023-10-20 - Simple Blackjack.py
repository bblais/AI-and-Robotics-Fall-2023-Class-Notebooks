#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *


# ## Simple Blackjack
# 
# - shuffle one deck
# - each player is dealt 2 cards - one is face up one face down
# - 2 players, both equivalent
# - move "hit" and "stand"
# - if "hit"
#     - dealt another card face up - bust - hand score > 21(end of game)
#     - other player's turn
# - if "stand"
#     - end of your turn
#  
# - end when both players stand
# - whoever has the highest hand score wins  (ties as well)
# - hand score calculated
# 

# In[2]:


def valid_moves(state,player):
    return ["hit","stand"]


# In[3]:


def initial_state():

    # State
    # deck
    # hand player 1
    # hand player 2
    # player 1 standing
    # player 2 standing
    # last card player 1
    # last card player 2

    deck=makedeck(1)
    hand1=deck.deal(2)
    hand2=deck.deal(2) 
    standing1=False
    standing2=False    
    last_card1=None
    last_card2=None

    state=deck,hand1,hand2,standing1,standing2

    return state


# In[4]:


def score(hand):

    total=0
    has_ace=False
    for card in hand:
        if card.rank==1:
            has_ace=True
            
        if card.rank>10:
            total=total+10
        else:
            total=total+card.rank

    if has_ace:
        if total+10<=21:
            total=total+10
    
    return total
    


# In[5]:


score([Card(1,'C'),Card(1,'C'),Card(8,'C'),Card(2,'C')])


# In[6]:


deck,hand1,hand2,standing1,standing2=initial_state()
print(hand1,score(hand1))
print(hand2,score(hand2))


# In[7]:


def win_status(state,player):
    deck,hand1,hand2,standing1,standing2=state

    score1=score(hand1)
    score2=score(hand2)
    visible_score1=score(hand1[1:])
    visible_score2=score(hand2[1:])

    if standing1 and standing2:
        if player==1:
            if score1>score2:
                return 'win'
            elif score1==score2:
                return 'stalemate'
            else:
                return 'lose'

        elif player==2:
            if score1>score2:
                return 'lose'
            elif score1==score2:
                return 'stalemate'
            else:
                return 'win'
        else:
            raise ValueError("You can't get there from here.")

    if player==1 and visible_score1>21:
        return "lose"

    if player==2 and visible_score2>21:
        return "lose"


    


# In[8]:


def state_to_observation(state,player):
    
    deck,hand1,hand2,standing1,standing2=state

    if player==1:
        observation=hand1,hand2[1:],standing1,standing2
    else:
        observation=hand2,hand1[1:],standing2,standing1
        

    return observation  # what an agent actually sees


# In[9]:


def update_state(state,player,move):
    deck,hand1,hand2,standing1,standing2=state

    if move=='stand':
        if player==1:
            standing1=True

        if player==2:
            standing2=True
            
    elif move=='hit':
        card=deck.deal(1)[0]  # deal one card and take the [0th] element of the list
        if player==1:
            hand1+=[card]
        if player==2:
            hand2+=[card]
        
    else:
        raise ValueError("You can't get there from here.")

    new_state=deck,hand1,hand2,standing1,standing2
    return new_state


# In[10]:


def show_state(observation):
    my_hand,your_hand,me_standing,you_standing=observation
    print(f"My hand {my_hand}")
    if you_standing:
        print(f"Other hand {your_hand} showing and Standing")    
    else:
        print(f"Other hand {your_hand}.")    



# In[11]:


def repeat_move(state,player,move):
    deck,hand1,hand2,standing1,standing2=state

    if player==1 and standing2:
        return True

    if player==2 and standing1:
        return True

    return False


# what specifies a card
# 
# - rank 1-13
# - suit H , C, S, D
# 
# - jokers
# 

# In[12]:


card=Card(13,'C')


# In[13]:


card.rank


# In[14]:


card.suit


# In[15]:


print(makedeck(1))


# In[16]:


print(makedeck(2))


# In[17]:


deck=makedeck(1)
len(deck)


# In[18]:


hand=deck.deal(2)


# In[19]:


hand


# In[20]:


len(deck)


# In[21]:


def random_move(observation,player):    
    moves=valid_moves(observation,player)
    return random.choice(moves)

random_agent=Agent(random_move)


# In[23]:


g=Game(number_of_games=1)
g.run(random_agent,random_agent)
g.report()   


# In[ ]:




