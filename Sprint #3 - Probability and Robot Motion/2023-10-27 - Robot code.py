#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Robot373 import *


# In[5]:


left,right=Motors("ab")
color_sensor=Sensors(None,None,"color",None)


# In[6]:


def forward(power=30):
    left.power=power
    right.power=power


# In[7]:


forward()
while True:
    r,g,b,something=color_sensor.value
    print(r,g,b,something)
    color=closest_color(r,g,b,
                maroon=[128,0,0],
                gray=[128,128,128],
                white=[256,256,256],
                black=[0,0,0],
                )
    if color!='black':
        break
    Wait(0.05)


# In[8]:


def forward_until_not_color(color_name):
    forward()
    while True:
        r,g,b,something=color_sensor.value
        print(r,g,b,something)
        color=closest_color(r,g,b,
                    maroon=[128,0,0],
                    gray=[128,128,128],
                    white=[256,256,256],
                    black=[0,0,0],
                    )
        if color!='color_name':
            break
        Wait(0.05)


# In[9]:


forward_until_not_color("black")


# In[ ]:




