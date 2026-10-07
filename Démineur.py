import numpy as np
import random
import os
import time

def bombes_aléatoires(matrice):                      #placement des bombes
    k=0
    while k<Nb_colonnes-2:
        x=random.randint(1,Nb_colonnes-2)
        y=random.randint(1,Nb_colonnes-2)
        if matrice[x,y]==0:
            matrice[x,y]=9
            k+=1
            
def autres_cases(matrice):                           #cases autour des bombes
    for i in range(1,Nb_colonnes-1):
        for j in range(1,Nb_colonnes-1):
            numéro=0
            if matrice[i,j]!=9:
                for k in range(-1,2):
                    for p in range(-1,2):
                        if matrice[i+k,j+p]==9:
                            numéro+=1
                matrice[i,j]=numéro        

def register(demineur,matrice):                                      #enregistrer la partie
    f = open("partie_en_cours.txt","w")
#     f.write(" ")
#     f.close()
    for i in range (Nomb_lignes):
        for j in range(Nomb_colonnes):
            b=str(demineur[i,j])
            l2.append(b)
    f.writelines(l2)
    f.write(',')
    Ly=["joueur :",pseudo]
    f.writelines(Ly)
    f.write(',')
    for i in range (Nb_lignes):
        for j in range(Nb_colonnes):
            a=str(matrice[i,j])
            l1.append(a)
    f.writelines(l1)
    f.close
    
    
    
    
def jeu(demineur,matrice):                              #actions du joueur
    compteur=0
    for r in range(1,Nb_colonnes-1):
            for s in range(1,Nb_colonnes-1):
                if matrice[r,s]==9 and demineur[r,s]=='F':
                    compteur+=1                         #compteur de drapeau/bombe
    if compteur==Nb_colonnes-2:                        
        print('Gagné!')                                 #Gagné
        print(matrice)
        print("Score de",pseudo," :", time.clock() - begin,"secondes.") #score
    else :
        c=int(input('entrer la ligne de la case :'))    #(-1)pour commencer les lignes à 1 et non 0
        l=int(input('entrer la colonne de la case :'))      #idem pour les colonnes
        n=int(input('cliquer=0 drapeau=1 annul_drapeau=2 endgame=3 :'))              #cliquer, drapeau ou fin de partie
        if n==1:                 #drapeau
            demineur[c,l]='F' 
            print(demineur)                       
            jeu(demineur,matrice)
        else:
            if n==2:             #retirer drapeau
                if demineur[c,l]=='F':
                    demineur[c,l]='^'
                    print(demineur)                       
                    jeu(demineur,matrice)
                else:
                    print(demineur)  
                    print('case sans drapeau')                     
                    jeu(demineur,matrice)
            if n==0:             #cliquer
                if matrice[c,l]!=9:                 # pas perdu
                    demineur[c,l]=matrice[c,l]  
                    print(demineur)
                    jeu(demineur,matrice)
                else:                               # perdu
                    print(matrice)
                    autres_cases(matrice)
                    print("Score de",pseudo," :", time.clock() - begin,"secondes.")     
                    print('Perdu')
            if n==3:            #fin de partie
                print(demineur)
                print("Score de",pseudo," :", time.clock() - begin,"secondes.")    #enregistrer la partie
                Reg=int(input('enregistrer la partie oui=0 non=1 :'))
                if Reg==1:
                    print(matrice)
                    autres_cases(matrice)
                    print("Score de",pseudo," :", time.clock() - begin,"secondes.")     
                    print('Try again')
                else:
                    register(demineur,matrice)
                    print('Partie enregistrée')
            if n==74:           #EasterEgg
                mdp=input('entrer password:')
                if mdp=='ColocGang':
                    print(matrice)
                    print('Gagné Bg,100 pompes stp')   
                    print("Score de",pseudo," :", time.clock() - begin,"secondes.")           
                elif mdp=='azerty':
                    print(demineur)
                    print('Tu me prends pour qui?')
                    jeu(demineur,matrice)
                elif mdp=='1234':
                    print(demineur)
                    print("C'est pas aussi simple!")
                    jeu(demineur,matrice)
    

                    
os.chdir("C:/Users/Max/Documents/pyzo/démineur")                    #register
repcourrant = os.getcwd()
l1=[]
l2=[]
print("Bienvenue: vous allez jouer au démineur, le but est de trouver toutes les bombes en fonction des chiffres qui les entourent et d'y mettre un drapeau. Si c'est votre première partie merci de ne pas reprendre la partie en cours. ")

Play=int(input('reprendre la partie en cours oui=0 non=1 :'))       #reprendre une partie enregistrée
if Play==0:
    f=open('partie_en_cours.txt','r')
    partie=f.read()
    l=partie.split(',')
    print(l)
#     banane=f.read(l[1])
    L0=[]
    L2=[]
#     print(banane)
    for i in range (Nb_colonnes):
        for j in range(Nb_colonnes):
            L0.append(l[0][i+j])
    demineur=np.array(L0)
    
    for i in range (Nb_colonnes):
        for j in range(Nb_colonnes):
            L2.append(l[2][i+j])
    matrice=np.array(L2)
    
    f.close
    jeu(demineur,matrice)
else:
    pseudo=input('entrer votre pseudo:')                            #pseudo
    Niveau_souhaité=input('niveau ;facile,moyen,difficile: ')       #création niveau
    facile=3+2
    moyen=12+2
    difficile=15+2  
    test=['facile','moyen','difficile']
    while Niveau_souhaité not in test:                              #erreur d'entrée de niveau
        print('ERROR SYNTAXE')
        Niveau_souhaité=input('niveau ;facile,moyen,difficile: ')
    
    if Niveau_souhaité=='facile':                                   #nom du niveau + temps enregistré
        Nb_colonnes= facile
        begin = time.clock()
    elif Niveau_souhaité=='moyen':                                    
        Nb_colonnes=moyen
        begin = time.clock()
    else:
        Nb_colonnes=difficile 
        begin = time.clock()  
        
    Nb_lignes=Nb_colonnes                                           #création matrice programme
    M=[]                                                 
    for i in range(Nb_colonnes):
        L=[]
        for j in range(Nb_lignes):
            a=0
            L.append(a)
        M.append(L)
    matrice=np.array(M)                                   
    bombes_aléatoires(matrice)
    autres_cases(matrice)
    #print(matrice)                                      #pour voir la matrice programme retirer le '#' en début de ligne
    
    Nomb_colonnes=Nb_colonnes                             #matrice affichée                                      
    Nomb_lignes=Nb_lignes
    N=[]                                                 
    for i in range(Nomb_colonnes):
        L1=[]
        for j in range(Nomb_lignes):
            b='O'                                         #design de la matrice affichée
            L1.append(b)
        N.append(L1)
    demineur=np.array(N)  
    print(demineur)
    jeu(demineur,matrice)                                 #commencer la partie

