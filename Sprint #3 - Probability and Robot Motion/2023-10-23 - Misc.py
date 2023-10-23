#!/usr/bin/env python
# coding: utf-8

# In[4]:


def do_this():
    print("Bob")

def do_that():
    print("Sally")


# In[2]:


do_this()


# In[3]:


do_that()


# In[5]:


print("Bob")


# In[6]:


import random


# In[7]:


get_ipython().run_line_magic('pinfo', 'random.randrange')


# In[10]:


print([random.randrange(0,4) for _ in range(200)])


# In[12]:


print([random.randrange(0,4) for _ in range(200)])


# In[ ]:


timer=Timer()
found=False
while timer.value<1:
    if closest_color()=="tape":
        found=True
        break

if found:  # found the tape
    print("found the tape")
else:
    print("do something else")



# In[13]:


def Wait_or_Color(waittime):
    timer=Timer()
    found=False
    while timer.value<waittime:
        if closest_color()=="tape":
            found=True
            break
    
    return found


# In[ ]:


found=Wait_or_Color(1)
if found:  # found the tape
    print("found the tape")
else:
    print("do something else")

