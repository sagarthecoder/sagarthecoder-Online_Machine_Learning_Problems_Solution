#!/usr/bin/env python
# coding: utf-8

# In[4]:



x=[ 15 , 12,  8 ,  8 ,  7  , 7  , 7  , 6 ,  5 ,  3]
y=[10 , 25,  17 , 11 , 13 , 17 , 20 , 13 , 9  , 15]
sz=len(x)

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
cons=avgy-(SlopeRes*avgx)

ans=(SlopeRes*10)+cons
print(round(ans,1))

