
# coding: utf-8

# In[ ]:


# sequences and types examples
# tuple: seuqence of variables, iterable, immutable
# set: non-iterable, non-immutable


# In[15]:


tup1 = (0,'hello',1,'bye')
# tuple elements are indexed with square brackets
print tup1[0] + tup1[2]
type (tup1)


# In[12]:


import csv
def read_csv_file_as_list(filename):
    with open(filename) as csvfile:
     out_list=list(csv.DictReader(csvfile))
    return out_list

filename = '/Users/mfyoma/source_code/data-manipulation-examples/auto-mpg.csv'
# the list here gets initialized by calling the function
mpg_list = read_csv_file_as_list(filename)
print type(read_csv_file_as_list)
print type(mpg_list)


# In[22]:


#list concatenation
list1 = [1,2]
print list1 + list1
print list1*2
# print sum of elements in a list
print 'sum of list values: ' + str(sum(list1))
for index,item in enumerate(list1): print index, item

