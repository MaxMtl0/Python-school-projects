import sqlite3
fichierDonnees="C:/Users/Max/Documents/pyzo/Base de donnée3.sq3"
conn =sqlite3.connect(fichierDonnees)
cur =conn.cursor()
cur.execute("CREATE TABLE membres (age INTEGER, nom TEXT, taille REAL)")
cur.execute("INSERT INTO membres(age,nom,taille) VALUES(21,'Dupont',1.83)")
cur.execute("INSERT INTO membres(age,nom,taille) VALUES(15,'Martin',1.57)")
cur.execute("INSERT INTO membres(age,nom,taille) VALUES(18,'Schmitd',1.69)")
conn.commit()
cur.close()
conn.close()
