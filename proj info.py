import sqlite3

def recherche1(Z):                                                                   #recherche si abonné
    def correction_kholle(Z):
        Z1=int(input('souhaitez-vous la correction? oui 0 non 1:'))
        if Z1==1:
            recherche1(Z)
        elif Z1==0:
            cur.execute("SELECT * FROM Kholle1")
            L=list(cur)
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
            cur.execute("SELECT * FROM Td1")
            L=list(cur)
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
            cur.execute("SELECT * FROM Cc1")
            L=list(cur)
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
            cur.execute("SELECT * FROM Cb1")
            L=list(cur)
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
            cur.execute("SELECT * FROM Tp1")
            L=list(cur)
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
            cur.execute("SELECT * FROM Es1")
            L=list(cur)
            print(L)
            recherche1(Z)
        else:
            print("nous n'avons pas compris votre demande")
            correction_td(Z)
            
    D=input('Sur quel sujet souhaitez-vous vous entrainer; kholle, td, cc, es, cb, tp:')
    if D=='kholle':
        if Z=='PT':
            cur.execute("SELECT sujet_PT FROM kholle")
            L=list(cur)
            print(L)
            correction_kholle(Z)
        elif Z=='PTSI':
            cur.execute("SELECT sujet_PTSI FROM kholle")
            L=list(cur)
            print(L)
            correction_kholle(Z)
        else:
            print("Nous n'avons pas compris dans quelle classe vous êtes") 
            recherche1(Z)
    elif D=='td':
        if Z=='PT':
            cur.execute("SELECT sujet_PT FROM td")
            L=list(cur)
            print(L)
            correction_td(Z)
        elif Z=='PTSI':
            cur.execute("SELECT sujet_PTSI FROM td")
            L=list(cur)
            print(L)
            correction_td(Z)
        else:
            print("Nous n'avons pas compris dans quelle classe vous êtes") 
            recherche1(Z)
    elif D=='cc':
        if Z=='PT':
            cur.execute("SELECT sujet_PT FROM cc")
            L=list(cur)
            print(L)
            correction_cc(Z)
        elif Z=='PTSI':
            cur.execute("SELECT sujet_PTSI FROM cc")
            L=list(cur)
            print(L)
            correction_cc(Z)
        else:
            print("Nous n'avons pas compris dans quelle classe vous êtes") 
            recherche1(Z)
    elif D=='es':
        if Z=='PT':
            cur.execute("SELECT sujet_PT FROM es")
            L=list(cur)
            print(L)
            correction_es(Z)
        elif Z=='PTSI':
            cur.execute("SELECT sujet_PTSI FROM es")
            L=list(cur)
            print(L)
            correction_es(Z)
        else:
            print("Nous n'avons pas compris dans quelle classe vous êtes") 
            recherche1(Z)
    elif D=='cb':
        if Z=='PT':
            cur.execute("SELECT sujet_PT FROM cb")
            L=list(cur)
            print(L)
            correction_cb(Z)
        elif Z=='PTSI':
            cur.execute("SELECT sujet_PTSI FROM cb")
            L=list(cur)
            print(L)
            correction_cb(Z)
        else:
            print("Nous n'avons pas compris dans quelle classe vous êtes") 
            recherche1(Z)
    elif D=='tp':
        if Z=='PT':
            cur.execute("SELECT sujet_PT FROM tp")
            L=list(cur)
            print(L)
            correction_tp(Z)
        elif Z=='PTSI':
            cur.execute("SELECT sujet_PTSI FROM tp")
            L=list(cur)
            print(L)
            correction_tp(Z)
        else:
            print("Nous n'avons pas compris dans quelle classe vous êtes") 
            recherche1(Z)
    else:
        print("nous n'avons pas compris votre demande")
        recherche1(Z)

def recherche():                                                                        #recherche si non abonné
    A=input("vous souhaitez accéder à des sujets de quel niveau? PTSI ou PT :")
    D=input('Sur quel sujet souhaitez-vous vous entrainer; kholle, td, cc, es, cb, tp:')
    if D=='kholle':
        if A=='PT':
            cur.execute("SELECT sujet_PT FROM kholle")
            L=list(cur)
            print(L)
            print('souhaitez-vous la correction? si oui il faut vous abonner')
            Begin1()
        elif A=='PTSI':
            cur.execute("SELECT sujet_PTSI FROM kholle")
            L=list(cur)
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
            print(L)
            print('souhaitez-vous la correction? si oui il faut vous abonner')
            Begin1()
        elif A=='PTSI':
            cur.execute("SELECT sujet_PTSI FROM td")
            L=list(cur)
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
            print(L)
            print('souhaitez-vous la correction? si oui il faut vous abonner')
            Begin1()
        elif A=='PTSI':
            cur.execute("SELECT sujet_PTSI FROM cc")
            L=list(cur)
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
            print(L)
            print('souhaitez-vous la correction? si oui il faut vous abonner')
            Begin1()
        elif A=='PTSI':
            cur.execute("SELECT sujet_PTSI FROM es")
            L=list(cur)
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
            print(L)
            print('souhaitez-vous la correction? si oui il faut vous abonner')
            Begin1()
        elif A=='PTSI':
            cur.execute("SELECT sujet_PTSI FROM cb")
            L=list(cur)
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
            print(L)
            print('souhaitez-vous la correction? si oui il faut vous abonner')
            Begin1()
        elif A=='PTSI':
            cur.execute("SELECT sujet_PTSI FROM tp")
            L=list(cur)
            print(L)
            print('souhaitez-vous la correction? si oui il faut vous abonner')
            Begin1()
        else:
            print("Nous n'avons pas compris dans quelle classe vous êtes") 
            recherche()
    else:
        print("nous n'avons pas compris votre demande de sujet")
        recherche()
        
def abonnement():
    C=input('quel est votre nom?:')
    F=input('quel est votre prénom?:') 
    E=input('quel est votre âge?:')
    G=input('En quel classe êtes vous?:')
    H=input('entrez un mot de passe:')
    cur.execute("INSERT INTO membres(age,nom,prenom,classe,mdp) VALUES('"+E+"','"+C+"','"+F+"','"+G+"','"+H+"')")
    
    cur.execute("SELECT * FROM membres")
    L=list(cur)
    
    print(L)
    print('Vous êtes abonné!!')
    recherche1()
    
def Begin1():
    B=int(input('souhaitez-vous vous abonner? oui 0; non 1 :'))
    if B==1:
        recherche()
    elif B==0:
        abonnement()
    else:
        Begin1()

def Begin():
    A=int(input('êtes vous abonnés? oui 0; non 1 :'))
    if A==1:
        Begin1()
    elif A==0:
        verif() 
    elif A==25:
        admin()
    else:
        Begin()
        
def admin():
    print('vous êtes administrateur')
    S=input('à quelle table voulez-vous accéder?:')
    if S=='cb':
        cur.execute("SELECT * FROM cb")
        L=list(cur)
        print(L)
        G=int(input("souaitez-vous la modifier oui 0 non 1:"))
        if G==1:
            admin()
        else:
            G1=int(input("Que souaitez-vous modifier sujet 0/ correction 1/ tout supprimer 3:"))
            if G1==3:
                cur.execute("DELETE FROM cb WHERE sujet='a'")
                cur.execute("SELECT * FROM cb")
                L=list(cur)
                print(L)
                admin()
            elif G1==0:
                G3=input("entrez l'ancien sujet:")
                G2=input('entrez le nouveau sujet:')
                cur.execute("UPDATE cb SET sujet = '"+G2+"' WHERE sujet='"+G3+"' ")
                cur.execute("SELECT * FROM cb")
                L=list(cur)
                print(L)
                admin()
            elif G1==1:
                G3=input("entrez l'ancienne correction:")
                G2=input('entrez la nouvelle correction:')
                cur.execute("UPDATE cb SET correction = '"+G2+"' WHERE correction='"+G3+"'")
                cur.execute("SELECT * FROM cb")
                L=list(cur)
                print(L)
                admin()
            else:
                print("nous n'avons pas compris votre demande")
                admin()
        
    elif S=='tp':
        cur.execute("SELECT * FROM tp")
        L=list(cur)
        print(L)
        G=int(input("souaitez-vous la modifier oui 0 non 1:"))
        if G==1:
            admin()
        else:
            G1=int(input("Que souaitez-vous modifier sujet 0/ correction 1/ tout supprimer 3:"))
            if G1==3:
                cur.execute("DELETE FROM tp WHERE sujet='a'")
                cur.execute("SELECT * FROM tp")
                L=list(cur)
                print(L)
                admin()
            elif G1==0:
                G3=input("entrez l'ancien sujet:")
                G2=input('entrez le nouveau sujet:')
                cur.execute("UPDATE kholle SET sujet = '"+G2+"' WHERE sujet='"+G3+"' ")
                cur.execute("SELECT * FROM tp")
                L=list(cur)
                print(L)
                admin()
            elif G1==1:
                G3=input("entrez l'ancienne correction:")
                G2=input('entrez la nouvelle correction:')
                cur.execute("UPDATE tp SET correction = '"+G2+"' WHERE correction='"+G3+"'")
                cur.execute("SELECT * FROM tp")
                L=list(cur)
                print(L)
                admin()
            else:
                print("nous n'avons pas compris votre demande")
                admin()
        
    elif S=='kholle':
        cur.execute("SELECT * FROM kholle")
        L=list(cur)
        print(L)
        G=int(input("souaitez-vous la modifier oui 0 non 1:"))
        if G==1:
            admin()
        else:
            G1=int(input("Que souaitez-vous modifier sujet 0/ correction 1/ tout supprimer 3:"))
            if G1==3:
                cur.execute("DELETE FROM kholle WHERE sujet='a'")
                cur.execute("SELECT * FROM kholle")
                L=list(cur)
                print(L)
                admin()
            elif G1==0:
                G3=input("entrez l'ancien sujet:")
                G2=input('entrez le nouveau sujet:')
                cur.execute("UPDATE kholle SET sujet = '"+G2+"' WHERE sujet='"+G3+"' ")
                cur.execute("SELECT * FROM kholle")
                L=list(cur)
                print(L)
                admin()
            elif G1==1:
                G3=input("entrez l'ancienne correction:")
                G2=input('entrez la nouvelle correction:')
                cur.execute("UPDATE kholle SET correction = '"+G2+"' WHERE correction='"+G3+"'")
                cur.execute("SELECT * FROM kholle")
                L=list(cur)
                print(L)
                admin()
            else:
                print("nous n'avons pas compris votre demande")
                admin()
        
    elif S=='cc':
        cur.execute("SELECT * FROM cc")
        L=list(cur)
        print(L)
        G=int(input("souaitez-vous la modifier oui 0 non 1:"))
        if G==1:
            admin()
        else:
            G1=int(input("Que souaitez-vous modifier sujet 0/ correction 1/ tout supprimer 3:"))
            if G1==3:
                cur.execute("DELETE FROM cc WHERE sujet='a'")
                cur.execute("SELECT * FROM cc")
                L=list(cur)
                print(L)
                admin()
            elif G1==0:
                G3=input("entrez l'ancien sujet:")
                G2=input('entrez le nouveau sujet:')
                cur.execute("UPDATE cc SET sujet = '"+G2+"' WHERE sujet='"+G3+"' ")
                cur.execute("SELECT * FROM cc")
                L=list(cur)
                print(L)
                admin()
            elif G1==1:
                G3=input("entrez l'ancienne correction:")
                G2=input('entrez la nouvelle correction:')
                cur.execute("UPDATE cc SET correction = '"+G2+"' WHERE correction='"+G3+"'")
                cur.execute("SELECT * FROM cc")
                L=list(cur)
                print(L)
                admin()
            else:
                print("nous n'avons pas compris votre demande")
                admin()
        
    elif S=='es':
        cur.execute("SELECT * FROM es")
        L=list(cur)
        print(L)
        G=int(input("souaitez-vous la modifier oui 0 non 1:"))
        if G==1:
            admin()
        else:
            G1=int(input("Que souaitez-vous modifier sujet 0/ correction 1/ tout supprimer 3:"))
            if G1==3:
                cur.execute("DELETE FROM es WHERE sujet='a'")
                cur.execute("SELECT * FROM es")
                L=list(cur)
                print(L)
                admin()
            elif G1==0:
                G3=input("entrez l'ancien sujet:")
                G2=input('entrez le nouveau sujet:')
                cur.execute("UPDATE es SET sujet = '"+G2+"' WHERE sujet='"+G3+"' ")
                cur.execute("SELECT * FROM es")
                L=list(cur)
                print(L)
                admin()
            elif G1==1:
                G3=input("entrez l'ancienne correction:")
                G2=input('entrez la nouvelle correction:')
                cur.execute("UPDATE td SET correction = '"+G2+"' WHERE correction='"+G3+"'")
                cur.execute("SELECT * FROM es")
                L=list(cur)
                print(L)
                admin()
            else:
                print("nous n'avons pas compris votre demande")
                admin()
        
    elif S=='td':
        cur.execute("SELECT * FROM td")
        L=list(cur)
        print(L)
        G=int(input("souaitez-vous la modifier oui 0 non 1:"))
        if G==1:
            admin()
        else:
            G1=int(input("Que souaitez-vous modifier sujet 0/ correction 1/ tout supprimer 3:"))
            if G1==3:
                cur.execute("DELETE FROM td WHERE sujet='a'")
                cur.execute("SELECT * FROM td")
                L=list(cur)
                print(L)
                admin()
            elif G1==0:
                G3=input("entrez l'ancien sujet:")
                G2=input('entrez le nouveau sujet:')
                cur.execute("UPDATE td SET sujet = '"+G2+"' WHERE sujet='"+G3+"' ")
                cur.execute("SELECT * FROM td")
                L=list(cur)
                print(L)
                admin()
            elif G1==1:
                G3=input("entrez l'ancienne correction:")
                G2=input('entrez la nouvelle correction:')
                cur.execute("UPDATE td SET correction = '"+G2+"' WHERE correction='"+G3+"'")
                cur.execute("SELECT * FROM td")
                L=list(cur)
                print(L)
                admin()
            else:
                print("nous n'avons pas compris votre demande")
                admin()
    else:
        print("nous n'avons pas compris votre demande")
        admin()

def verif():
    N=input('entrez votre nom:')
    cur.execute("SELECT nom FROM membres")
    L=list(cur)
    for i in range(len(L)):
        if N==L[i]:
            P=input('entrez votre prénom:')
            cur.execute("SELECT prenom FROM membres")
            K=list(cur)
            for j in range(len(K)):
                if P==K[j]:
                    M=input('entrez votre mot de passe:')
                    cur.execute("SELECT mdp FROM membres")
                    U=list(cur)
                    for t in range(len(U)):
                        if M==U[t]:
                            print('bienvenue',P,' ',N)
                            cur.execute("SELECT classe FROM membres WHERE mdp='"+M+"'")
                            C=list(cur)
                            recherche1(C)
    B=int(input("pour recommencer la vérification->0, pour arreter la verification->1, pour s'abonner->2, pour arreter le programme->3"))
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
    conn.commit()
    cur.close()
    conn.close()
                
                
conn =sqlite3.connect("C:/Users/Max/Documents/pyzo/sujets si.sq3")
cur =conn.cursor()

print("Bienvenu sur notre plateforme où vous aurez accès à tout les sujets d'entrainement en SI, si vous êtes abonnés vous aurez accès également aux corrections des sujets. L'abonnement est de 1€/mois")
Begin()                 
                #modifier une table
                #PT PTSI
                #arréter le programme
                #vérifier l'abonnement