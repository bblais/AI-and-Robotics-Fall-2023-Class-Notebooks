#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Robot373 import *


# In[2]:


r,g,b,something=[277,366,477,715]
color=closest_color(r,g,b,
            RedTape = [270,60,60],
            GreenTape = [80,260,100],
            BlueTape = [140,320,524],
            OrangeTape = [323,115,50],
            Board = [260,350,450],
            )


# In[3]:


color


# In[6]:


def take_picture(filename='picture.jpg',brightness=100,view=False,S=10):

    a=f"fswebcam -s brightness={brightness}%% -r 1600x900 --no-banner -S {S} '{filename}'"
    print(a)


# In[7]:


take_picture()


# In[ ]:




