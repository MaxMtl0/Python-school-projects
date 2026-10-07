from pylab import*

def f1(x):
    return x
def f2(x):
    return sqrt(x)
def f3(x):
    return x**2
def f4(x):
    return cos(x)
def f5(x):
    return sin(x)


x=arange(1, 10, 0.01)
y1=[];y2=[];y3=[];y4=[];y5=[]
for a in x:
    y1.append(f1(a))
    y2.append(f2(a))
    y3.append(f3(a))
    y4.append(f4(a))
    y5.append(f5(a))
    
plot(x,y1,color='red',linewidth=1)
plot(x,y2,color='g',linewidth=1)
plot(x,y3,color='b',linewidth=1)
plot(x,y4,color='black',linewidth=1)
plot(x,y5,color='pink',linewidth=1)


# axis(0,4, -10,10)
figtext(0.9, 0.05, 'x')
figtext(0.1, 0.95, 'y')
show()
    