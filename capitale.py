#capitale
from ville import Ville
class Capitale(Ville):
    def __init__(self,nom,nbHabitants,pays):
        super().__init__(nom,nbHabitants)
        self.pays = pays
    
    def __str__(self):
        return  super().__str__()+"Capitale de "+self.pays

