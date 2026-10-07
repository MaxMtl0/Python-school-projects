hauteur=int(input('Combien de lignes : '))
nbr_etoiles=1
nbr_espace=hauteur-1
for i in range(hauteur):
    print(nbr_espace*" ",nbr_etoiles*"*")#n*"ph" ecrit phphphph n fois
    nbr_etoiles+=2  #ou nbr etoile= nombre etoiles+2
    nbr_espace-=1   #ou nbr espace= nombre espace -1