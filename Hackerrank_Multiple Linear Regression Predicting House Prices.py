#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
F,N=list(map(int,input().split()))
X=[]
y=[]
for i in range(N):
    rows=list(map(float,input().split()))
    X.append(rows[:F])
    y.append(rows[F])


test=[]
for i in range(int(input())):
    test.append(list(map(float,input().split())))
    
    

model=LinearRegression()
model.fit(X,y)
pred=model.predict(test)
for i in range(len(pred)):
    print(pred[i])
    


# In[ ]:




