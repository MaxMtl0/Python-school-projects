import random
def code(p,C):                  #code le message
    a=''
    for i in range(len(L)):
        a+=chr(ord(L[i])+ord(C[i%len(C)]))
    print(a)
    return a

def decode(L,C):                #décode le message
    b=''
    for j in range(len(a)):
        b+=chr(ord(a[j])-ord(C[j%len(C)]))
    return b
    
def conversion(n):              #conversion decimal en binaire
    if n > 1:
        conversion(n // 2)
    print(n % 2, end='')
    
#def conversion_bis(n):          #conversion binaire en decimal
    
    
def message_code(a):            #message codé en binaire
    L1=[] 
    c=ord(a[0])
    L1.append(conversion(c))
    return L1
    
def coupe(L1):                        #sépare en blocs de 4 la liste de binaires
    A=[]
    B=[]
    nb=len(L1)//4
    for i in range(nb):
        while len(A)<4:
            c=L1.pop()
            A.append(c)
        B.append(A)
    print(B)
    
def bruit(L1):                  #pas fini
    for i in range(len(L1)):
        e=random.randint(1,len(L1))
        
def hamming(v):
    Nb_lignes=3
    Nb_colonnes=7                                        #création matrice 
    M=[]                                                 
    for i in range(Nb_colonnes):
        N=[]
        for j in range(Nb_lignes):
            a=0
            L.append(a)
        M.append(L)
    matrice=np.array(M) 
        
    
L=input('entrer phrase :')       #message
C='clef'                         #clef de code vigenere 
a=code(L,C)
# print(decode(a,C))


message_code(a)       
coupe(message_code(a))           