#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
from mplturtle import *


# ![image.png](attachment:015c0703-2efc-4f62-af6e-f7bfd6b86395.png)

# In[5]:


reset(figsize=(5,5))
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)


# In[8]:


reset(figsize=(5,5))

for i in range(4):
    forward(101)
    right(90)


# In[12]:


reset(figsize=(5,5))
size=30
for i in range(4):
    forward(size)
    right(90)


# In[9]:


def square():
    for i in range(4):
        forward(101)
        right(90)
    


# In[10]:


reset(figsize=(5,5))
square()


# In[13]:


def square(size):
    # as if size=#
    for i in range(4):
        forward(size)
        right(90)
    


# In[14]:


reset(figsize=(5,5))
square(101)


# In[15]:


reset(figsize=(5,5))
square(20)


# In[ ]:





# ![image.png](attachment:69f785f2-d348-45af-9b3e-9e48e099ceab.png)

# In[17]:


reset(figsize=(5,5))
square(30)

left(60)
forward(30)
right(120)
forward(30)


# In[21]:


from numpy import sqrt


# In[22]:


reset(figsize=(5,5))

square_size=30
square(square_size)

roof_size=square_size/sqrt(2)

left(45)
forward(roof_size)
right(90)
forward(roof_size)


# In[23]:


def house(size):
    square_size=size
    square(square_size)
    
    roof_size=square_size/sqrt(2)
    
    left(45)
    forward(roof_size)
    right(90)
    forward(roof_size)    


# In[24]:


reset(figsize=(5,5))
house(30)


# In[25]:


reset(figsize=(5,5))
house(30)

forward(50)

house(30)


# In[28]:


reset(figsize=(5,5))
house(30)

left(45)    # straighten out
penup()     # don't draw
forward(20) # move over
pendown()   # back to drawing

house(30)

left(45)    # straighten out
penup()     # don't draw
forward(20) # move over
pendown()   # back to drawing

house(30)




# In[35]:


reset(figsize=(5,5))

number_of_houses=5
# row of houses
for i in range(number_of_houses):
    house(30)
    
    left(45)    # straighten out
    penup()     # don't draw
    forward(20) # move over
    pendown()   # back to drawing
    
    
left(180)    # turn around
penup()     # don't draw
forward(30*number_of_houses + 20*number_of_houses) # move over
pendown()   # back to drawing
left(180)    # turn around

right(90)
penup()     # don't draw
forward(60) # move over
pendown()   # back to drawing
left(90)

# row of houses
for i in range(number_of_houses):
    if i==0 or i==(number_of_houses-1):
        house(30)   
        left(45)    # straighten out

    else:
        penup()     # don't draw
        forward(30)
        pendown()   # back to drawing
        
    penup()     # don't draw
    forward(20) # move over
    pendown()   # back to drawing


    
left(180)    # turn around
penup()     # don't draw
forward(30*number_of_houses + 20*number_of_houses) # move over
pendown()   # back to drawing
left(180)    # turn around

right(90)
penup()     # don't draw
forward(60) # move over
pendown()   # back to drawing
left(90)

# row of houses
for i in range(number_of_houses):
    house(30)
    
    left(45)    # straighten out
    penup()     # don't draw
    forward(20) # move over
    pendown()   # back to drawing
    
    
left(180)    # turn around
penup()     # don't draw
forward(30*number_of_houses + 20*number_of_houses) # move over
pendown()   # back to drawing
left(180)    # turn around

right(90)
penup()     # don't draw
forward(60) # move over
pendown()   # back to drawing
left(90)


# In[40]:


def forward_nodraw(length):
    penup()     # don't draw
    forward(length) # move over
    pendown()   # back to drawing    


# In[41]:


def row_of_houses(number_of_houses):
    # row of houses
    for i in range(number_of_houses):
        house(30)
        
        left(45)    # straighten out
        forward_nodraw(20)
        


# In[42]:


def next_row(number_of_houses):
    left(180)    # turn around
    forward_nodraw(30*number_of_houses + 20*number_of_houses)
    left(180)    # turn around
    
    right(90)
    forward_nodraw(60)
    left(90)    


# In[45]:


reset(figsize=(5,5))
row_of_houses(5)
next_row(5)
row_of_houses(5)


# In[46]:


reset(figsize=(5,5))
for row in range(5):
    row_of_houses(5)
    next_row(5)


# In[47]:


def row_of_houses(number_of_houses,skip_middle=False):
    # row of houses
    for i in range(number_of_houses):
        if skip_middle:


            if i==0 or i==(number_of_houses-1):
                house(30)   
                left(45)    # straighten out
            else:
                forward_nodraw(30)

        
        else:
            house(30)
            left(45)    # straighten out
        forward_nodraw(20)
        


# In[50]:


reset(figsize=(5,5))
row_of_houses(5)
next_row(5)
row_of_houses(5,skip_middle=True)
next_row(5)
row_of_houses(5)


# In[ ]:





# In[ ]:





# In[ ]:





# Write a function that takes size and shape as arguments.  Things like shape='square' or shape='hexagon', size=30, etc...
# 
# ![image.png](attachment:30fef6fa-30d9-4e64-93b2-17d3ef57e24f.png)
# 
# include triangle, square, pentagon and hexagon.

# In[55]:


def square(size):
    # as if size=#
    for i in range(4):
        forward(size)
        right(90)

def triangle(size):
    for i in range(3):
        forward(size)
        right(360/3)

def pentagon(size):
    for i in range(5):
        forward(size)
        right(360/5)


# In[60]:


reset(figsize=(5,5))
square(50)
forward_nodraw(70)
triangle(50)

forward_nodraw(70)
pentagon(50)


# In[65]:


def draw_shape(shape,size):

    if shape=='square':
        square(size)
    elif shape=='triangle':
        triangle(size)
    elif shape=='pentagon':
        pentagon(size)
    else:
        print("I don't know how to draw a shape called ",shape,"of size ",size)


# In[66]:


reset(figsize=(5,5))
draw_shape('square',50)
forward_nodraw(70)
draw_shape('triangle',50)
forward_nodraw(70)
draw_shape('pentagon',50)


# In[67]:


def draw_shape(shape,size):

    if shape=='square':
        N=4
    elif shape=='triangle':
        N=3
    elif shape=='pentagon':
        N=5
    else:
        print("I don't know how to draw a shape called ",shape,"of size ",size)
        return

    for i in range(N):
        forward(size)
        right(360/N)
    


# In[69]:


reset(figsize=(5,5))
draw_shape('square',50)
forward_nodraw(90)
draw_shape('triangle',30)
forward_nodraw(90)
draw_shape('pentagon',70)


# In[ ]:




