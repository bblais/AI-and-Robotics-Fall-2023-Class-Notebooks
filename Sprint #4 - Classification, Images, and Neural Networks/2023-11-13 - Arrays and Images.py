#!/usr/bin/env python
# coding: utf-8

# In[5]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *


# In[21]:


im=imread('images/cats.jpg')


# In[22]:


imshow(im)  # subimage im[400:800,300:700,:]


# In[9]:


im.shape


# In[10]:


im[500,752,:]


# In[11]:


im.max(),im.min()


# In[23]:


subimage=im[400:800,300:700,:]
imshow(subimage)


# In[25]:


another=im[:,:,0]
imshow(another)
colorbar()


# In[26]:


another=im[:,:,1]
imshow(another)
colorbar()


# In[27]:


another=im[:,:,2]
imshow(another)
colorbar()


# In[28]:


subimage=im[400:800,1500:,:]
imshow(subimage)


# In[31]:


for i in range(4):
    if i==0:
        subplot(2,2,1)
        imshow(subimage)
    else:
        subplot(2,2,i+1)
        imshow(subimage[:,:,i-1],cmap=cm.gray)
        


# In[ ]:





# In[16]:


im=imread('images/cat1.png')
imshow(im)


# In[17]:


im.shape


# In[19]:


subimage=im[:,:,3]
imshow(subimage)
colorbar()


# In[20]:


im.min(),im.max()


# In[ ]:




