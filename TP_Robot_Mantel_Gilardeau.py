class LiaisonSerie():
    def __init__(self,port):
        self.port = port
        print("Connexion au port "+self.port+"\n")

    def envoyerCommande(self,cmd):
        print("Envoi de la commande : "+cmd+" sur le port"+self.port)

    def envoyerCommandeAvecReponse(self,cmd):
        print("Envoi de la commande attendant une reponse : "+cmd+" sur le port "+self.port)
        reponse = input("Entrez la reponse : ")
        return reponse
    


class Moteur():
    def __init__(self,vitesse,position,L):
        self.vitesse = vitesse
        self.position = position
        self.L = L                      #liaison série

    def __str__(self):
        return "Le moteur " + self.position + " a une vitesse de " +str(self.vitesse)

    def arret(self):
        self.vitesse = 0
        L.envoyerCommande("D,"+str(self.vitesse)+","+str(self.position))
    
    def vitesse(self,v):
        if v <=-9 :
            self.vitesse = -9
        elif v>= 9:
            self.vitesse = 9
        else :
            self.vitesse = v
        
        

class Capteur():                                #type = lum ou prox, indice = n°
    def __init__(self,type,indice_capteur, L):
        self.type = type
        self.indice_capteur = indice_capteur
        self.L = L
        
        

class CapteurLuminosite(Capteur):               #Heridité de class Capteur
    def __init__(self,type,indice_capteur,ValLum,L):
        super().__init__(type,indice_capteur, L)
        self.ValLum = ValLum

    def __str__(self):
        return "Le capteur de lumière " + str(self.indice_capteur) + " a pour valeur " + str(self.ValLum)
    
    

class CapteurProx(Capteur):                     #Heridité de class Capteur
    def __init__(self,type,indice_capteur,do,L):  #do = distance de l'obstacle
        super().__init__(type,indice_capteur, L)
        self.do = do

    def __str__(self):
        return "Le capteur de proximité " + str(self.indice_capteur) + " a pour valeur " + str(self.do)

    def obstacle(self):
        if self.do<50:                  #50 cm
            print("Obstacle détecté vers le capteur " + str(self.indice_capteur))
            return True                 
        else:
            return False
    def cible(self):
        L0=[]
        L0.append(self.capteurAvd.do)
        L0.append(self.capteurAvg.do)
        L0.append(self.capteurAv.do)
        L0.append(self.capteurAr.do)
        L0.append(self.capteurG.do)
        L0.append(self.capteurD.do)
        compteur0 = 1
        min = L0[0]
        while compteur0 < len(L0):
            potentielmin = L0[compteur0]
            if min >= potentielmin :
                min = potentielmin                                  #si 2 capteurs ont la même luminosité, le max est enregistré sur le premier capteur
            compteur0+=1
        return L0.index(min)+1



class Robot():
    def __init__(self, L):
        self.L = L
        self.Mg = Moteur(5,"g",L)
        self.Md = Moteur(5,"d",L)
        self.Vitesse_moy = 5

    def droite(self):
        self.Md.arret()
        self.Mg.vitesse > 0
        print("Le robot tourne à droite\n")

    def gauche(self):
        self.Mg.arret()
        self.Md.vitesse > 0
        print("Le robot tourne à gauche\n")

    def stop(self):
        self.Mg.arret()
        self.Md.arret()
        print("Le robot s'arrête\n")

    def avancer(self):
        self.Md.vitesse = self.Vitesse_moy 
        self.Mg.vitesse = self.Vitesse_moy         
        print("Le robot avance tout droit\n")

    def reculer(self):
        self.Md.vitesse = -1 * self.Vitesse_moy
        self.Mg.vitesse = -1 * self.Vitesse_moy
        L.envoyerCommande("D," + str(self.Md.vitesse) + "," + str(self.Md.position))
        L.envoyerCommande("D," + str(self.Mg.vitesse) + "," + str(self.Mg.position))
        print("Le Robot recule\n")
        
        

class Obstacle(Robot,CapteurProx):
    def __init__(self,L):
        super().__init__(L)
        self.capteurAvd = CapteurProx("n",1, 100, L)
        self.capteurAvg = CapteurProx("n", 2, 100, L)
        self.capteurAv = CapteurProx("n", 3, 100, L)
        self.capteurAr = CapteurProx("n", 4, 100, L)
        self.capteurG = CapteurProx("n", 5, 100, L)
        self.capteurD = CapteurProx("n", 6, 49, L)          #obstacle détecté à droite


    def eviter(self):
        print("      RobotEviteur")
        if self.capteurAvd.obstacle() == True or self.capteurD.obstacle() == True:
            self.gauche()
        elif self.capteurAvg.obstacle() == True or self.capteurG.obstacle() == True:
            self.droite()
        elif self.capteurAv.obstacle() == True :
            self.reculer()
        elif self.capteurAr.obstacle() == True :
            self.avancer()
        else:
            Mode_Obstacle.avancer()            #pas toujours pertinent en fonction du terrain ->stopper
            
    def foncer(self):
        print("      RobotFonceur")
        if self.cible() == 2 or self.cible() == 5 :
            print("L'obstacle le plus proche est à gauche")
            self.gauche()
        elif self.cible() == 1 or self.cible() == 6 :
            print("L'obstacle le plus proche est à droite")
            self.droite()
        elif self.cible() == 3 :
            print("L'obstacle le plus proche est devant")
            self.avancer()
        elif self.cible() == 4 :
            print("L'obstacle le plus proche est derrière")
            self.reculer()
        else:
            Mode_Obstacle.avancer()          
            
        

class Photon(Robot):
    def __init__(self,L):
        super().__init__(L)
        self.capteurAvd = CapteurLuminosite("o",1, 100, L)
        self.capteurAvg = CapteurLuminosite("o", 2, 100, L)
        self.capteurAv = CapteurLuminosite("o", 3, 100, L)
        self.capteurAr = CapteurLuminosite("o", 4, 100, L)
        self.capteurG = CapteurLuminosite("o", 5, 100, L)
        self.capteurD = CapteurLuminosite("o", 6, 48, L)       #le plus de lumière à droite
        
    def capt_max(self):
        L1=[]
        L1.append(self.capteurAvd.ValLum)
        L1.append(self.capteurAvg.ValLum)
        L1.append(self.capteurAv.ValLum)
        L1.append(self.capteurAr.ValLum)
        L1.append(self.capteurG.ValLum)
        L1.append(self.capteurD.ValLum)
        compteur = 0
        max = L1[0]
        max1 = L1[compteur + 1]
        while compteur < len(L1):
            if max <= max1 :
                max = max1                                  #si 2 capteurs ont la même luminosité, le max est enregistré sur le premier capteur
                compteur+=1
            else :
                compteur+=1
        return L1.index(max)


    def phile(self):
        print("      PhotoPhile")
        if self.capt_max() == 1 or self.capt_max() == 6:
            print("Le plus de lumière est détecté vers la droite")
            self.droite()
        elif self.capt_max() == 2 or self.capt_max() == 5:
            print("Le plus de lumière est détecté vers la gauche")
            self.gauche()
        elif self.capt_max() == 3:
            print("Le plus de lumière est détecté vers l'avant")
            self.avancer()
        elif self.capt_max() == 4:
            print("Le plus de lumière est détecté vers l'arrière")
            self.reculer()
        else :
            print("La lumière ne varie pas")
            self.stop()             #si tous les capteurs sont au même niveau il s'arrête
            
    def phobe(self):
        print("      PhotoPhobe")
        if self.capt_max() == 1 or self.capt_max() == 6:
            print("Le plus de lumière est détecté vers la droite")
            self.gauche()
        elif self.capt_max() == 2 or self.capt_max() == 5:
            print("Le plus de lumière est détecté vers la gauche")
            self.droite()
        elif self.capt_max() == 3:
            print("Le plus de lumière est détecté vers l'avant")
            self.reculer()
        elif self.capt_max() == 4:
            print("Le plus de lumière est détecté vers l'arrière")
            self.avancer()
        else :
            print("La lumière ne varie pas")
            self.stop()             #si tous les capteurs sont au même niveau il s'arrête

            


if __name__ == "__main__":
    L = LiaisonSerie("COM4")
    Mode_Obstacle = Obstacle(Robot) 
    
    Mode_Obstacle.capteurAvd.do = 100
    Mode_Obstacle.capteurAvg.do =100
    Mode_Obstacle.capteurAv.do =100
    Mode_Obstacle.capteurAr.do =100
    Mode_Obstacle.capteurG.do =100
    Mode_Obstacle.capteurD.do =100
    
    Mode_Photon = Photon(Robot)
    Mode_Photon.capteurAvd.ValLum = 50
    Mode_Photon.capteurAvg.ValLum = 100
    Mode_Photon.capteurAv.ValLum = 125
    Mode_Photon.capteurAr.ValLum = 150
    Mode_Photon.capteurG.ValLum = 175
    Mode_Photon.capteurD.ValLum = 200
    
    Mode_Obstacle.eviter()
    Mode_Photon.phile()
    Mode_Photon.phobe()
    Mode_Obstacle.foncer()