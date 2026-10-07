import random

def Echange(T,c,b):
    A=T[c]
    T[c]=T[b]
    T[b]=A

def Segmente(T,i,j):
    g=i+1
    d=j
    p=T[i]
    while g<=d:
        while d>=0 and T[d]>p:
            d=d-1
        while g<=j and T[g]<=p:
            g=g+1
        if g<d:
            Echange(T,g,d)
            d=d-1
            g=g+1
    k=d
    Echange(T,i,d)
    return k

def tri_rapide(T,i,j):
    if i<j:
        k=Segmente(T,i,j)
        tri_rapide(T,i,k-1)
        tri_rapide(T,k+1,j)
        
        
        
        
# def tri_opti(T,i,j):
#     if i<j:
#         k=Segmente(T,i,j)
#         if k-i>15:
#             
#création liste
T=[]        
a=10
for i in range(0,a+1):
    a=random.randint(0,10)
    T.append(a)

print (T)
tri_rapide(T,0,len(T)-1)
print(T)