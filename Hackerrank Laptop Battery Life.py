import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
with open('trainingdata.txt', 'r') as f:
    data = f.read().splitlines()
#print(data)
X=[]
y=[]
for line in data:
    row=(list(map(float,line.split(','))))
    X.append(row[0:1])
    y.append(row[1:])

#print(*X)
#print(*y)
plt.scatter(X, y)
plt.title('Fred\'s Battery Life')
plt.xlabel('Charged time (h)')
plt.ylabel('Laptop usage (h)')
plt.grid()
plt.show()
val=float(input())
if(val<=float(4)):
    print(round(float(val*2),2))
else :
    print(round(float(8),2))