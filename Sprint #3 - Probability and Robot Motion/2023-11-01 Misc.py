#!/usr/bin/env python
# coding: utf-8

# In[1]:


def get_color():
    r,g,b,something=color_sensor.value
    color=closest_color(r,g,b,
                       floor=[60,70,60],
                        red=[148,26,30],
                        green=[55,175,40],
                       )


# ## scan a little to the left and right and decide where the green is

# In[ ]:


# left turn
left.power=-20
right.power=20
Wait(0.3)

color_left=get_color()


# right turn
left.power=20
right.power=-20
Wait(0.6)
color_right=get_color()

if color_right=="green":
    pass
if color_left=="green":
    left.power=-20
    right.power=20
    Wait(0.6)
    



# In[ ]:


def scan_for_color(target_color):
    # left turn
    left.power=-20
    right.power=20
    Wait(0.3)
    
    color_left=get_color()
    
    
    # right turn
    left.power=20
    right.power=-20
    Wait(0.6)
    color_right=get_color()
    
    if color_right==target_color:
        pass
    if color_left==target_color:
        left.power=-20
        right.power=20
        Wait(0.6)
        
    left.power=0
    right.power=0
    
    


# In[ ]:


def scan_for_color(target_color):
    # left turn
    left.power=-20
    right.power=20
    Wait(0.3)
    
    color=get_color()

    if color==target_color:
        left.power=0
        right.power=0
    else:
        turn_right_until_color(target_color)
        
    
 


# ## always turn left until green

# In[ ]:


left.power=-20
right.power=20
while True:
    color=get_color()
    if color=="green":
        break
left.power=0
right.power=0


# In[ ]:


def turn_left_until_color(target_color):
    left.power=-20
    right.power=20
    while True:
        color=get_color()
        if color==target_color:
            break
    left.power=0
    right.power=0
        


# In[ ]:


turn_left_until_color("green")

