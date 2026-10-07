def Miroir(n):
    n=str(n)
    miroir_n=[]
    for i in range(1,len(n)+1):
        miroir_n.append(n[-i])
    return (miroir_n)



n=int(input('entrer un nombre :'))
print(Miroir(n))

        
        

