#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
from mplturtle import *


# ![image.png](attachment:42fe4ca4-0b02-4b6d-abe2-a59a5b566c55.png)

# In[2]:


def square(size):
    for i in range(4):
        forward(size)
        right(90)

def f(length,draw=True):
    if not draw:
        penup()

    forward(length)

    if not draw:
        pendown()


# In[3]:


reset(figsize=(5,5))

current_color='black'
next_color='red'


for j in range(5):
    for i in range(5):

        pencolor(current_color)
        square(50)
        f(70,draw=False)


        # swap the colors
        current_color,next_color=next_color,current_color
    
    
    left(180)
    f(50*5+20*5,draw=False)
    left(180)
    
    right(90)
    f(70,draw=False)
    left(90)
    


# In[4]:


reset(figsize=(5,5))

count=0
for j in range(5):
    for i in range(5):

        if count%2==0:  # even
            pencolor("black")
        else:
            pencolor("red")
            
        square(50)
        f(70,draw=False)

        count=count+1
    
    left(180)
    f(50*5+20*5,draw=False)
    left(180)
    
    right(90)
    f(70,draw=False)
    left(90)
    


# In[5]:


reset(figsize=(5,5))

step=2
for i in range(0,90+1,step):
    forward(50)
    backward(50)
    left(step)


# In[6]:


reset(figsize=(5,5))

step=2
for i in range(0,270+1,step):
    forward(50)
    backward(50)
    right(step)


# In[7]:


reset(figsize=(5,5))

step=2
pencolor('black')
for i in range(0,90,step):
    forward(50)
    backward(50)
    left(step)

pencolor('red')
for i in range(0,90,step):
    forward(50)
    backward(50)
    left(step)

pencolor('blue')
for i in range(0,90,step):
    forward(50)
    backward(50)
    left(step)

pencolor('green')
for i in range(0,90,step):
    forward(50)
    backward(50)
    left(step)


# In[8]:


reset(figsize=(5,5))

step=2

for color in ['black','red','blue','green']:
    pencolor(color)
    for i in range(0,90,step):
        forward(50)
        backward(50)
        left(step)


# In[9]:


reset(figsize=(5,5))

step=2
right(30)
for color in ['black','red','blue']:
    pencolor(color)
    for i in range(0,120,step):
        forward(50)
        backward(50)
        left(step)


# In[ ]:





# ![image.png](attachment:a675f6db-f99e-4ff6-a682-dddff499880f.png)

# In[11]:


reset(figsize=(5,5))
for i in range(5):
    forward(25)
    right(90)
    forward(25)
    left(90)


# In[12]:


reset(figsize=(5,5))

right(180)
for i in range(5):
    forward(25)
    left(90)
    forward(25)
    right(90)


# In[13]:


def square(size):
    # as if size=#
    for i in range(4):
        forward(size)
        right(90)

def hexagon(size):
    for i in range(6):
        forward(size)
        right(360/6)


# In[20]:


reset(figsize=(5,5))

size=80

penup()
backward(size//2)
left(90)
forward(size//2)
right(90)
pendown()

square(size)

penup()
forward(size//2)
right(90)
backward(size//2)
left(90)
pendown()




# In[24]:


def centered_square(size):
    
    penup()
    backward(size//2)
    left(90)
    forward(size//2)
    right(90)
    pendown()
    
    square(size)
    
    penup()
    forward(size//2)
    right(90)
    forward(size//2)
    left(90)
    pendown()
        


# In[25]:


reset(figsize=(5,5))
centered_square(50)
centered_square(80)


# In[26]:


reset(figsize=(5,5))

for size in range(10,110,10):
    centered_square(size)


# In[28]:


reset(figsize=(5,5))

size=50

penup()
right(90)
forward(size//2)
left(90)
pendown()

circle(size)

penup()
left(90)
forward(size//2)
right(90)
pendown()



# In[29]:


def centered_circle(size):
    penup()
    right(90)
    forward(size//2)
    left(90)
    pendown()
    
    circle(size)
    
    penup()
    left(90)
    forward(size//2)
    right(90)
    pendown()
        


# In[30]:


reset(figsize=(5,5))

for size in range(10,110,10):
    centered_circle(size)


# ![image.png](attachment:9c94b4db-2a3d-4dc0-abff-b6d6810ffc44.png)

# In[36]:


reset(figsize=(5,5))

pencolor("blue")
for i in range(80):
    penup()
    forward(200)
    pendown()
    hexagon(25)
    penup()
    backward(200)
    left(5)
    pendown()
    


# In[39]:


reset(figsize=(5,5))

for color,radius in zip(["blue","purple","cyan","yellow","brown"],[200,170,140,110,80]):

    pencolor(color)
    for i in range(40):
        penup()
        forward(radius)
        pendown()
        hexagon(25)
        penup()
        backward(radius)
        left(10)
        pendown()
        


# In[ ]:





# In[ ]:





# ![image.png](attachment:8139574a-79f0-4b72-bd55-823e8c9ad708.png)

# In[41]:


reset(figsize=(5,5))

size=10
for i in range(12):
    square(size)
    forward(size)

# next row
right(180)
forward(12*size)
right(180)
forward(size//2)
left(90)
forward(size)
right(90)

for i in range(11):
    square(size)
    forward(size)



# In[45]:


reset(figsize=(5,5))
size=10

for N in range(12,0,-1):
    for i in range(N):
        square(size)
        forward(size)

    if N>1:
        # next row
        right(180)
        forward(N*size)
        right(180)
        forward(size//2)
        left(90)
        forward(size)
        right(90)


# Write a *recipe* (on paper, or typed out) for the computer to solve the 100x100 Queen's problem

# In[ ]:


def check_capture(board):
    pass


# - for all possible value of row1, row2, row3, ....   (100 x 100 x 100 x ....)  = 100^100 (not very efficient, but works)
#     - for column 1, place a queen in the in the row (row1)
#     - for column 2, place a queen in the row (row2)
#     - .... repeat for all 100 columns
#     - check for capture -- if there are none -- found solution, otherwise go back to step 1

# In[ ]:




