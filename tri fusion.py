import random

def Fusion(T,g,d,m):
    n1=m-g+1
    n2=d-m
    for i in range(1,n1+1):
        G.append(T[g+i-1])
    for j in range(1,n2+1):
        D.append(T[m+j])
    i=1
    j=1
    G.append(float('inf'))
    D.append(float('inf'))
    for k in range(g,d+1):
        if i<=n1 and G[i]<=D[j]:
            T[k]=G[i]
            i=i+1
        else:
            if j<=n2 and G[i]>=D[j]:
                T[k]=D[j]
                j=j+1
                

def tri_fusion(T,g,d):
    if g<d:
        m=(g+d)//2
        tri_fusion(T,g,m)
        tri_fusion(T,m+1,d)
        Fusion(T,g,d,m)
        
G=[]
D=[]
T=[]        
#création liste
a=10
for i in range(0,a+1):
    a=random.randint(0,10)
    T.append(a)
print(T)

g=T[0]
d=T[10]
m=T[5]
print(g,d,m)
Fusion(T,g,d,m)
# tri_fusion(T,g,d)
print (T)
tri_fusion(T,0,len(T)-1)
print(T)