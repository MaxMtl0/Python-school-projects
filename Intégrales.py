from math import*
from pylab import*
def f1(x):   #entrer la fonction
    return exp(-x**2)
    
def Rect(SD,SG,a,c,f1):
    xi=0
    for i in range(n):
        xi=a+c
        SG=SG+f1(xi)
    for i in range(n+1):
        xi=a*c
        SD=SD+f1(xi)
    return SD and SG
    
def f(x):
    return x-log(x)
    
def int_rectangleG(f,a,b,n):
    assert a<b and 0<n
    h=(b-a)/n
    s=0
    for k in range (n):
        s+=f(a+k*h)
    return h*s
    
def int_rectangleD(f,a,b,n):
    assert a<b and 0<n
    h=(b-a)/n
    s=0
    for k in range (1,n+1):
        s+=f(a+k*h)
    return h*s

def int_rectanglemedian(f,a,b,n):
    assert a<b and 0<n
    h=(b-a)/n
    s=0
    for k in range (1,n+1):
        s+=f(a+(k-0.5)*h)
    return h*s

def int_trapeze(f,a,b,n):
    assert a<b and 0<n
    h=(b-a)/n
    s=(f(a)+f(b))/2
    for k in range (1,n):
        s+=f(a+k*h)
    return h*s
    
def int_simpson(f,a,b,n):
    return (int_trapeze(f,a,b,n)+2*int_rectanglemedian(f,a,b,n)/3
    
SG=0
SD=0
n=2
a=int(input('entrer la valeur de a:'))
b=int(input('entrer la valeur de b:'))
p=float(input('entrer la valeur de p:'))

c=(b-a)/n
Rect(SD,SG,a,c,f1)
while SG-SD<p:
    n+=1
    Rect(SD,SG,a,c)
print((SD-SG)/2)
