import numpy as np
L=[]
a=2
n=int(input('entrer la dernière valeur :'))
for i in range(a,n+1):                         #L=list(range(2,n))
    L.append(a)
    i=(i+1)
    a=(a+1)
                                                  # T=np.array(L)
print(L)
L1=[]
while len(L)>1:
    b=L[0]
    L.pop(b)
    if b%L[i]==0:
        L.pop(i)
        L1.append(b)
    else:
        L1.append(b)
        L1.append(i)
TNB=np.array(L1)
print(TNB)
print(len(n),'nombres premiers')

    