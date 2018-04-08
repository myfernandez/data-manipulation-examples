
# coding: utf-8

# In[2]:


#date and time examples
import datetime as dt
import time
print dt.datetime.fromtimestamp(time.time())


# In[3]:


print time.time()


# In[4]:


dt.day


# In[14]:


print dt.date.today()
print dt.datetime.now()
goal_date= dt.date(2019, 2, 28)
(goal_date - dt.date.today()).days

