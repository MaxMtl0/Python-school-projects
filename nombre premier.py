a=int(input('Enter a : '))
test=0
for n in range(2,a):
    A=a%n
    if A==0:
        test=1
if test==0:
    print(a,'est un nombre premier')
else:
    print(a,'est pas un nombre premier')
    
        