from math import*
def binome_newton():
    a=fact(n)
    b=fact(k)*fact(n-k)
    a=a/b
    print(a)
        
def fact():
    P=1
    for i in range (1,n+1):
        P=P*i
        
n=int(input('entrez n:'))
for k in range(n):
    binome_newton()
    
# correction
# def coef(n,k):
#     if n==k or k==0:
#         return 1
#     else:
#         return coef(n-1,k-1)+coef(n-1,k)