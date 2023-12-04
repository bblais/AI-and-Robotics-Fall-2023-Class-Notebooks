#!/usr/bin/env python
# coding: utf-8

# In[1]:


from breakthrough import *
from my_robot_functions import *
from classy import *
from pylab import imread,imsave


# ## Agent

# In[2]:


def get_move(state,player):
    if player==1:
        Q=LoadTable("Q1_breakthrough_table.json")
    else:
        Q=LoadTable("Q2_breakthrough_table.json")
        
    
    if state not in Q:
        return random_move(state,player)  # this is defined in my game functions import
    else:
        return top_choice(Q[state])


# ## Make Move

# In[3]:


def make_move(move):
    print("Making move ",move)
    
    board=Board(4,4)  # just to get the conversion functions for free
    
    start,end=move
    rs,cs=board.rc_from_index(start)  # convert to row, column
    re,ce=board.rc_from_index(end)
    
    distance_to_board=10
    length_column=4
    length_row=4

    type_of_move=ce-cs  # 0 for a forward move, +1 for a right-hand diagonal, -1 for left-hand diagonal
    distance_to_column=distance_to_board+length_column*cs
    distance_to_row=(4-rs)*length_row

    if type_of_move==0:  # forward

        move_forward(distance_to_column)
        turn_robot_left_90()
        move_forward(distance_to_row)
        arm_down()  # to push the piece
        move_forward( 1*length_row )
        arm_up()

        # go back
        move_backward(distance_to_row + 1*length_row)
        turn_robot_right_90()
        move_backward(distance_to_column)

    elif type_of_move==1:  # right-hand diagonal

        move_forward(distance_to_column)
        turn_robot_left_90()
        move_forward(distance_to_row)


        arm_down()  # to push the piece
        turn_robot_right_45()
        move_forward( 1*length_row )

        # go back
        move_backward(1*length_row)
        turn_robot_left_45()    
        move_backward(distance_to_row )
        turn_robot_right_90()
        move_backward(distance_to_column)

    elif type_of_move==-1:  # left-hand diagonal
        move_forward(distance_to_column)
        turn_robot_left_90()
        move_forward(distance_to_row)


        arm_down()  # to push the piece
        turn_robot_left_45()
        move_forward( 1*length_row )

        # go back
        move_backward(1*length_row)
        turn_robot_right_45()    
        move_backward(distance_to_row )
        turn_robot_right_90()
        move_backward(distance_to_column)

    else:
        raise ValueError("You can't get there from here.")


# ## Read State

# In[4]:


def read_state_from_file(filename):
    text=open(filename).read()
    text=text.strip()
    lines=[line.strip() for line in text.split('\n')]  # get rid of \n
    
    row=lines[0].split()
    R,C=len(lines),len(row)
    print(f"{R}x{C} board")
    state=Board(R,C)
    state.board=[int(val) for val in text.split()]  
    print(state)
    return state


# In[6]:


def read_state():
    from pylab import imread,imsave
    import os

    # train the classifier
    images=image.load_images('images/training squares/',delete_alpha=True)  #<=========
    data=image.images_to_vectors(images,verbose=True)  # train on all of them

    #classifier=kNearestNeighbor()
    classifier=NaiveBayes()
    classifier.fit(data.vectors,data.targets)


    # get the picture
    fname='current_board.jpg'              # for the robot
    take_picture(fname)
    im=imread(fname)

    # slice the picture into squares of the right size
    square_size=50 # choose a size that works for you
    import json
    with open('locations.json') as json_file:
        locations = json.load(json_file)

    count=0
    # for debugging
    if not os.path.exists('images/predicted'):
        os.mkdir('images/predicted')
    
    values=[]
    for r,c in locations:
        sr=r-square_size//2
        er=sr+square_size
        sc=c-square_size//2
        ec=sc+square_size   
        subimage=im[sr:er,sc:ec,:]
    
        # convert the square image to a data vector for the classifier
        vector=subimage.ravel()
        prediction=C.predict(atleast_2d(vector))[0]
    
        values.append(prediction)

        # for debugging
        imsave('images/predicted/square %d predicted as %s.jpg' % (count,data.target_names[prediction]),subimage)
    
        count+=1

    
    # reconstruct the state from the predictions
    state=Board(4,4)                                      #<========= change the size
    state.board=values

    print("Current state is:")
    print(state)

    x=input("""
    Hit return if this is correct, otherwise type a character 
    and the state will be read from current_board.txt.""")

    if x:
        print("Reading from file...")
        state=read_state_from_file('board.txt')

    print("Using")
    print(state)

    
    return state


# In[7]:


#state=read_state()


# ## Now the entire project

# In[8]:


state=read_state()     #  read the state from the world
move=get_move(state,1)   # from an agent
make_move(move)        # robot motion to move pieces, etc...


# In[ ]:



