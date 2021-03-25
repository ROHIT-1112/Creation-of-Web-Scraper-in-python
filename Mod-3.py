#!/usr/bin/env python
# coding: utf-8

# # Search for elements with given classes and attributes

# In[2]:


import requests as req
from bs4 import BeautifulSoup


# In[3]:


URL = 'https://pt.wikipedia.org/wiki/Ariquemes'
r = req.get(URL)
soup = BeautifulSoup(r.content)


# In[4]:


links = soup.find_all("a") # finding total number of links in source code
print(len(links))         # "a" :- is anchor tag used in creating links in html


# In[5]:


links[0:5]


# In[6]:


attr_filter ={"class":"mw-jump-link"} # selecting link which "mw-jump-link"
soup.find_all("a",attr_filter)                


# In[7]:


attr_filter ={"class":"mw-jump-link",
              "href":"#content"} # selecting link which "mw-jump-link"
soup.find_all("a",attr_filter)   # selecting href attribute         


# In[8]:


attr_filter = {"class":"no-print"}
soup.find_all(None,attr_filter)


# In[ ]:




