import random

o1=random.randint(1,6)
o2=random.randint(1,6)
j1=random.randint(1,6)
j2=random.randint(1,6)
print('ordi :',o1,o2,' et joueur',j1,j2)

if o1==o2 and j1!=j2:   #!= veut dire différent
    print('ordi gagne')
elif j1==j2 and o1!=o2:  #elif veut dire sinon si...
    print('joueur gagne')
elif j1+j2>o1+o2:
    print('joueur gagne')
elif o1+o2>j1+j2:
    print('ordi gagne')
else :                   #else veut dire sinon...
        print('égalité')
