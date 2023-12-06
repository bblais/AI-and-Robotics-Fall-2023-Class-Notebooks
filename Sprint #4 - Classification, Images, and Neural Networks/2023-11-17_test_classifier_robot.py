#!/usr/bin/env python
# coding: utf-8

# In order to use a classifier for read_state you need a training set of image squares for your game.  See 2023-11-17 - Make a training image set of squares.ipynb to do that.
# 
# In this example, my training set is in the folder "images/training squares".

# We'll start by debugging, and making sure it works, before making a complete read_state function

# In[1]:


from classy import *
from Game import Board


# In[2]:


images=image.load_images('images/training squares/')
images=remap_targets(images,new_target_names=['blank','player1','player2'])
summary(images)


# In[3]:


data=image.images_to_vectors(images)


# The following should really be 100% -- if it can't identify the data that it knows about, it will make errors on any test

# In[4]:


on_robot=False


# In[5]:


print("training...")
for C in [NaiveBayes(),kNearestNeighbor()]:
    print(str(C),": ",end="")
    C.fit(data.vectors,data.targets)
    print("On the full data set:",C.percent_correct(data.vectors,data.targets))

    sfname=str(C).replace("()","")+"_trained.json"
    C.save(sfname)
    print(f"Saved {sfname}")
    if not on_robot:
        sfname=str(C).replace("()","")+"_trained2.json"
        C.save(sfname)    
        print(f"Saved {sfname}")


# In[6]:


print("loading...")
for C in [NaiveBayes(),kNearestNeighbor()]:
    print(str(C),": ",end="")
    sfname=str(C).replace("()","")+"_trained.json"
    C.load(sfname)
    print(f"Loaded {sfname}")
    print("On the full data set:",C.percent_correct(data.vectors,data.targets))

for C in [NaiveBayes(),kNearestNeighbor()]:
    print(str(C),": ",end="")
    sfname=str(C).replace("()","")+"_trained2.json"
    C.load(sfname)
    print(f"Loaded {sfname}")
    print("On the full data set:",C.percent_correct(data.vectors,data.targets))


# In[7]:


from pylab import imread
from numpy import atleast_2d


# In[8]:


fname='images/board to reconstruct - was test9.jpg'
im=imread(fname)


# slice into squares

# In[9]:


square_size=50 # choose a size that works for you
import json
with open('locations.json') as json_file:
    locations = json.load(json_file)

count=0
im=imread(fname)

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

    count+=1


# In[10]:


state=Board(4,4)
state.board=values
state


# ## Now put it all together into read_state
#     

# In[11]:


def read_state_from_file(filename):
    from Game import Board
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


# In[12]:


def take_picture(fname):  # in jupyter have this, but don't put this on your robot!
    pass


# In[13]:


def read_state():
    from pylab import imread,imsave
    from numpy import atleast_2d
    import os
    from Game import Board
    from classy import image,NaiveBayes

    # train the classifier
    images=image.load_images('images/training squares/',delete_alpha=True)  #<=========
    data=image.images_to_vectors(images,verbose=True)  # train on all of them

    #classifier=kNearestNeighbor()
    classifier=NaiveBayes()
    classifier.load("naive_bayes_training_squares_trained.json")
    #classifier.fit(data.vectors,data.targets)


    # get the picture
    fname='current_board.jpg'              # for the robot
    fname='images/board to reconstruct - was test9.jpg' # for debugging in jupyter
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


# In[14]:


state=read_state()


# In[ ]:




