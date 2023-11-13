#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *


# In[4]:


im=imread('images/cats.jpg')


# In[5]:


imshow(im)  # subimage im[400:800,300:700,:]


# In[6]:


im.shape


# In[7]:


im[500,752,:]


# In[8]:


im.max(),im.min()


# In[9]:


subimage=im[400:800,300:700,:]
imshow(subimage)


# In[10]:


another=im[:,:,0]
imshow(another)
colorbar()


# In[11]:


another=im[:,:,1]
imshow(another)
colorbar()


# In[12]:


another=im[:,:,2]
imshow(another)
colorbar()


# In[13]:


subimage=im[400:800,1500:,:]
imshow(subimage)


# In[14]:


for i in range(4):
    if i==0:
        subplot(2,2,1)
        imshow(subimage)
    else:
        subplot(2,2,i+1)
        imshow(subimage[:,:,i-1],cmap=cm.gray)
        


# In[ ]:





# In[15]:


im=imread('images/cat1.png')
imshow(im)


# In[16]:


im.shape


# In[17]:


subimage=im[:,:,3]
imshow(subimage)
colorbar()


# In[18]:


im.min(),im.max()


# In[19]:


im=imread('images/connect4.png')


# In[20]:


imshow(im)


# In[21]:


square_size=50
center_columns=arange(50,600,100)
center_columns


# In[26]:


imshow(im)
center_columns=arange(58,600,87)
for x in center_columns:
    plot([x,x],[0,530],'k-',lw=2)

center_rows=arange(58,580,87)
for y in center_rows:
    plot([0,600],[y,y],'g-',lw=2)


# In[27]:


center_rows


# In[28]:


center_columns


# In[29]:


locations=[]
for row in center_rows:
    for col in center_columns:
        locations.append([row,col])
locations


# In[31]:


imshow(im)
for r,c in locations:
    plot([c],[r],'o')


# In[35]:


r,c=[319, 58]


# In[36]:


r


# In[37]:


c


# In[33]:


sr=r-square_size//2
er=sr+square_size
sc=c-square_size//2
ec=sc+square_size
sr,er,sc,ec


# In[34]:


subimage=im[sr:er,sc:ec,:]
subimage.shape


# In[38]:


imshow(subimage)


# In[39]:


count=1
for r,c in locations:
    sr=r-square_size//2
    er=sr+square_size
    sc=c-square_size//2
    ec=sc+square_size   
    subimage=im[sr:er,sc:ec,:]

    subplot(6,7,count)
    imshow(subimage)

    count+=1


# In[40]:


imshow(im)


# In[41]:


imshow(subimage)


# In[ ]:




