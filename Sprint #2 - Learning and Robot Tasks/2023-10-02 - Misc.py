#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def adjusted_state(state):
    part1,part2,part3=state
    new_state=part1,part2
    return new_state


# In[ ]:


def skittles_move(state,player,info):
    S=info.S
    last_state=info.last_state
    last_action=info.last_action

    original_state=state
    state=adjusted_state(original_state)
    original_last_state=last_state
    last_state=adjusted_state(original_last_state)
    
    # make/adjust the table

    if state not in S:
        # add a row to the table for each move
        S[state]=Table()
        moves=valid_moves(original_state,player)
        for action in moves:
            S[state][action]=3  # number of skittles/beads for each move
    
    move=weighted_choice(S[state])

    if move is None:  # there are no skittles in this row
        if last_state:
            S[last_state][last_action]=S[last_state][last_action]-1
            if S[last_state][last_action]<0:
                S[last_state][last_action]=0

        move=random_move(original_state,player)

    
    return move

def skittles_after(status,player,info):
    S=info.S
    last_state=info.last_state
    last_action=info.last_action

    original_state=state
    state=adjusted_state(original_state)
    original_last_state=last_state
    last_state=adjusted_state(original_last_state)
    
    if status=='lose':
        if last_state:
            S[last_state][last_action]=S[last_state][last_action]-1
            if S[last_state][last_action]<0:
                S[last_state][last_action]=0
                
    # does this double-count the learning if you lose on your own turn        
    

