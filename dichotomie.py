#Dichotomie
from pylab import*
from math import*
p=float(input('entrer la précision:'))
a=float(input('entrer a: '))
b=float(input('entrer b: '))
def fonction(x):
    x=log(x)-(1/(1+x**2))
    return (x)
d=abs(a-b)      #valeur absolue
c=(a+b)/2
cpt=0
while d>p:
    cpt+=1
    c=(a+b)/2
    if fonction(c)*fonction(a)>0:
        a=c
        d=abs(a-b)
    else:
        b=c
        d=abs(a-b)
print('x= :',c)
print('nb d iteration :',cpt)