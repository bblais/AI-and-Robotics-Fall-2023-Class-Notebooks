#!/usr/bin/env python
# coding: utf-8

# In[15]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *


# In[16]:


from classy import *


# In[40]:


images=image.load_images('images/training squares/')
images=remap_targets(images,new_target_names=['blank','player1','player2'])
summary(images)


# In[41]:


images['data'][0].shape


# In[42]:


data=image.images_to_vectors(images)


# In[43]:


data_train,data_test=split(data,test_size=0.2)


# ## Naive Bayes

# In[21]:


C=NaiveBayes()
C.fit(data_train.vectors,data_train.targets)
print("On Training Set:",C.percent_correct(data_train.vectors,data_train.targets))
print("On Test Set:",C.percent_correct(data_test.vectors,data_test.targets))


# In[22]:


C.means


# In[23]:


C.means.shape


# In[24]:


mean0=C.means[0,:]


# In[25]:


mean0.shape


# In[26]:


im0=mean0.reshape((50,50,3))
im0=im0-im0.min()  # set the min to zero
im0=im0/im0.max()  # set the max to 1


# In[27]:


imshow(im0)


# In[28]:


for i in range(3):
    subplot(1,3,i+1)
    mean0=C.means[i,:]
    im0=mean0.reshape((50,50,3))
    im0=im0-im0.min()  # set the min to zero
    im0=im0/im0.max()  # set the max to 1
    imshow(im0)


# ## CSC

# In[44]:


C=CSC()
C.fit(data_train.vectors,data_train.targets)
print("On Training Set:",C.percent_correct(data_train.vectors,data_train.targets))
print("On Test Set:",C.percent_correct(data_test.vectors,data_test.targets))


# In[46]:


C.centers.shape


# In[47]:


C.targets


# In[50]:


for i in range(18):  # make sure this matches the shape
    subplot(3,6,i+1) # make sure that the 3 and 6 multiply to be greater than or equal to the number of centers

    mean0=C.centers[i,:]
    im0=mean0.reshape((50,50,3))
    im0=im0-im0.min()  # set the min to zero
    im0=im0/im0.max()  # set the max to 1
    imshow(im0) 
    title(C.targets[i])


# ## kNearestNeighbor -- you can't visualize this classifier.  Why?

# In[ ]:





# In[ ]:





# ## Perceptron

# ### for neural networks, it helps a lot to standardize the inputs (subtract mean, divide by stdev)

# In[29]:


standardize(data)
summary(data)


# In[30]:


data_train,data_test=split(data,test_size=0.2)


# In[31]:


data_train.vectors.shape


# In[32]:


number_of_features=data_train.vectors.shape[1]
number_of_categories=3  # the types of pieces


# In[33]:


C=NumPyNetBackProp({
    'input':number_of_features,               # number of features
    'output':(number_of_categories,'linear'),  # number of classes
    'cost':'mse',
})


# In[34]:


C.fit(data_train.vectors,data_train.targets,epochs=5000)   # you'll want to increase epochs here


# In[35]:


print(("On Training Set:",C.percent_correct(data_train.vectors,data_train.targets)))
print(("On Test Set:",C.percent_correct(data_test.vectors,data_test.targets)))


# In[36]:


len(C.weights)


# In[37]:


C.weights[0]  # first layer


# In[38]:


W=C.weights[0]
W.shape


# In[39]:


for i in range(3):
    subplot(1,3,i+1)
    vec=W[:,i]
    vec=(vec-W.min())/(W.max()-W.min())  # rescale to 0-1
    im=vec.reshape((50,50,3))
    imshow(im)


# ## Playing with reverse correlation -- not much useful here it turns out

# In[128]:


X=rand(20000,7500)


# In[129]:


C.output(X)[0].shape


# In[130]:


y=C.output(X)[0]


# In[131]:


output_images=[]
for v in y.T:
    v=atleast_2d(v)
    im_vec=(v.T*X).sum(axis=0)
    im_vec=(im_vec-im_vec.min())/(im_vec.max()-im_vec.min()) 
    im=im_vec.reshape(50,50,3)
    output_images.append(im)


# In[132]:


for i in range(3):
    subplot(1,3,i+1)
    imshow(output_images[i])


# In[ ]:





# In[ ]:





# ## Multiple layer, nonlinear

# In[11]:


C=NumPyNetBackProp({
    'input':number_of_features,               # number of features
    'hidden':[(6,'logistic'),],   # this size is "arbitrary"
    'output':(number_of_categories,'logistic'),  # number of classes
    'cost':'mse',
})


# In[12]:


C.fit(data_train.vectors,data_train.targets,epochs=500)   # you'll want to increase epochs here


# In[13]:


print(("On Training Set:",C.percent_correct(data_train.vectors,data_train.targets)))
print(("On Test Set:",C.percent_correct(data_test.vectors,data_test.targets)))


# In[14]:


len(C.weights)


# In[15]:


W=C.weights[0]
W.shape


# In[16]:


W=C.weights[1]
W.shape


# In[17]:


W=C.weights[0]
for i in range(4):
    subplot(2,3,i+1)
    vec=W[:,i]
    vec=(vec-W.min())/(W.max()-W.min())  # rescale to 0-1
    im=vec.reshape((50,50,3))
    imshow(im)


# In[ ]:





# In[142]:


X=rand(20000,7500)
y=C.output(X)


# In[143]:


y[0].shape


# In[148]:


for i in range(11):
    pass
print(i)


# In[150]:


from tqdm import tqdm


# In[160]:


def reverse_correlation(C,N=20000):
    X=rand(N,7500)
    y=C.output(X)

    all_ims=[]
    for l in range(len(y)):    
        i=0
        ims=[]
        for v in y[l].T:
            v=atleast_2d(v)
            im_vec=(v.T*X).sum(axis=0)/N
            #im_vec=(im_vec-im_vec.min())/(im_vec.max()-im_vec.min()) 
            im=im_vec.reshape(50,50,3)

            ims.append(im)
    
            i+=1  
        all_ims.append(ims)

    return all_ims


# In[161]:


all_ims=reverse_correlation(C)


# In[162]:


for k,ims in enumerate(all_ims):
    for i,im in enumerate(ims):
        print(all_ims[k][i].min(),all_ims[k][i].max())


# In[167]:


num_repeat=20  # 60 
for repeat in tqdm(range(num_repeat)):
    all_ims2=reverse_correlation(C)

    for k,ims in enumerate(all_ims2):
        for i,im in enumerate(ims):
            all_ims[k][i]+=im    


# In[169]:


for ims in all_ims:
    figure()
    n=len(ims) 
    c=int(ceil(sqrt(n)))
    r=n//c
    if r*c<n:
        r+=1

    
    for i,im in enumerate(ims):
        subplot(r,c,i+1)

        im=(im-im.min())/(im.max()-im.min()) 
        imshow(im)


# In[ ]:




