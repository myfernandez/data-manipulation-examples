
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


# In[17]:


linear = np.linspace(0,4,9)
print linear


# In[18]:


print linear.reshape(3,3)


# In[19]:


print linear.resize(3,3)


# In[20]:


print linear


# In[21]:


print z.resize(2,3)


# In[22]:


print z.resize(3,2)


# In[23]:


print z


# In[25]:


np.ones((3,2))


# In[26]:


np.zeros((2,2))


# In[27]:


np.diag(y)


# In[30]:


np.repeat([1,2,3],3)


# In[31]:


np.array([1,2,3]*3)


# In[32]:


p=np.ones([2,3],int)
p


# In[33]:


np.array(p*2)


# In[34]:


#notice the difference between operations in a list and array
#for example [1,2,3]*3 is different than array([1,2,3])*3


# In[35]:


np.array([1,2,3])*3



# In[36]:


np.array([1,2,3]*3)

