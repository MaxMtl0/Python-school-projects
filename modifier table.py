import sqlite3
conn =sqlite3.connect("C:/Users/Max/Documents/pyzo/sujets si.sq3")
cur =conn.cursor()
cur.execute("SELECT * FROM membres")

cur.execute("INSERT INTO membres(age,nom,prenom,classe,abonnement) VALUES(19,'Ricard','pernot','PTSI','non')")     #ajouter
cur.execute("UPDATE membres SET nom ='Gerart' WHERE nom='Ricard'")      #modifier
cur.execute("DELETE FROM membres WHERE nom='Gerart'")                 #supprimer

# cur.execute("UPDATE kholle SET sujet ='RDM' WHERE sujet='a'")
# cur.execute("UPDATE sujets SET td ='https://classroom.google.com/u/1/w/MzIwMTQwMDQ2NjA5/t/all' WHERE td='b'")


cur.execute("SELECT age FROM membres")
L=list(cur)
print(L)

cur.execute("SELECT * FROM membres")
L1=list(cur)
print(L1)

# cur.execute("SELECT * FROM cc")
# L1=cur.fetchall()
# print(L1)
# 
# cur.execute("SELECT * FROM kholle")
# L=list(cur)
# print(L)


conn.commit()
cur.close()
conn.close()

