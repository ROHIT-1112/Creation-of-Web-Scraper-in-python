#!/usr/bin/env python
# coding: utf-8

# # Authenticate and mantain connections through cookies and sessions

# ## Link
# 
# http://testing-ground.scraping.pro/login

# In[ ]:





# In[1]:


import requests as req

link = 'http://testing-ground.scraping.pro/login'


# In[2]:


from bs4 import BeautifulSoup

LOGGED_SELECTOR = '#case_login > h3'

def is_logged(html_source):
    soup = BeautifulSoup(html_source)
    elements = soup.select(LOGGED_SELECTOR)
    if len(elements) == 1:
        element = elements[0]
        if 'success' in element.get('class', []):
            return True
        else:
            return False
    elif len(elements) > 1:
        raise Exception('Something is wrong with the source')
    else:
        return False


# In[ ]:


input_data = {"usr":"admin",
             "pwd":"12345"}

r_post = req.post(link +"?mode = login" ,input_data)
r_get = req.get(link + "?mode = welcome")

is_logged(r_get.content)


# In[ ]:


input_data = {"usr":"admin",
             "pwd":"12345"}

r_post = req.post(link +"?mode = login" ,input_data)


is_logged(r_post.content)


# In[ ]:





input_data = {"usr":"admin",
             "pwd":"12345"}
s = req.session()
r_post = req.post(link +"?mode = login" ,input_data)
r_get = req.get(link + "?mode = welcome")

is_logged(r_get.content)


# In[ ]:




