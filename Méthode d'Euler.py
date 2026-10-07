from math import*
from pylab import*
def Yexact(x):
    return -(1/2)*x-(3/4)+(7/4)*exp(2*x)
def Yeuler(x):
    return -(1/2)+(7/2)*exp(2*a)*(x-a)+(-(1/2)*a-(3/4)+(7/4)*exp(2*a))

x=0
for i in range (1,4):
    x+=0.1
    Yeuler(x)

x=arange(0, 3, 0.1)
y1=[];y2=[]
for a in x:
    y1.append(Yexact(a))
    y2.append(Yeuler(a))
plot(x,y1,color='red',linewidth=1)
plot(x,y2,color='blue',linewidth=1)
axis([0,3, 0,700]) 
figtext(0.9, 0.05, 'x')
figtext(0.1, 0.95, 'y')
show()
