#!/usr/bin/env python
# coding: utf-8

# # Use CSS selectors for searching complex patterns

# ## Link
# 
# https://pt.wikipedia.org/wiki/Rond%C3%B4nia

# In[ ]:





# In[1]:


import requests as req
from bs4 import BeautifulSoup

URL = 'https://pt.wikipedia.org/wiki/Rond%C3%B4nia'
r = req.get(URL)
soup = BeautifulSoup(r.content)


# In[2]:


selector = "div.thumb:nth-child(49) > div:nth-child(1) > a:nth-child(1) > img:nth-child(1)"


# In[3]:


soup.select(selector)


# In[ ]:




