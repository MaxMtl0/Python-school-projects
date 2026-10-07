from pylab import*
def f(t):
    return (3/2)*arccos(cos(t))-0.6*arccos(cos(2*t))
def g(t):
    return (3/2)*arcsin(sin(t))+18*arcsin(sin(2*t))+arcsin(sin(4*t))

t=arange(0, 10, 0.01)
x=f(t)
y=g(t)
plot(x,y,color='red',linewidth=1)
axis([-1,5, -30,30])
figtext(0.9, 0.05, 'x')
figtext(0.1, 0.95, 'y')
show()