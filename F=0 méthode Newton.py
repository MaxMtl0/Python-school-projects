from math import*
def f(x):
    return log(x)-(1/(1+x**2))
def df(x):
    return 1/x+(2*x)/((1+x**2)**2)
compteur=0
a=1.40
p=0.001
y=a-f(a)/df(a)
while abs(a-y)>p :
    a=y
    y=a-f(a)/df(a)
    compteur+=1

print(a,"nombre d'itération",compteur)