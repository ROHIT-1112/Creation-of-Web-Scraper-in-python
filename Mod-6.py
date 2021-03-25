#!/usr/bin/env python
# coding: utf-8

# # Send POST, PUT and PATCH data with modified headers

# ## Link
# 
# https://jsonplaceholder.typicode.com/posts

# In[1]:


import requests as req
import json

api_link = 'https://jsonplaceholder.typicode.com/posts'


# In[2]:


r = req.get(api_link)
data = json.loads(r.content)
data[0:2]


# In[3]:


r = req.post(api_link)
data = json.loads(r.content)
print(data)


# In[4]:


input_data = {"title":"test title", #post method
             "user_id": 5}

r = req.post(api_link ,input_data)
data = json.loads(r.content)
print(data)


# In[5]:


input_data = {"title":"test title",  #put method
             "user_id": 5}

r = req.put(api_link ,input_data)
data = json.loads(r.content)
print(data)


# In[6]:


input_data = {"title":"test title",  #patch method
             "user_id": 5}

r = req.patch(api_link ,input_data)
data = json.loads(r.content)
print(data)


# In[7]:


input_data = json.dumps({"title":"test title",  #patch method
             "user_id": 5})

headers = {"Content-Type":"application/json"}
r = req.patch(api_link , input_data,headers = headers)
data = json.loads(r.content)
print(data)


# In[ ]:




