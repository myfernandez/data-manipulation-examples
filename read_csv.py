
# coding: utf-8

# In[56]:


import csv


# In[52]:


get_ipython().magic(u'reset')


# In[ ]:





# In[ ]:





# In[57]:


with open('/Users/mfyoma/source_code/numpy-examples/auto-mpg.csv') as csvfile:
 mpg=list(csv.DictReader(csvfile))


# In[ ]:


print mpg[0]


# In[ ]:


print mpg[1]


# In[ ]:


mpg[0].keys()


# In[ ]:


print mpg[0]['mpg']


# In[ ]:


sum1 = 0
for item in mpg:
    sum1 += float(item['mpg'])
print sum1


# In[53]:


a = [float(1),float(2)]
print a
sum(a)


# In[58]:


print sum(float(d['mpg']) for d in mpg)


# In[59]:


print mpg


# In[60]:


print mpg[0]


# In[64]:


print(d['cyl']) for d in mpg


# In[62]:


for d in mpg:
    print d['cyl']
    


# In[65]:


dict = {'item1':1, 'item2':1, 'item3':3}
print dict


# In[69]:


unique_dict = set(dict.values())
print unique_dict


# In[72]:


# one liner for taking just unique cylinders
unique_cylinders = set(d['cyl'] for d in mpg)
print unique_cylinders


# In[76]:


#lets calculate the city mpg for each type of cylinder
ctympgbycyl= []
for c in unique_cylinders:
    summpg = 0
    cyltypecount = 0
    for d in mpg:
        if d['cyl'] == c:
            summpg += float(d['mpg'])
            cyltypecount += 1
    ctympgbycyl.append((c,summpg/cyltypecount))

ctympgbycyl
ctympgbycyl.sort(key=lambda x: x[0])
ctympgbycyl

