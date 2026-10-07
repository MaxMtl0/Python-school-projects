# PROJET TD INFO
import sqlite3
fichierDonnees ="C:/Users/Max/Documents/pyzo/sujets si.sq3"
conn =sqlite3.connect(fichierDonnees)
cur =conn.cursor()
cur.execute("CREATE TABLE membres (age INTEGER, nom TEXT, prenom TEXT, classe TEXT, abonnement TEXT, mdp TEXT)")
cur.execute("INSERT INTO membres(age,nom,prenom,classe,abonnement,mdp) VALUES(19,'Derras','Rayan','PT','oui','azerty')")

cur.execute("CREATE TABLE kholle (sujet_PT TEXT,sujet_PTSI TEXT)")
cur.execute("INSERT INTO kholle(sujet_PT,sujet_PTSI) VALUES('khollept','kholleptsi')")

cur.execute("CREATE TABLE cb (sujet_PT TEXT,sujet_PTSI TEXT)")
cur.execute("INSERT INTO cb (sujet_PT,sujet_PTSI) VALUES('cbpt','cbptsi')")

cur.execute("CREATE TABLE td (sujet_PT TEXT,sujet_PTSI TEXT)")
cur.execute("INSERT INTO td(sujet_PT,sujet_PTSI) VALUES('tdpt','tdptsi')")

cur.execute("CREATE TABLE cc (sujet_PT TEXT,sujet_PTSI TEXT)")
cur.execute("INSERT INTO cc(sujet_PT,sujet_PTSI) VALUES('ccpt','ccptsi')")

cur.execute("CREATE TABLE es (sujet_PT TEXT,sujet_PTSI TEXT)")
cur.execute("INSERT INTO es(sujet_PT,sujet_PTSI) VALUES('espt','esptsi')")

cur.execute("CREATE TABLE tp (sujet_PT TEXT,sujet_PTSI TEXT)")
cur.execute("INSERT INTO tp(sujet_PT,sujet_PTSI) VALUES('tppt','tpptsi')")

cur.execute("CREATE TABLE Kholle1 (correction_PT TEXT,correction_PTSI TEXT)")
cur.execute("INSERT INTO Kholle1(correction_PT ,correction_PTSI) VALUES('khollept1','kholleptsi1')")

cur.execute("CREATE TABLE Cb1 (correction_PT TEXT,correction_PTSI TEXT)")
cur.execute("INSERT INTO Cb1 (correction_PT ,correction_PTSI) VALUES('cbpt1','cbptsi1')")

cur.execute("CREATE TABLE Td1 (correction_PT TEXT,correction_PTSI TEXT)")
cur.execute("INSERT INTO Td1(correction_PT ,correction_PTSI) VALUES('tdpt1','tdptsi1')")

cur.execute("CREATE TABLE Cc1 (correction_PT TEXT,correction_PTSI TEXT)")
cur.execute("INSERT INTO Cc1(correction_PT ,correction_PTSI) VALUES('ccpt1','ccptsi1')")

cur.execute("CREATE TABLE Es1 (correction_PT TEXT,correction_PTSI TEXT)")
cur.execute("INSERT INTO Es1(correction_PT ,correction_PTSI) VALUES('espt1','esptsi1')")

cur.execute("CREATE TABLE Tp1 (correction_PT TEXT,correction_PTSI TEXT)")
cur.execute("INSERT INTO Tp1(correction_PT ,correction_PTSI) VALUES('tppt1','tpptsi1')")
conn.commit()
cur.close()
conn.close()
