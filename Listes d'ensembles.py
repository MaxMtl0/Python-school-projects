import random
L=[]
for i in range(30):
    a=random.randint(10,99)
    L.append(a)
print('Liste :',L)
L3=[]
LR=[]
for a in L:
    if a%3==0:
        L3.append(a)
    else:
        LR.append(a)
print("Avant modification:\nL3={}\nLR={}\n".format(L3,LR))
for a in L3:
    if a%2==0:
        L3.remove(a)
for a in LR:
    if a%5==0:
        LR.remove(a)
L3.sort(), LR.sort()
print("Après modification:\nL3={}\nLR={}".format(L3,LR))


