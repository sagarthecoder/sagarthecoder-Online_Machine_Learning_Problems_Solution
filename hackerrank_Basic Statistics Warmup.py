import numpy as np 
import math
from scipy import stats
n=int(input())
ara=list(map(int,input().split()))

mn=np.mean(ara)
print(round(mn,1))
ara.sort()
mdo=0
mid=int(n/2)
if(n%2!=0):
    mdo=ara[mid]
else :
    mdo=float(float((ara[mid]+ara[mid-1]))/float(2))
print(round(mdo,1))
mod=stats.mode(ara)
print(mod[0][0])
st=np.std(ara)

print(round(st,1))
frac=(float(1.960))*(st/math.sqrt(n))
low=mn-frac
high=mn+frac
print(round(low,1),round(high,1))
