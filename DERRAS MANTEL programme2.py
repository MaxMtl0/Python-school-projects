import sqlite3

conn =sqlite3.connect("C:/Users/Max/Documents/pyzo/sujets si.sq3")
cur =conn.cursor()
                                                                        ##Procédures##
def recherche1(Z): #recherche si abonné
    def correction_kholle(Z): #fonction dans une autre pour garder la valeur Z(classepT/PTSI) sans utiliser de classe
        Z1=int(input('souhaitez-vous la correction? oui 0 non 1:'))
        if Z1==1:
            recherche1(Z)
        elif Z1==0:
            if Z=='PT': #correction en fonction de la classe de l'utilisateur
                cur.execute("SELECT correction_PT FROM Kholle1")
                L=list(cur)
                L=L[0][0]  #pour supprimerles crochets et virgules
                print(L)   
                recherche1(Z)
            elif Z=='PTSI':
                cur.execute("SELECT correction_PTSI FROM Kholle1")
                L=list(cur)
                L=L[0][0]
                print(L)
                recherche1(Z)
        else:
            print("nous n'avons pas compris votre demande")
            correction_kholle(Z)
            
            
    def correction_td(Z):
        Z1=int(input('souhaitez-vous la correction? oui 0 non 1:'))
        if Z1==1:
            recherche1(Z)
        elif Z1==0:
            if Z=='PT':
                cur.execute("SELECT correction_PT FROM Td1")
                L=list(cur)
                L=L[0][0]
                print(L)
                recherche1(Z)
            elif Z=='PTSI':
                cur.execute("SELECT correction_PTSI FROM Td1")
                L=list(cur)
                L=L[0][0]
                print(L)
                recherche1(Z)
        else:
            print("nous n'avons pas compris votre demande")
            correction_td(Z)
                
    def correction_cc(Z):
        Z1=int(input('souhaitez-vous la correction? oui 0 non 1:'))
        if Z1==1:
            recherche1(Z)
        elif Z1==0:
            if Z=='PT':
                cur.execute("SELECT correction_PT FROM Cc1")
                L=list(cur)
                L=L[0][0]
                print(L)
                recherche1(Z)
            elif Z=='PTSI':
                cur.execute("SELECT correction_PTSI FROM Cc1")
                L=list(cur)
                L=L[0][0]
                print(L)
                recherche1(Z)
        else:
            print("nous n'avons pas compris votre demande")
            correction_cc(Z)

    def correction_cb(Z):
        Z1=int(input('souhaitez-vous la correction? oui 0 non 1:'))
        if Z1==1:
            recherche1(Z)
        elif Z1==0:
            if Z=='PT':
                cur.execute("SELECT correction_PT FROM Cb1")
                L=list(cur)
                L=L[0][0]
                print(L)
                recherche1(Z)
            elif Z=='PTSI':
                cur.execute("SELECT correction_PTSI FROM Cb1")
                L=list(cur)
                L=L[0][0]
                print(L)
                recherche1(Z)
        else:
            print("nous n'avons pas compris votre demande")
            correction_cb(Z)
                
    def correction_tp(Z):
        Z1=int(input('souhaitez-vous la correction? oui 0 non 1:'))
        if Z1==1:
            recherche1(Z)
        elif Z1==0:
            if Z=='PT':
                cur.execute("SELECT correction_PT FROM Tp1")
                L=list(cur)
                L=L[0][0]
                print(L)
                recherche1(Z)
            elif Z=='PTSI':
                cur.execute("SELECT correction_PTSI FROM Tp1")
                L=list(cur)
                L=L[0][0]
                print(L)
                recherche1(Z)
        else:
            print("nous n'avons pas compris votre demande")
            correction_tp(Z)

    def correction_es(Z):
        Z1=int(input('souhaitez-vous la correction? oui 0 non 1:'))
        if Z1==1:
            recherche1(Z)
        elif Z1==0:
            if Z=='PT':
                cur.execute("SELECT correction_PT FROM Es1")
                L=list(cur)
                L=L[0][0]
                print(L)
                recherche1(Z)
            elif Z=='PTSI':
                cur.execute("SELECT correction_PTSI FROM Es1")
                L=list(cur)
                L=L[0][0]
                print(L)
                recherche1(Z)
        else:
            print("nous n'avons pas compris votre demande")
            correction_td(Z)
                                                                #début procédure recherche1
    D=input('Sur quel sujet souhaitez-vous vous entrainer; kholle, td, cc, es, cb, tp, arret:')
    if D=='kholle':
        if Z=='PT':
            cur.execute("SELECT sujet_PT FROM kholle")
            L=list(cur)
            L=L[0][0]
            print(L)
            correction_kholle(Z)
        elif Z=='PTSI':
            cur.execute("SELECT sujet_PTSI FROM kholle")
            L=list(cur)
            L=L[0][0]
            print(L)
            correction_kholle(Z)
        else:
            print("Nous n'avons pas compris dans quelle classe vous êtes") 
            recherche1(Z)
    elif D=='td':
        if Z=='PT':
            cur.execute("SELECT sujet_PT FROM td")
            L=list(cur)
            L=L[0][0]
            print(L)
            correction_td(Z)
        elif Z=='PTSI':
            cur.execute("SELECT sujet_PTSI FROM td")
            L=list(cur)
            L=L[0][0]
            print(L)
            correction_td(Z)
        else:
            print("Nous n'avons pas compris dans quelle classe vous êtes") 
            recherche1(Z)
    elif D=='cc':
        if Z=='PT':
            cur.execute("SELECT sujet_PT FROM cc")
            L=list(cur)
            L=L[0][0]
            print(L)
            correction_cc(Z)
        elif Z=='PTSI':
            cur.execute("SELECT sujet_PTSI FROM cc")
            L=list(cur)
            L=L[0][0]
            print(L)
            correction_cc(Z)
        else:
            print("Nous n'avons pas compris dans quelle classe vous êtes") 
            recherche1(Z)
    elif D=='es':
        if Z=='PT':
            cur.execute("SELECT sujet_PT FROM es")
            L=list(cur)
            L=L[0][0]
            print(L)
            correction_es(Z)
        elif Z=='PTSI':
            cur.execute("SELECT sujet_PTSI FROM es")
            L=list(cur)
            L=L[0][0]
            print(L)
            correction_es(Z)
        else:
            print("Nous n'avons pas compris dans quelle classe vous êtes") 
            recherche1(Z)
    elif D=='cb':
        if Z=='PT':
            cur.execute("SELECT sujet_PT FROM cb")
            L=list(cur)
            L=L[0][0]
            print(L)
            correction_cb(Z)
        elif Z=='PTSI':
            cur.execute("SELECT sujet_PTSI FROM cb")
            L=list(cur)
            L=L[0][0]
            print(L)
            correction_cb(Z)
        else:
            print("Nous n'avons pas compris dans quelle classe vous êtes") 
            recherche1(Z)
    elif D=='tp':
        if Z=='PT':
            cur.execute("SELECT sujet_PT FROM tp")
            L=list(cur)
            L=L[0][0]
            print(L)
            correction_tp(Z)
        elif Z=='PTSI':
            cur.execute("SELECT sujet_PTSI FROM tp")
            L=list(cur)
            L=L[0][0]
            print(L)
            correction_tp(Z)
        else:
            print("Nous n'avons pas compris dans quelle classe vous êtes") 
            recherche1(Z)
    elif D=='arret':
        arret()
    elif D=='25':
        admin()
    else:
        print("nous n'avons pas compris votre demande")
        recherche1(Z)

def recherche(): #recherche si non abonné
    A=input("vous souhaitez accéder à des sujets de quel niveau? PTSI ou PT :") 
    D=input('Sur quel sujet souhaitez-vous vous entrainer; kholle, td, cc, es, cb, tp, arret:')
    if D=='kholle':
        if A=='PT':
            cur.execute("SELECT sujet_PT FROM kholle")
            L=list(cur)
            L=L[0][0]
            print(L)
            print('souhaitez-vous la correction? si oui il faut vous abonner')
            Begin1()
        elif A=='PTSI':
            cur.execute("SELECT sujet_PTSI FROM kholle")
            L=list(cur)
            L=L[0][0]
            print(L)
            print('souhaitez-vous la correction? si oui il faut vous abonner')
            Begin1()
        else:
            print("Nous n'avons pas compris dans quelle classe vous êtes") 
            recherche()
            
    elif D=='td':
        if A=='PT':
            cur.execute("SELECT sujet_PT FROM td")
            L=list(cur)
            L=L[0][0]
            print(L)
            print('souhaitez-vous la correction? si oui il faut vous abonner')
            Begin1()
        elif A=='PTSI':
            cur.execute("SELECT sujet_PTSI FROM td")
            L=list(cur)
            L=L[0][0]
            print(L)
            print('souhaitez-vous la correction? si oui il faut vous abonner')
            Begin1()
        else:
            print("Nous n'avons pas compris dans quelle classe vous êtes") 
            recherche()
    elif D=='cc':
        if A=='PT':
            cur.execute("SELECT sujet_PT FROM cc")
            L=list(cur)
            L=L[0][0]
            print(L)
            print('souhaitez-vous la correction? si oui il faut vous abonner')
            Begin1()
        elif A=='PTSI':
            cur.execute("SELECT sujet_PTSI FROM cc")
            L=list(cur)
            L=L[0][0]
            print(L)
            print('souhaitez-vous la correction? si oui il faut vous abonner')
            Begin1()
        else:
            print("Nous n'avons pas compris dans quelle classe vous êtes") 
            recherche()
    elif D=='es':
        if A=='PT':
            cur.execute("SELECT sujet_PT FROM es")
            L=list(cur)
            L=L[0][0]
            print(L)
            print('souhaitez-vous la correction? si oui il faut vous abonner')
            Begin1()
        elif A=='PTSI':
            cur.execute("SELECT sujet_PTSI FROM es")
            L=list(cur)
            L=L[0][0]
            print(L)
            print('souhaitez-vous la correction? si oui il faut vous abonner')
            Begin1()
        else:
            print("Nous n'avons pas compris dans quelle classe vous êtes") 
            recherche()
    elif D=='cb':
        if A=='PT':
            cur.execute("SELECT sujet_PT FROM cb")
            L=list(cur)
            L=L[0][0]
            print(L)
            print('souhaitez-vous la correction? si oui il faut vous abonner')
            Begin1()
        elif A=='PTSI':
            cur.execute("SELECT sujet_PTSI FROM cb")
            L=list(cur)
            L=L[0][0]
            print(L)
            print('souhaitez-vous la correction? si oui il faut vous abonner')
            Begin1()
        else:
            print("Nous n'avons pas compris dans quelle classe vous êtes") 
            recherche()
    elif D=='tp':
        if A=='PT':
            cur.execute("SELECT sujet_PT FROM tp")
            L=list(cur)
            L=L[0][0]
            print(L)
            print('souhaitez-vous la correction? si oui il faut vous abonner')
            Begin1()
        elif A=='PTSI':
            cur.execute("SELECT sujet_PTSI FROM tp")
            L=list(cur)
            L=L[0][0]
            print(L)
            print('souhaitez-vous la correction? si oui il faut vous abonner')
            Begin1()
        else:
            print("Nous n'avons pas compris dans quelle classe vous êtes") 
            recherche()
    elif D=='arret':
        arret()
    elif D=='25':
        admin()
    else:
        print("nous n'avons pas compris votre demande de sujet")
        recherche()
        
def abonnement(): #abonnement de l'utilisateur
    C=input('quel est votre nom?:')
    F=input('quel est votre prénom?:') 
    E=input('quel est votre âge?:')
    G=input('En quel classe êtes vous PT/PTSI?:')
    H=input('entrez un mot de passe:')
    cur.execute("INSERT INTO membres(age,nom,prenom,classe,mdp) VALUES('"+E+"','"+C+"','"+F+"','"+G+"','"+H+"')")
    conn.commit() #on enregistre les données
    cur.execute("SELECT '"+F+"' FROM membres")
    L=list(cur)
    L=L[0][0]
    print(L)
    print('Vous êtes abonné!!')
    recherche1(G)
    
def Begin1(): #demande si l'utilisateur veut s'abonner
    B=int(input('souhaitez-vous vous abonner? oui 0; non 1 :'))
    if B==1:
        recherche()
    elif B==0:
        abonnement()
    else:
        Begin1()

def Begin(): #lance le programme
    A=int(input('êtes vous abonnés? oui 0; non 1 :'))
    if A==1:
        Begin1()
    elif A==0:
        verif() 
    elif A==25:
        admin()
    else:
        Begin()
        
def admin(): #pour accéder aux droits d'admin il faut avoir accès au code '25'
    print('vous êtes administrateur') #pour sortir du mode admin il faut faire arret() l407 puis relancer
    S=input('à quelle table voulez-vous accéder?:')
    if S=='cb':
        cur.execute("SELECT * FROM cb")
        L=list(cur)
        L=L[0]
        print('sujets PT/PTSI',L)
        cur.execute("SELECT * FROM Cb1")
        L=list(cur)
        L=L[0]
        print('correction PT/PTSI',L) #on présente tout pour voir ce qu'il y a à modifier
        G=int(input("souaitez-vous la modifier oui 0 non 1:"))
        if G==1:
            admin()
        else: 
            G1=int(input("Que souaitez-vous modifier sujet PT 0/sujet PTSI 1/ correction PT 2/correction PTSI 3/ tout supprimer 4/arreter le programme 5:"))
            if G1==0:
                G3=input("entrez l'ancien sujet:")
                G2=input('entrez le nouveau sujet:')#pour supprimer le sujet que d'une classe(ex:PT) il faut update et rien mettre dans le nouveau sujet 
                cur.execute("UPDATE cb SET sujet_PT = '"+G2+"' WHERE sujet_PT='"+G3+"' ")
                cur.execute("SELECT sujet_PT FROM cb")
                L=list(cur)
                L=L[0][0]
                print('nouveau sujet',L)
                conn.commit()
                admin()
            elif G1==1:
                G3=input("entrez l'ancien sujet:")
                G2=input('entrez le nouveau sujet:')
                cur.execute("UPDATE cb SET sujet_PTSI = '"+G2+"' WHERE sujet_PTSI='"+G3+"' ")
                cur.execute("SELECT sujet_PTSI FROM cb")
                L=list(cur)
                L=L[0][0]
                print('nouveau sujet',L)
                conn.commit()
                admin()
            elif G1==2:
                G3=input("entrez l'ancienne correction:")
                G2=input('entrez la nouvelle correction:')
                cur.execute("UPDATE Cb1 SET correction_PT = '"+G2+"' WHERE correction_PT='"+G3+"'")
                cur.execute("SELECT correction_PT FROM Cb1")
                L=list(cur)
                L=L[0][0]
                print('nouvelle correction',L)
                conn.commit()
                admin()
            elif G1==3:
                G3=input("entrez l'ancienne correction:")
                G2=input('entrez la nouvelle correction:')
                cur.execute("UPDATE Cb1 SET correction_PTSI = '"+G2+"' WHERE correction_PTSI='"+G3+"'")
                cur.execute("SELECT correction_PTSI FROM Cb1")
                L=list(cur)
                L=L[0][0]
                print('nouvelle correction',L)
                conn.commit()
                admin()
            elif G1==4: #ici on supprime toute la partie séléctionnée (cb) les deux classes comprises(PT/PTSI) 
                cur.execute("DELETE FROM cb ")
                cur.execute("SELECT * FROM cb")
                L=list(cur)
                L=L[0]
                print('sujets',L)
                cur.execute("DELETE FROM Cb1 ")
                cur.execute("SELECT * FROM Cb1")
                L=list(cur)
                L=L[0]
                print('corrections',L)
                conn.commit()
                admin()
            elif G1==5:
                arret()
            else:
                print("nous n'avons pas compris votre demande")
                admin()
    elif S=='tp':
        cur.execute("SELECT * FROM tp")
        L=list(cur)
        L=L[0]
        print('sujets PT/PTSI',L)
        cur.execute("SELECT * FROM Tp1")
        L=list(cur)
        L=L[0]
        print('correction PT/PTSI',L)
        G=int(input("souaitez-vous la modifier oui 0 non 1:"))
        if G==1:
            admin()
        else:
            G1=int(input("Que souaitez-vous modifier sujet PT 0/sujet PTSI 1/ correction PT 2/correction PTSI 3/ tout supprimer 4/arreter le programme 5:"))
            if G1==0:
                G3=input("entrez l'ancien sujet:")
                G2=input('entrez le nouveau sujet:')
                cur.execute("UPDATE tp SET sujet_PT = '"+G2+"' WHERE sujet_PT='"+G3+"' ")
                cur.execute("SELECT sujet_PT FROM tp")
                L=list(cur)
                L=L[0][0]
                print('nouveau sujet',L)
                conn.commit()
                admin()
            elif G1==1:
                G3=input("entrez l'ancien sujet:")
                G2=input('entrez le nouveau sujet:')
                cur.execute("UPDATE tp SET sujet_PTSI = '"+G2+"' WHERE sujet_PTSI='"+G3+"' ")
                cur.execute("SELECT sujet_PTSI FROM tp")
                L=list(cur)
                L=L[0][0]
                print('nouveau sujet',L)
                conn.commit()
                admin()
            elif G1==2:
                G3=input("entrez l'ancienne correction:")
                G2=input('entrez la nouvelle correction:')
                cur.execute("UPDATE Tp1 SET correction_PT = '"+G2+"' WHERE correction_PT='"+G3+"'")
                cur.execute("SELECT correction_PT FROM Tp1")
                L=list(cur)
                L=L[0][0]
                print('nouvelle correction',L)
                conn.commit()
                admin()
            elif G1==3:
                G3=input("entrez l'ancienne correction:")
                G2=input('entrez la nouvelle correction:')
                cur.execute("UPDATE Tp1 SET correction_PTSI = '"+G2+"' WHERE correction_PTSI='"+G3+"'")
                cur.execute("SELECT correction_PTSI FROM Tp1")
                L=list(cur)
                L=L[0][0]
                print('nouvelle correction',L)
                conn.commit()
                admin()
            elif G1==4:
                cur.execute("DELETE FROM tp ")
                cur.execute("SELECT * FROM tp")
                L=list(cur)
                L=L[0]
                print('sujets',L)
                cur.execute("DELETE FROM Tp1 ")
                cur.execute("SELECT * FROM Tp1")
                L=list(cur)
                L=L[0]
                print('corrections',L)
                conn.commit()
                admin()
            elif G1==5:
                arret()
            else:
                print("nous n'avons pas compris votre demande")
                admin()
        
    elif S=='cc':
        cur.execute("SELECT * FROM cc")
        L=list(cur)
        L=L[0]
        print('sujets PT/PTSI',L)
        cur.execute("SELECT * FROM Cc1")
        L=list(cur)
        L=L[0]
        print('correction PT/PTSI',L)
        G=int(input("souaitez-vous la modifier oui 0 non 1:"))
        if G==1:
            admin()
        else:
            G1=int(input("Que souaitez-vous modifier sujet PT 0/sujet PTSI 1/ correction PT 2/correction PTSI 3/ tout supprimer 4/arreter le programme 5:"))
            if G1==0:
                G3=input("entrez l'ancien sujet:")
                G2=input('entrez le nouveau sujet:')
                cur.execute("UPDATE cc SET sujet_PT = '"+G2+"' WHERE sujet_PT='"+G3+"' ")
                cur.execute("SELECT sujet_PT FROM cc")
                L=list(cur)
                L=L[0][0]
                print('nouveau sujet',L)
                conn.commit()
                admin()
            elif G1==1:
                G3=input("entrez l'ancien sujet:")
                G2=input('entrez le nouveau sujet:')
                cur.execute("UPDATE cc SET sujet_PTSI = '"+G2+"' WHERE sujet_PTSI='"+G3+"' ")
                cur.execute("SELECT sujet_PTSI FROM cc")
                L=list(cur)
                L=L[0][0]
                print('nouveau sujet',L)
                conn.commit()
                admin()
            elif G1==2:
                G3=input("entrez l'ancienne correction:")
                G2=input('entrez la nouvelle correction:')
                cur.execute("UPDATE Cc1 SET correction_PT = '"+G2+"' WHERE correction_PT='"+G3+"'")
                cur.execute("SELECT correction_PT FROM Cc1")
                L=list(cur)
                L=L[0][0]
                print('nouvelle correction',L)
                conn.commit()
                admin()
            elif G1==3:
                G3=input("entrez l'ancienne correction:")
                G2=input('entrez la nouvelle correction:')
                cur.execute("UPDATE Cc1 SET correction_PTSI = '"+G2+"' WHERE correction_PTSI='"+G3+"'")
                cur.execute("SELECT correction_PTSI FROM Cc1")
                L=list(cur)
                L=L[0][0]
                print('nouvelle correction',L)
                conn.commit()
                admin()
            elif G1==4:
                cur.execute("DELETE FROM cc ")
                cur.execute("SELECT * FROM cc")
                L=list(cur)
                L=L[0]
                print('sujets',L)
                cur.execute("DELETE FROM Cc1 ")
                cur.execute("SELECT * FROM Cc1")
                L=list(cur)
                L=L[0]
                print('corrections',L)
                conn.commit()
                admin()
            elif G1==5:
                arret()
            else:
                print("nous n'avons pas compris votre demande")
                admin()
        
    elif S=='td':
        cur.execute("SELECT * FROM td")
        L=list(cur)
        L=L[0]
        print('sujets PT/PTSI',L)
        cur.execute("SELECT * FROM Td1")
        L=list(cur)
        L=L[0]
        print('correction PT/PTSI',L)
        G=int(input("souaitez-vous la modifier oui 0 non 1:"))
        if G==1:
            admin()
        else:
            G1=int(input("Que souaitez-vous modifier sujet PT 0/sujet PTSI 1/ correction PT 2/correction PTSI 3/ tout supprimer 4/arreter le programme 5:"))
            if G1==0:
                G3=input("entrez l'ancien sujet:")
                G2=input('entrez le nouveau sujet:')
                cur.execute("UPDATE td SET sujet_PT = '"+G2+"' WHERE sujet_PT='"+G3+"' ")
                cur.execute("SELECT sujet_PT FROM td")
                L=list(cur)
                L=L[0][0]
                print('nouveau sujet',L)
                conn.commit()
                admin()
            elif G1==1:
                G3=input("entrez l'ancien sujet:")
                G2=input('entrez le nouveau sujet:')
                cur.execute("UPDATE td SET sujet_PTSI = '"+G2+"' WHERE sujet_PTSI='"+G3+"' ")
                cur.execute("SELECT sujet_PTSI FROM td")
                L=list(cur)
                L=L[0][0]
                print('nouveau sujet',L)
                conn.commit()
                admin()
            elif G1==2:
                G3=input("entrez l'ancienne correction:")
                G2=input('entrez la nouvelle correction:')
                cur.execute("UPDATE Td1 SET correction_PT = '"+G2+"' WHERE correction_PT='"+G3+"'")
                cur.execute("SELECT correction_PT FROM Td1")
                L=list(cur)
                L=L[0][0]
                print('nouvelle correction',L)
                conn.commit()
                admin()
            elif G1==3:
                G3=input("entrez l'ancienne correction:")
                G2=input('entrez la nouvelle correction:')
                cur.execute("UPDATE Td1 SET correction_PTSI = '"+G2+"' WHERE correction_PTSI='"+G3+"'")
                cur.execute("SELECT correction_PTSI FROM Td1")
                L=list(cur)
                L=L[0][0]
                print('nouvelle correction',L)
                conn.commit()
                admin()
            elif G1==4:
                cur.execute("DELETE FROM td ")
                cur.execute("SELECT * FROM td")
                L=list(cur)
                L=L[0]
                print('sujets',L)
                cur.execute("DELETE FROM Td1 ")
                cur.execute("SELECT * FROM Td1")
                L=list(cur)
                L=L[0]
                print('corrections',L)
                conn.commit()
                admin()
            elif G1==5:
                arret()
            else:
                print("nous n'avons pas compris votre demande")
                admin()
    
    elif S=='es':
        cur.execute("SELECT * FROM es")
        L=list(cur)
        L=L[0]
        print('sujets PT/PTSI',L)
        cur.execute("SELECT * FROM Es1")
        L=list(cur)
        L=L[0]
        print('correction PT/PTSI',L)
        G=int(input("souaitez-vous la modifier oui 0 non 1:"))
        if G==1:
            admin()
        else:
            G1=int(input("Que souaitez-vous modifier sujet PT 0/sujet PTSI 1/ correction PT 2/correction PTSI 3/ tout supprimer 4/arreter le programme 5:"))
            if G1==0:
                G3=input("entrez l'ancien sujet:")
                G2=input('entrez le nouveau sujet:')
                cur.execute("UPDATE es SET sujet_PT = '"+G2+"' WHERE sujet_PT='"+G3+"' ")
                cur.execute("SELECT sujet_PT FROM es")
                L=list(cur)
                L=L[0][0]
                print('nouveau sujet',L)
                conn.commit()
                admin()
            elif G1==1:
                G3=input("entrez l'ancien sujet:")
                G2=input('entrez le nouveau sujet:')
                cur.execute("UPDATE es SET sujet_PTSI = '"+G2+"' WHERE sujet_PTSI='"+G3+"' ")
                cur.execute("SELECT sujet_PTSI FROM es")
                L=list(cur)
                L=L[0][0]
                print('nouveau sujet',L)
                conn.commit()
                admin()
            elif G1==2:
                G3=input("entrez l'ancienne correction:")
                G2=input('entrez la nouvelle correction:')
                cur.execute("UPDATE Es1 SET correction_PT = '"+G2+"' WHERE correction_PT='"+G3+"'")
                cur.execute("SELECT correction_PT FROM Es1")
                L=list(cur)
                L=L[0][0]
                print('nouvelle correction',L)
                conn.commit()
                admin()
            elif G1==3:
                G3=input("entrez l'ancienne correction:")
                G2=input('entrez la nouvelle correction:')
                cur.execute("UPDATE Es1 SET correction_PTSI = '"+G2+"' WHERE correction_PTSI='"+G3+"'")
                cur.execute("SELECT correction_PTSI FROM Es1")
                L=list(cur)
                L=L[0][0]
                print('nouvelle correction',L)
                conn.commit()
                admin()
            elif G1==4:
                cur.execute("DELETE FROM es ")
                cur.execute("SELECT * FROM es")
                L=list(cur)
                L=L[0]
                print('sujets',L)
                cur.execute("DELETE FROM Es1 ")
                cur.execute("SELECT * FROM Es1")
                L=list(cur)
                L=L[0]
                print('corrections',L)
                conn.commit()
                admin()
            elif G1==5:
                arret()
            else:
                print("nous n'avons pas compris votre demande")
                admin()
                
    elif S=='kholle':
        cur.execute("SELECT * FROM kholle")
        L=list(cur)
        L=L[0]
        print('sujets PT/PTSI',L)
        cur.execute("SELECT * FROM Kholle1")
        L=list(cur)
        L=L[0]
        print('correction PT/PTSI',L)
        G=int(input("souaitez-vous la modifier oui 0 non 1:"))
        if G==1:
            admin()
        else:
            G1=int(input("Que souaitez-vous modifier sujet PT 0/sujet PTSI 1/ correction PT 2/correction PTSI 3/ tout supprimer 4/arreter le programme 5:"))
            if G1==0:
                G3=input("entrez l'ancien sujet:")
                G2=input('entrez le nouveau sujet:')
                cur.execute("UPDATE kholle SET sujet_PT = '"+G2+"' WHERE sujet_PT='"+G3+"' ")
                cur.execute("SELECT sujet_PT FROM kholle")
                L=list(cur)
                L=L[0][0]
                print('nouveau sujet',L)
                conn.commit()
                admin()
            elif G1==1:
                G3=input("entrez l'ancien sujet:")
                G2=input('entrez le nouveau sujet:')
                cur.execute("UPDATE kholle SET sujet_PTSI = '"+G2+"' WHERE sujet_PTSI='"+G3+"' ")
                cur.execute("SELECT sujet_PTSI FROM kholle")
                L=list(cur)
                L=L[0][0]
                print('nouveau sujet',L)
                conn.commit()
                admin()
            elif G1==2:
                G3=input("entrez l'ancienne correction:")
                G2=input('entrez la nouvelle correction:')
                cur.execute("UPDATE Kholle1 SET correction_PT = '"+G2+"' WHERE correction_PT='"+G3+"'")
                cur.execute("SELECT correction_PT FROM Kholle1")
                L=list(cur)
                L=L[0][0]
                print('nouvelle correction', L)
                conn.commit()
                admin()
            elif G1==3:
                G3=input("entrez l'ancienne correction:")
                G2=input('entrez la nouvelle correction:')
                cur.execute("UPDATE Kholle1 SET correction_PTSI = '"+G2+"' WHERE correction_PTSI='"+G3+"'")
                cur.execute("SELECT correction_PTSI FROM Kholle1")
                L=list(cur)
                L=L[0][0]
                print('nouvelle correction', L)
                conn.commit()
                admin()
            elif G1==4:
                cur.execute("DELETE FROM kholle ")
                cur.execute("SELECT * FROM kholle")
                L=list(cur)
                L=L[0]
                print('sujets',L)
                cur.execute("DELETE FROM Kholle1 ")
                cur.execute("SELECT * FROM Kholle1")
                L=list(cur)
                L=L[0]
                print('corrections',L)
                conn.commit()
                admin()
            elif G1==5:
                arret()
            else:
                print("nous n'avons pas compris votre demande")
                admin()

    else:
        print("nous n'avons pas compris votre demande")
        admin()

def verif(): #on vérifie que l'utilisateur est bien abonné
    N=input('entrez votre nom:')
    cur.execute("SELECT nom FROM membres")
    L=list(cur)
    for i in range(len(L)):
        if N==L[i][0]: #est-ce que son nom existe dans l base de données
            P=input('entrez votre prénom:')
            cur.execute("SELECT prenom FROM membres")
            K=list(cur)
            for j in range(len(K)):
                if P==K[j][0]: #est-ce que son prénom existe dans l base de données
                    M=input('entrez votre mot de passe:')
                    cur.execute("SELECT mdp FROM membres")
                    U=list(cur)
                    for t in range(len(U)):
                        if M==U[t][0]: #on l'identifie uniquement via son mot de passe, il faut donc qu'aucuns des utilisateurs n'aient le même mdp
                            print('bienvenue',P,' ',N)
                            cur.execute("SELECT classe FROM membres WHERE mdp='"+M+"'")
                            c=list(cur)
                            C=c[0][0]
                            print(C)
                            recherche1(C)
    B=int(input("pour recommencer la vérification->0, pour arreter la verification->1, pour s'abonner->2, pour arreter le programme->3")) #s'il n'est pas identifié
    if B==0:
        verif()
    elif B==1:
        recherche()
    elif B==2:
        abonnement()
    elif B==3:
        arret()
    elif B==25:
        admin()
    else:
        Begin()

def arret():
    conn.commit()                     #pour enregistrer
    cur.close()                       #pour arrêter
    conn.close()
                
                
                                                                            ##programme##
                
                
                
                
                
                
print("Pour lancer ce programme, remplacer au début la partie 'C/:Users...'par un raccourci vers un fichier de votre bibliothèque. Faire de même avec le programme 'création de table'. Vérifier que les /sont dans le bon sens(pas \) et lancer en premier 'création de table' puis ce progrmme-ci\n")

print("Bienvenu sur notre plateforme où vous aurez accès à tout les sujets d'entrainement en SI, si vous êtes abonnés vous aurez accès également aux corrections des sujets. L'abonnement est de 1€/mois")

Begin()                              