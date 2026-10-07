#Lagrange
from pylab import*
from math import*
p=float(input('entrer la précision: '))
a=1.40
b=1.45
def fonction(x):
    x=log(x)-(1/(1+x**2))
    return(x)
cpt=0
c=(b*fonction(a)-a*fonction(b))/(fonction(a)-fonction(b))
d=abs(a-b)                                                  #valeur absolue
while d>p:
    c=(b*fonction(a)-a*fonction(b))/(fonction(a)-fonction(b))
    e=fonction(a)*fonction(c)
    if e>0:
        a=c
    else :
        b=c
    d=abs(a-b)
    cpt+=1
f=(b+a)/2
print(f,"nombre compteur",cpt)