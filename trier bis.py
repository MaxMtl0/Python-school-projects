a=float(input('Enter a : '))
b=float(input('Enter b : '))
c=float(input('Enter c : '))

if a<b:
    if b<c:
        print(a,'<=',b,'<=',c)
    elif c<b:
         print(a,'<=',c,'<=',b)
    else:
        print(c,'<=',a,'<=',b)
else:
    if a<c:
        print(b,'<=',a,'<=',c)
    elif b<c:
        print(b,'<=',c,'<=',a)
    else:
        print(c,'<=',b,'<=',a)
    
        