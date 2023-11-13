#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *


# In[80]:


im=imread('images/cats.jpg')


# In[81]:


imshow(im)  # subimage im[400:800,300:700,:]


# ## rotating the image

# In[82]:


im=rot90(im)
imshow(im)


# ## Back to the original

# In[83]:


im=imread('images/cats.jpg')


# In[84]:


im.shape


# In[85]:


im[500,752,:]


# In[86]:


im.max(),im.min()


# In[87]:


subimage=im[400:800,300:700,:]
imshow(subimage)


# In[88]:


another=im[:,:,0]
imshow(another)
colorbar()


# In[89]:


another=im[:,:,1]
imshow(another)
colorbar()


# In[90]:


another=im[:,:,2]
imshow(another)
colorbar()


# In[91]:


subimage=im[400:800,1500:,:]
imshow(subimage)


# In[92]:


for i in range(4):
    if i==0:
        subplot(2,2,1)
        imshow(subimage)
    else:
        subplot(2,2,i+1)
        imshow(subimage[:,:,i-1],cmap=cm.gray)
        


# In[ ]:





# In[93]:


im=imread('images/cat1.png')
imshow(im)


# In[94]:


im.shape


# In[95]:


subimage=im[:,:,3]
imshow(subimage)
colorbar()


# In[96]:


im.min(),im.max()


# In[97]:


im=imread('images/connect4.png')


# In[98]:


imshow(im)


# In[99]:


square_size=50
center_columns=arange(50,600,100)
center_columns


# In[100]:


imshow(im)
center_columns=arange(50,600,100)  # first attempt
for x in center_columns:
    plot([x,x],[0,530],'k-',lw=2)


# In[101]:


imshow(im)
center_columns=arange(58,600,87)
for x in center_columns:
    plot([x,x],[0,530],'k-',lw=2)

center_rows=arange(58,580,87)
for y in center_rows:
    plot([0,600],[y,y],'g-',lw=2)


# In[102]:


center_rows


# In[103]:


center_columns


# In[104]:


locations=[]
for row in center_rows:
    for col in center_columns:
        locations.append([row,col])
locations


# In[105]:


imshow(im)
for r,c in locations:
    plot([c],[r],'o')


# In[106]:


r,c=[319, 58]


# In[107]:


r


# In[108]:


c


# In[109]:


sr=r-square_size//2
er=sr+square_size
sc=c-square_size//2
ec=sc+square_size
sr,er,sc,ec


# In[110]:


subimage=im[sr:er,sc:ec,:]
subimage.shape


# In[111]:


imshow(subimage)


# In[114]:


count=0
for r,c in locations:
    sr=r-square_size//2
    er=sr+square_size
    sc=c-square_size//2
    ec=sc+square_size   
    subimage=im[sr:er,sc:ec,:]

    subplot(6,7,count+1)
    imshow(subimage)

    if count==0:
        example_white=subimage
    if count==16:
        example_yellow=subimage
    if count==17:
        example_red=subimage

    
    count+=1


# In[115]:


imshow(im)


# In[116]:


subplot(1,3,1)
imshow(example_red)

subplot(1,3,2)
imshow(example_yellow)

subplot(1,3,3)
imshow(example_white)


# In[47]:


subimage


# In[48]:


def closest_color(r,g,b,**kwargs):
    """
    C=closest_color(100,0,0,
            red=[100,0,0],
            green=[0,100,0],
            black=[100,100,100],
            )
    """
    min_distance_sq=0
    min_color=None

    for color in kwargs:

        r2,g2,b2=kwargs[color]

        distance_sq=(r-r2)**2+(g-g2)**2+(b-b2)**2

        if min_color is None:  # first color
            min_color=color
            min_distance_sq=distance_sq
        elif distance_sq<min_distance_sq:
            min_color=color
            min_distance_sq=distance_sq
        else:
            pass

    return min_color


# In[117]:


pixel_red=example_red[25,25,:]
pixel_white=example_white[25,25,:]
pixel_yellow=example_yellow[25,25,:]
pixel_red,pixel_yellow,pixel_white


# In[ ]:





# In[121]:


closest_color(*pixel_red,
             red=[1,0,0],
             yellow=[1,1,0],
             white=[1,1,1])


# In[122]:


closest_color(*pixel_white,
             red=[1,0,0],
             yellow=[1,1,0],
             white=[1,1,1])


# In[123]:


closest_color(*pixel_yellow,
             red=[1,0,0],
             yellow=[1,1,0],
             white=[1,1,1])


# In[124]:


def classify_one_square(subimage):
    one_pixel=subimage[25,25,:]
    return closest_color(*one_pixel,
                 red=[1,0,0],
                 yellow=[1,1,0],
                 white=[1,1,1])    


# In[127]:


from Game import Board
state=Board(6,7)


# In[128]:


count=0
figure(figsize=(10,12))
values=[]
for r,c in locations:
    sr=r-square_size//2
    er=sr+square_size
    sc=c-square_size//2
    ec=sc+square_size   
    subimage=im[sr:er,sc:ec,:]

    subplot(6,7,count+1)
    imshow(subimage)

    color=classify_one_square(subimage)
    title(color)

    if color=='white':
        values.append(0)
    if color=='red':
        values.append(1)
    if color=='yellow':
        values.append(2)
    count+=1

state.board=values



# In[129]:


state


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[63]:


import json
with open('locations.json') as json_file:
    locations = json.load(json_file)


# In[64]:


locations


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ## Some Misc Off-topic stuff below

# In[65]:


col=2


# In[66]:


if col==1:
    color='red'
elif col==2:
    color='blue'
elif col==3:
    color='green'


# In[67]:


color


# In[68]:


colors=['red','blue','green']
color=colors[col-1]


# In[69]:


color


# In[70]:


colors={1:'red',2:'blue',3:'green'}
color=colors[col]
color


# In[72]:


imshow(im)


# In[ ]:




