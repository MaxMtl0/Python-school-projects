import os
rep=os.getcwd()
os.chdir("C:/Users/Max/Documents/pyzo/rep_courant")
rep=os.getcwd()
print(rep)
def wazza():
    print('entrer 3 mots')
    a=int(input('Mot1:'))
    b=int(input('Mot2:'))
    c=int(input('Mot3:'))
    f=open("dico.txt","w")
    l=['a','b','c\n']
    f.writelines(l)
    f.close
    
    g=open("dico.txt","w")
    f=open("dico.txt","r")
    #sauvegarde
    
    g=open("dico.txt","r")
    f=open("dico.txt","w")
    test=0
    for l in g:
        if l<a:
            f.write(l)
        else:
            if test==0:
                f.write(a)
                f.write(l)
                test+=1
            else:
                f.write(l)
    f.close
    g.close
wazza()
