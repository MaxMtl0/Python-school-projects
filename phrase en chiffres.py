Ph=input("entrer une phrase sans majuscule ni ponctuation :")
liste2=[]
for i in range (len(Ph)):
    a=Ph[i]
    if ord(a)-96!=-64:
        liste2.append(ord(a)-96)
    else:
        liste2.append(0)
print(liste2)

alpha=' abcdefghijklmnopqrstuvwxyz'
decode=''
for i in range (len(liste2)):
    decode=decode+alpha[liste2[i]]
print (decode)














