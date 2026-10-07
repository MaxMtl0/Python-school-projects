a=int(input('Enter a : '))
test=0
n=1
while (n<a-1):
    n=n+1
    B=a%n
    if B==0:
        test=1
if test==0:
    print (a,'est un nombre premier')
else:
    print (a,'est pas un nombre premeier')
    