def code(L,C):
    a=''
    for i in range(len(L)):
        a+=chr(ord(L[i])+ord(C[i%len(C)]))
    print(a)
    return a

def decode(L,C):
    b=''
    for j in range(len(a)):
        b+=chr(ord(a[j])-ord(C[j%len(C)]))
    return b
    
L='barycentre'               #phrase
C='clef'        #clef
a=code(L,C)
print(decode(a,C))


