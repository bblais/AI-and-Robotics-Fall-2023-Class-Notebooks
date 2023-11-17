#!/usr/bin/env python
# coding: utf-8

# **Step 1:** You need a series of pictures of the board with pieces in various positions.  They don't have to be legitimate board states.  Here's an example set:

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *


# In[5]:


from glob import glob
import os


# In[10]:


fnames=glob('images/board images/*.jpg')
test_image='images/board images/test9.jpg'
fnames.remove(test_image)  # this will be the image I will reconstruct, so I don't want it in the training
fnames


# In[14]:


for i,fname in enumerate(fnames):
    im=imread(fname)
    subplot(3,4,i+1)
    imshow(im)

    root,part=os.path.split(fname)
    
    title(part)

subplot(3,4,12)
fname=test_image
im=imread(fname)
imshow(im)
root,part=os.path.split(fname)
title(part + "[TEST]")


# **Step 2:** Now you need the locations of the centers of the squares.  You can do something like 2023-11-13 - Arrays and Images.ipynb, or perhaps easier, run the 2023-11-13 - Get Board Center Square Locations.ipynb on one of the images, select the center squares, and hit the escape key.  It will save the centers to a json file which we load here.

# In[15]:


import json
with open('locations.json') as json_file:
    locations = json.load(json_file)
locations


# **Step 3:** Run through all the center locations for each file, extract a square, and save it as another image.  We'll be saving it to a folder I've already made called "images/training squares".

# In[18]:


square_size=50 # choose a size that works for you


count=0
for i,fname in enumerate(fnames):
    im=imread(fname)

    
    for r,c in locations:
        sr=r-square_size//2
        er=sr+square_size
        sc=c-square_size//2
        ec=sc+square_size   
        subimage=im[sr:er,sc:ec,:]
    
        square_fname='images/training squares/square%d.jpg' % count
        print(square_fname)
        imsave(square_fname,subimage)
        
        count+=1


# The folder will now look like: ![image.png](attachment:fec64cf6-83c4-4d66-a453-e77c2843a964.png)

# **Step 4:** By hand, in the file explorer, put the right images into the right folders.  There may be ways to automate this step, but since you only need to do this once, by hand will work fine.
# 
# The folder will look something like this:
# ![image.png](attachment:65995273-124e-4d85-b7b2-74026d673ab5.png)

# Now you have a training set!

# In[ ]:




