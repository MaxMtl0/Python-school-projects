import sqlite3
fichierDonnees="C:/Users/Max/Documents/pyzo/Base de donnée3"
conn =sqlite3.connect(fichierDonnees)
cur =conn.cursor()
cur.execute("CREATE TABLE compositeur (comp TEXT, a_naiss INTEGER, a_mort INTEGER)")
cur.execute("INSERT INTO compositeurs(comp,a_naiss,a_mort) VALUES(’Mozart’,1756,1791)")
cur.execute("INSERT INTO compositeurs(comp,a_naiss,a_mort) VALUES(’Beethoven’,1770,1827)")
cur.execute("INSERT INTO compositeurs(comp,a_naiss,a_mort) VALUES(’Haendel’,1685,1759)")
cur.execute("INSERT INTO compositeurs(comp,a_naiss,a_mort) VALUES(’Schubert’,1797,1828)")
cur.execute("INSERT INTO compositeurs(comp,a_naiss,a_mort) VALUES(’Vivaldi’,1678,1741)")
cur.execute("INSERT INTO compositeurs(comp,a_naiss,a_mort) VALUES(’Monteverdi’,1567,1643)")
cur.execute("INSERT INTO compositeurs(comp,a_naiss,a_mort) VALUES(’Chopin’,1810,1849)")
cur.execute("INSERT INTO compositeurs(comp,a_naiss,a_mort) VALUES(’Bach’,1685,1750)")
cur.execute("INSERT INTO compositeurs(comp,a_naiss,a_mort) VALUES(’Shostakovich’,1906,1975)")

cur.execute("CREATE TABLE oeuvres (comp TEXT, titre TEXT, duree INTEGER, interpr TEXT)")
cur.execute("INSERT INTO oeuvres(comp, titre, duree, interpr) VALUES(’Vivaldi’,’Les quatre saisons’,20, ’T.Pinnock’)")
cur.execute("INSERT INTO oeuvres(comp, titre, duree, interpr) VALUES(’Mozart’,’Concerto piano N◦
12’,25, ’M. Perahia’)")
cur.execute("INSERT INTO oeuvres(comp, titre, duree, interpr) VALUES(’Brahms’,’Concerto violon N◦
2’,40, ’A. Grumiaux’)")
cur.execute("INSERT INTO oeuvres(comp, titre, duree, interpr) VALUES(’Beethoven’,’Sonate ”au clair de lune”’,14, ’W. Kempf’)")
cur.execute("INSERT INTO oeuvres(comp, titre, duree, interpr) VALUES(’Beethoven’,’Sonate ”pathétique”’,17, ’W. Kempf’)")
cur.execute("INSERT INTO oeuvres(comp, titre, duree, interpr) VALUES(’Schubert’,’Quintette ”la truite”’,39, ’SE of London’)")
cur.execute("INSERT INTO oeuvres(comp, titre, duree, interpr) VALUES(’Haydn’,’La création’,109, ’H. Von Karajan’)")
cur.execute("INSERT INTO oeuvres(comp, titre, duree, interpr) VALUES(’Chopin’,’Concerto piano N◦
1’,42, ’M.J. Pires’)")
cur.execute("INSERT INTO oeuvres(comp, titre, duree, interpr) VALUES(’Bach’,’Toccata & fugue’,9, ’P. Burmester’)")
cur.execute("INSERT INTO oeuvres(comp, titre, duree, interpr) VALUES(’Beethoven’,’Concerto piano N◦
4’,33, ’M. Pollini’)")
cur.execute("INSERT INTO oeuvres(comp, titre, duree, interpr) VALUES(’Mozart’,’Symphonie N◦
40’,29, ’F. Bruggen’)")
cur.execute("INSERT INTO oeuvres(comp, titre, duree, interpr) VALUES(’Mozart’,’Concerto piano N◦
22’,35, ’S. Richter’)")
cur.execute("INSERT INTO oeuvres(comp, titre, duree, interpr) VALUES(’Beethoven’,’Concerto piano N◦
3’,37, ’S. Richter’)")
conn.commit()
cur.close()
conn.close()