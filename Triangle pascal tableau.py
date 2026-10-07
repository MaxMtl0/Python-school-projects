import numpy as np
A=int(input('entrer nombre de colonnes :'))+1
Colonnes=A
Lignes=A
M=[]
for i in range(0,Lignes):
    L=[]
    for j in range(0,Colonnes):
        a=0
        L.append(a)
    M.append(L)
matrix=np.array(M)
for j in range(0,A):
    matrix[j,0]=1
    for i in range(1,Lignes):
        for j in range(1,Colonnes):
            matrix[i,j]=matrix[i-1,j]+matrix[i-1,j-1]
for i in range(0,Lignes):
    for j in range(0,Colonnes):
        if matrix[i,j]!=0:
            print(matrix[i,j],end=' ')
    print(' ')
