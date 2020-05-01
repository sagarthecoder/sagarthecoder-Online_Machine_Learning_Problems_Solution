#!/usr/bin/env python
# coding: utf-8

# In[1]:



x=[ 15 , 12,  8 ,  8 ,  7  , 7  , 7  , 6 ,  5 ,  3]
y=[10 , 25,  17 , 11 , 13 , 17 , 20 , 13 , 9  , 15]


# In[2]:


sz=len(x)


# In[3]:


sumxy=0
sumxx=0
avgx=sum(x)/sz
avgy=sum(y)/sz
up=0
down=0
for i in range(0,sz):
    up+=((x[i]-avgx)*(y[i]-avgy))
    down+=((x[i]-avgx)**2)

SlopeRes=up/down
print(round(SlopeRes,3))

    


# In[ ]:





# In[ ]:




