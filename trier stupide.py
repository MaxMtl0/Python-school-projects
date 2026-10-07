import numpy as np
import random 
NbColonnes=10
L=[]
for i in range(0,NbColonnes):
    a=random.randint(0,100)
    L.append(a)
T=np.array(L)
print(T)
test=True
while test:               
    b=random.randint(0,9)         
    c=random.randint(0,9)
    B=T[b]
    C=T[c]
    T[b]=C
    T[c]=B
    test=False
    for i in range(len(T)-1):
        if T[i]>T[i+1]:
            test=True
for j in range(10):
    print(int(T[j])," ",end="")

