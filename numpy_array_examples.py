
# coding: utf-8

# In[1]:


##playing with arrays in Numpy


# In[3]:


import numpy as np


# In[7]:


# passing lists
mylist = [1,2,3]
x = np.array(mylist)
x


# In[11]:


y = np.array([4,5,6])
y


# In[14]:


# stacking lists vertically to build a (2,3) array
z = np.vstack((x,y))
z


# In[15]:


np.shape(z)

