#!/usr/bin/env python
# coding: utf-8

# # Plotting The Bat Symbol using Python & Matplotlib
# 
# PS:  When Batman fans are bored in the quarantine 

# In[ ]:





# ## Importing All Required Modules-

# In[1]:


import math
import numpy as np
import matplotlib.pyplot as plt


# ## Plotting the Representation -

# In[2]:


Y = np.arange(-4,4,.005)
X = np.zeros((0))
for y in Y:
    X = np.append(X,abs(y/2)-0.09137*y**2+math.sqrt(1-(abs(abs(y)-2)-1)**2)-3)


# In[3]:


Y1 = np.append(np.arange(-7,-3,.01),np.arange(3,7,.01))
X1 = np.zeros((0))
for y in Y1:
    X1 = np.append(X1,3*math.sqrt(-(y/7)**2+1))


# In[4]:


X = np.append(X,X1)
Y = np.append(Y,Y1)


# In[5]:


Y1 = np.append(np.arange(-7.,-4,.01),np.arange(4,7.01,.01))
X1 = np.zeros((0))
for y in Y1:
    X1 = np.append(X1,-3*math.sqrt(-(y/7)**2+1))


# In[6]:


X = np.append(X,X1)
Y = np.append(Y,Y1)


# In[7]:


Y1 = np.append(np.arange(-1,-.8,.01),np.arange(.8,1,.01))
X1 = np.zeros((0))
for y in Y1:
    X1 = np.append(X1, 9-8*abs(y))


# In[8]:


X = np.append(X,X1)
Y = np.append(Y,Y1)


# In[9]:


Y1 = np.arange(-.5,.5,.05)
X1 = np.zeros((0))
for y in Y1:
    X1 = np.append(X1,2)


# In[10]:


X = np.append(X,X1)
Y = np.append(Y,Y1)


# In[11]:


Y1 = np.append(np.arange(-2.9,-1,.01), np.arange(1,2.9,.01))
X1 = np.zeros((0))
for y in Y1:
    X1 = np.append(X1, 1.5-.5*abs(y)-1.89736*(math.sqrt(3-y**2+2*abs(y))-2))


# In[12]:


X = np.append(X,X1)
Y = np.append(Y,Y1)


# In[13]:


Y1 = np.append(np.arange(-.7,-.45,.01), np.arange(.45,.7,.01))
X1 = np.zeros((0))
for y in Y1:
    X1 = np.append(X1,3*abs(y)+.75)


# In[14]:


X = np.append(X,X1)
Y = np.append(Y,Y1)


# ## Plotting the Result -

# In[15]:


plt.plot(Y,X,'bo')
plt.grid()
plt.show()


#                                                                                               <> Crafted by Akshad Kolhatkar
