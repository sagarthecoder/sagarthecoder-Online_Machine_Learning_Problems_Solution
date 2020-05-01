#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


score1=[ 15 , 12 , 8 ,  8 ,  7 ,  7 ,  7 ,  6 ,  5 ,  3]
score2=[10 , 25 , 17 , 11 , 13 , 17 , 20 , 13 , 9  , 15]


# In[3]:


sum1=sum(score1)
sum2=sum(score2)


# In[4]:


sumxy=0
sumxx=0
sumyy=0
for i in range(0,len(score1)):
    sumxy=sumxy+(score1[i]*score2[i])
    sumxx+=(score1[i]**2)
    sumyy+=(score2[i]**2)


# In[5]:


sz=len(score1)
up=(sz*sumxy)-(sum1*sum2)
down=((sz*sumxx)-(sum1**2))*((sz*sumyy)-(sum2**2))
down=down**(1/2)

r=up/down
#print(up)
#print(down)
print(round(r,3))

 

