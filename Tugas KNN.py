#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[7]:


pd.__version__


# In[8]:


data = np.array([[1.,1.,'OR'], [1.,2.,'OR'], [1.,2.5,'OR'], [3.,3.,'GF'], [3.5,2.5,'GF'], [4.,3.,'GF'], [3.,2.5,'NN']])
query = [3.,2.5,'NN']


# In[9]:


df = pd.DataFrame(data)
df.columns = ['x','y', 'cat']
df


# In[12]:


for i in range(7):
    if(df.iloc[i]['cat'] == 'GF'):
        plt.scatter(df.iloc[i]['x'], df.iloc[i]['y'], s=100, c='r')
    elif(df.iloc[i]['cat'] == 'OR'):
        plt.scatter(df.iloc[i]['x'], df.iloc[i]['y'], s=100, c='y')
    else:
        plt.scatter(df.iloc[i]['x'], df.iloc[i]['y'], s=200, c='b')
plt.grid()
plt.show()


# In[14]:


import math
dis = []
for i in range(7):
    dis.append(math.sqrt((float(df.iloc[i]['x']) - query[0])**2 + (float(df.iloc[i]['y']) - query[1])**2))


# In[15]:


df['dis'] = dis
df


# In[ ]:





# In[ ]:




