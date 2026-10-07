from math import *
a=float(input('Enter a : '))
b=float(input('Enter b : '))
c=float(input('Enter c : '))
# print(a,b,c)
if a==0:
    if b==0:
        if c==0:
            print('Tout réel est solution')
        else:
            print('Pas de solution')
    else:
        x=-c/b
        print('Une solution :',x)
else:
    Delta=b**2-4*a*c
    if Delta>0:
        x1=(-b-sqrt(Delta))/(2*a)
        x2=(-b+sqrt(Delta))/(2*a)
        print('Deux solutions :',x1,' et ',x2)
    if Delta==0:
        x=-b/(2*a)
        print('Une solution :',x)
    if Delta<0:
        print('Pas de solution')
        