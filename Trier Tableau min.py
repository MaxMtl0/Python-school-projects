import numpy as np
import random
NbColonnes=int(input('entre le nombre de cases :'))
L=[]                                                 #L[1,12,-6,...]
for i in range(0,NbColonnes):
    a=random.randint(1,100)
    L.append(a)
T=np.array(L)
print(T)
print(T.min())                                      #plus petit nb du tableau
i=0
min=T[0]
for j in range(1,len(T)):
    if T[j]<min:
        min=T[j]
        i=j
print(i)
                                                    #emplacement du nb
    
