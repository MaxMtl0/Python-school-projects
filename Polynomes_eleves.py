from math import *

class Poly2(object) :
    """Polynôme du second degré."""
    def __init__(self,coefa,coefb,coefc) :
        """Construit un polynôme à partir des coefficients a,b,c."""
        self.a = coefa
        self.b = coefb
        self.c = coefc

    def __str__(self) :
        """Chaîne d'affichage du polynôme."""
        if self.b>=0 and self.c>=0 :  
            s = "{0.a}x²+{0.b}x+{0.c}".format(self)
        elif self.b<0 and self.c>=0 :
            s = "{0.a}x²{0.b}x+{0.c}".format(self)
        elif self.b>=0 and self.c<0 :
            s = "{0.a}x²+{0.b}x{0.c}".format(self)
        else :
            s = "{0.a}x²{0.b}x{0.c}".format(self)
        return s        
        
#     def delta(self):
#         if self(b)*self(b)-4*self(a)*self(c)<0:
#             return 'pas de racines'
#         elif self(b)*self(b)-4*self(a)*self(c)==0:
#             return -self(b)/(2*self(a))
#         else:
#             return b
# p=Poly2(1,4,1)
# print(p.a)
# print(p)
# Poly2.delta(p)
