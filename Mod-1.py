#!/usr/bin/env python
# coding: utf-8

# ## Loading page source code into Python
# 
# Link: https://pt.wikipedia.org/wiki/Ariquemes

# In[1]:


import requests as req # python standard library for pulling and
                       # pushing data from web


# In[2]:


URL = 'https://pt.wikipedia.org/wiki/Ariquemes'


# In[3]:


r =req.get(URL)


# In[4]:


print(r.content[:2000])#so that we only print first 2000 characters of source codes.


# In[5]:


from bs4 import BeautifulSoup
soup = BeautifulSoup(r.content)


# In[6]:


print(soup.prettify())


# In[ ]:




