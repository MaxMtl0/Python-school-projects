from math import*
def Liste(L):
    a=int(input('si vous voulez entrer un chiffre entrez 0 sinon 1:'))
    if a==0:
        b=int(input("entrer un chiffre :"))
        L.append(b)
        Liste(L)
    else:
        print(L)
        palindrome(L)
        
def palindrome(L):
    if len(L)<=1:
        print('true')
    if L[0]==L[-1]:
        L.pop(L[0])
        L.pop(L[-1])
        palindrome(L)
    else:
        print ('False')
    
L=[]
Liste(L)

# correction
# def pal(L):
#     if len(L)<2:
#         return true
#     if L[0]==L[-1]:
#         L.pop(0)
#         L.pop(-1)
#         return pal(L)
#     else:
#         return False

