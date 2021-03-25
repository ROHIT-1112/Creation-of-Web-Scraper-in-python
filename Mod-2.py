#!/usr/bin/env python
# coding: utf-8

# # Access elements and attributes inside HTML pages

# In[1]:


import requests as req
from bs4 import BeautifulSoup


# In[2]:


URL = 'https://pt.wikipedia.org/wiki/Ariquemes'
r = req.get(URL)
soup = BeautifulSoup(r.content)


# In[3]:


soup.prettify()[:1000]


# In[4]:


title = soup.h1
print(title)


# In[5]:


print(soup.img)


# In[6]:


print(soup.h2)


# In[7]:


print(soup.ul)


# In[8]:


print(soup.li)


# In[9]:


tables = soup.find_all("table") # finding total no. of tables in webpage.
print(len(tables))


# In[10]:


print(tables[1]) # checking a particular table source codes.


# In[11]:


tables[1]["style"]# checking a particular table style


# In[12]:


lists = soup.find_all("li") # checking total list in source code
print(len(lists))


# In[13]:


childs = list(lists[3].children)


# In[14]:


print(len(childs))
print(childs)


# In[ ]:




