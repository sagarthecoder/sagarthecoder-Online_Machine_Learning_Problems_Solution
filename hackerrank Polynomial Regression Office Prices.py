#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
X=[]
y=[]
F,N=list(map(int,input().split()))

for i in range(N):
    row=list(map(float,input().split()))
    X.append(row[0:F])
    y.append(row[F:F+1])
model=PolynomialFeatures(degree=4)
X_poly=model.fit_transform(X)
#model.fit(X_poly,y)
lin=LinearRegression()
lin.fit(X_poly,y)
test=[]

for i in range(int(input())):
    test.append(list(map(float,input().split())))

ans=lin.predict(model.fit_transform(test))
for i in range(len(ans)):
    print(*ans[i])


# In[ ]:




