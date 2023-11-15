#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *


# In[2]:


from classy import *


# In[3]:


data=load_excel('data/iris.xls')


# In[4]:


data.vectors


# In[5]:


data.targets


# In[6]:


data.target_names


# In[7]:


plot2D(data)


# In[10]:


subset=extract_features(data,[0,2])


# In[11]:


plot2D(subset)


# In[12]:


C=NaiveBayes()
C.fit(data.vectors,data.targets)


# In[13]:


print("On the full data set:",C.percent_correct(data.vectors,data.targets))


# In[14]:


C=NaiveBayes()
C.fit(subset.vectors,subset.targets)
print("On the subset data:",C.percent_correct(subset.vectors,subset.targets))


# In[17]:


plot2D(subset,C)
C.plot_centers()


# In[18]:


C=kNearestNeighbor()
C.fit(subset.vectors,subset.targets)
print("On the subset data:",C.percent_correct(subset.vectors,subset.targets))


# In[19]:


plot2D(subset,C)


# In[20]:


C=kNearestNeighbor(k=1)
C.fit(subset.vectors,subset.targets)
print("On the subset data:",C.percent_correct(subset.vectors,subset.targets))


# In[21]:


plot2D(subset,C)


# In[24]:


images=image.load_images('images/digits')


# In[26]:


images=remap_targets(images,new_target_names=['0','1','2','3','4','5','6','7','8','9'])


# In[27]:


data=image.images_to_vectors(images)


# In[28]:


C=NaiveBayes()
C.fit(data.vectors,data.targets)
print("On the full data set:",C.percent_correct(data.vectors,data.targets))


# In[30]:


C=kNearestNeighbor(k=1)
C.fit(data.vectors,data.targets)
print("On the full data set:",C.percent_correct(data.vectors,data.targets))


# In[31]:


training_data,testing_data=split(data)


# In[32]:


C=NaiveBayes()
C.fit(training_data.vectors,training_data.targets)
print("On the training data set:",C.percent_correct(training_data.vectors,training_data.targets))
print("On the test data set:",C.percent_correct(testing_data.vectors,testing_data.targets))


# In[33]:


C=kNearestNeighbor()
C.fit(training_data.vectors,training_data.targets)
print("On the training data set:",C.percent_correct(training_data.vectors,training_data.targets))
print("On the test data set:",C.percent_correct(testing_data.vectors,testing_data.targets))


# In[34]:


C=kNearestNeighbor(k=1)
C.fit(training_data.vectors,training_data.targets)
print("On the training data set:",C.percent_correct(training_data.vectors,training_data.targets))
print("On the test data set:",C.percent_correct(testing_data.vectors,testing_data.targets))


# In[35]:


C=NaiveBayes()
C.fit(training_data.vectors,training_data.targets)
print("On the training data set:",C.percent_correct(training_data.vectors,training_data.targets))
print("On the test data set:",C.percent_correct(testing_data.vectors,testing_data.targets))


# In[37]:


C.means.shape


# In[39]:


imshow(C.means[5,:].reshape(8,8),cmap=cm.gray)


# In[40]:


images=image.load_images('images/board images/squares')


# In[43]:


images=remap_targets(images,new_target_names=['blank','red','black'])


# In[44]:


summary(images)


# In[45]:


data=image.images_to_vectors(images)


# In[46]:


45*45*3


# In[47]:


C=NaiveBayes()
C.fit(data.vectors,data.targets)
print("On the full data set:",C.percent_correct(data.vectors,data.targets))


# In[ ]:




