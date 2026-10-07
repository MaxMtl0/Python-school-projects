import tkinter as tk
from tkPDFViewer import tkPDFViewer as pdf
import os
import pyfirmata
import time
import serial
# DEFINITIONS DES FONCTIONS

def saucisse():
    newWindow = tk.Toplevel(fenetre)
    newWindow.geometry("250x300")
#    newWindow.iconbitmap(r'C:/Users/Max/Documents/Cours/Si/convoi/interface/Transport-Express.ico')
    labelExample = tk.Label(newWindow, text = "saucisse")
    labelExample.pack()
   # buttonExample = tk.Button(newWindow, text = "vitesse")
    #buttonExample.place(x = 100, y = 50)
    labelvitesse = tk.Label(newWindow, text = "vitesse : 0.25 m/s")
    labelvitesse.pack()
    #edit = tk.Entry(newWindow)
    #edit.place(x = 50, y = 100)
    #buttonExample1 = tk.Button(newWindow, text = "couple")
    #buttonExample1.place(x = 100, y = 150)
    labelcouple = tk.Label(newWindow, text = "couple : 2.25 N.m")
    labelcouple.pack()
    #edit1 = tk.Entry(newWindow)
    #edit1.place(x = 50, y = 200)
    buttonExample0 = tk.Button(newWindow, text = "modifier programme")#, command=modif)
    buttonExample0.pack()
    buttonExample1 = tk.Button(newWindow, text = "lancer", command=lancer)
    buttonExample1.pack()
 
    
    
def carre_de_porc():
    newWindow = tk.Toplevel(fenetre)
    newWindow.geometry("250x300")
#    newWindow.iconbitmap(r'C:/Users/Max/Documents/Cours/Si/convoi/interface/Transport-Express.ico')
    labelExample = tk.Label(newWindow, text = "carre de porc")
    labelExample.pack()
   # buttonExample = tk.Button(newWindow, text = "vitesse")
   # buttonExample.place(x = 100, y = 50)
    labelvitesse = tk.Label(newWindow, text = "vitesse : 0.25 m/s")
    labelvitesse.pack()
   # edit = tk.Entry(newWindow)
   # edit.place(x = 50, y = 100)
   # buttonExample1 = tk.Button(newWindow, text = "couple")
   # buttonExample1.place(x = 100, y = 150)
    labelcouple = tk.Label(newWindow, text = "couple : 2.25 N.m")
    labelcouple.pack()
   # edit1 = tk.Entry(newWindow)
   # edit1.place(x = 50, y = 200)
    buttonExample1 = tk.Button(newWindow, text = "lancer", command=lancer)
    buttonExample1.place(x = 100, y = 250)
    
def infos():
    root = tk.Toplevel(fenetre)
    root.geometry("650x850")
#    root.iconbitmap(r'C:/Users/Max/Documents/Cours/Si/convoi/interface/Transport-Express.ico')
    v1 = pdf.ShowPdf()
    v1.img_object_li.clear()
#    v2 = v1.pdf_view(root, pdf_location=r"C:/Users/Max/Documents/permis/resultat code.pdf", width=75, height=100)
#    v2.pack()
    print('infos')
    
   # C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PixyMon v2
    
def camera():
    path = "C:/Program Files (x86)/PixyMon v2/bin"
    os.chdir(path)
    os.system("PixyMon v2.exe")
    
def parametre():
    newWindow = tk.Toplevel(fenetre)
    newWindow.geometry("250x200")
    newWindow.iconbitmap(r'C:/Users/Max/Documents/Cours/Si/convoi/interface/Transport-Express.ico')
    labelExample = tk.Label(newWindow, text = "parametre")
    buttonExample = tk.Button(newWindow, text = "changer la taille de la fenêtre")
    labelExample.pack()
    buttonExample.pack()
    


def plus():
        def produit1():
            def interrupteur(a):
                labelExample = tk.Label(newWindow, font=('Arial', 15))
                labelExample.config(text=str(a.get()+'           '))
                bouPurpule.config(text=str(a.get()+'           '), font=('Arial', 15))
                labelExample.place(x = 100, y = 0)
                edit.delete('end')
            
            def sup():
                bouPurpule.pack_forget()
                newWindow.destroy()
                
            newWindow = tk.Toplevel(fenetre)
            newWindow.geometry("250x600")
#            newWindow.iconbitmap(r'C:/Users/Max/Documents/Cours/Si/convoi/interface/Transport-Express.ico')
            b = tk.StringVar()
            edit = tk.Entry(newWindow,width=20, textvariable=b)
            edit.place(x = 50, y = 100)
            tk.Checkbutton(newWindow, text="renommer", onvalue=1, offvalue=0,command = lambda :interrupteur(b)).place(x = 50, y = 50)
            buttonExample = tk.Label(newWindow, text = "vitesse")
            buttonExample.place(x = 100, y = 150)
            edit = tk.Entry(newWindow)
            edit.place(x = 50, y = 200)
            buttonExample1 = tk.Label(newWindow, text = "couple")
            buttonExample1.place(x = 100, y = 250)
            edit1 = tk.Entry(newWindow)
            edit1.place(x = 50, y = 300)
            buttonExample1 = tk.Button(newWindow, text = "lancer", command=lancer)
            buttonExample1.place(x = 100, y = 350)
            supp = tk.Button(newWindow, text = "supprimer bouton",command=sup)
            supp.place(x = 100, y = 400)
            
        bouPurpule = tk.Button(zone1, fg="white", bg="darkred", command = produit1)
        bouPurpule.pack(side=tk.LEFT, fill=tk.Y, ipady=20, ipadx=20, padx=10,pady=10)
        


def temp():
    newWindow = tk.Toplevel(fenetre)
    newWindow.geometry("250x200")
#    newWindow.iconbitmap(r'C:/Users/Max/Documents/Cours/Si/convoi/interface/Transport-Express.ico')
    labelExample = tk.Label(newWindow, text = "température")
    labelExample.pack()
    celcius = tk.Label(newWindow, text = "25.2°C")
    celcius.pack()

#def modif():
 #   path = "C:/Users/Max/Desktop/Arduino IDE/bin"
  #  os.chdir(path)
   # os.system("Arduino IDE.Ink")

def lancer1():
    port = 'COM14'# Windows
    #port = '/dev/ttyACM3' # Linux
    #port = '/dev/tty.usbmodem11401' # Mac

    HIGH = True# Crée un état haut qui correspond à la Led allumé
    LOW = False # Pareil pour l’état bas

    board = pyfirmata.Arduino(port) # Initialise la communication avec la carte
    pin = board.get_pin('d:12:o') # Initialise la broche (d => digital, 13 => N° broche, o => output)

    for i in range(10): # Permet de faire clignoter la micro-led dix fois
        pin.write(HIGH)# Allume la led
        time.sleep(0.2) # Pause de 2 secondes
        pin.write(LOW) # Eteint la led
        time.sleep(0.2) # Nouvelle pause de 2 secondes

    board.exit() # Clôture la communication avec la carte

def on():
	#message.configure(text=" le relais est ON ", fg= 'blue')
	ser = serial.Serial('COM14', 19200, dsrdtr=1)	
	ser.close()
	
def off():
	#message.configure(text=" le relais est OFF", fg= 'red')
	ser = serial.Serial('COM14', 19200, dsrdtr=0)
	ser.close()

def lancer():
    print('e')


# CORPS PRINCIPAL DU PROGRAMME

fenetre = tk.Tk()

fenetre.title("speed-air cochon")

#fenetre.iconbitmap(r'C:/Users/Max/Documents/Cours/Si/convoi/interface/Transport-Express.ico')
fenetre.attributes('-fullscreen', True)

#fenetre.geometry("1500x1000")

# ampoule = tk.PhotoImage(file = r"C:/Users/Max/Documents/Cours/Si/convoi/interface/ampoule.png") 
# engrenage = tk.PhotoImage(file = r"C:/Users/Max/Documents/Cours/Si/convoi/interface/engrenage.png") 
# Picture = tk.PhotoImage(file = r"C:/Users/Max/Documents/Cours/Si/convoi/interface/Picture.png") 
# saucisse1 = tk.PhotoImage(file = r"C:/Users/Max/Documents/Cours/Si/convoi/interface/saucissebis.png") 
# cubeboeuf = tk.PhotoImage(file = r"C:/Users/Max/Documents/Cours/Si/convoi/interface/cube-boeuf.png") 
# plus1 = tk.PhotoImage(file = r"C:/Users/Max/Documents/Cours/Si/convoi/interface/plus1.png") 
# temperature=tk.PhotoImage(file = r"C:/Users/Max/Documents/Cours/Si/convoi/interface/température.png") 
# logorecape = tk.PhotoImage(file = r"C:/Users/Max/Documents/Cours/Si/convoi/interface/logo recape.png") 
# logoicam = tk.PhotoImage(file = r"C:/Users/Max/Documents/Cours/Si/convoi/interface/logo icam.png") 
# logotransporc = tk.PhotoImage(file = r"C:/Users/Max/Documents/Cours/Si/convoi/interface/logo transporc.png") 

# photoimage0 = saucisse1.subsample(10, 10) 
# photoimage1 = cubeboeuf.subsample(4, 4)
# photoimage2 = plus1.subsample(11, 11)
# photoimage3 = Picture.subsample(6, 6)
# photoimage5 = engrenage.subsample(6, 6)
# photoimage6 = ampoule.subsample(6, 6)
# photoimage7 = temperature.subsample(2, 2)
# photoimage8 = logorecape.subsample(2, 2)
# photoimage9 = logoicam.subsample(5, 5)
# photoimage10 = logotransporc.subsample(2, 2)


#bouRouge = tk.Button(fenetre,image = photoimage0, text="saucisse", fg="white", bg="darkred", command = saucisse)
#bouVert = tk.Button(fenetre,image=photoimage1, text="carré de porc", fg="white", bg="darkgrey", command = carre_de_porc)

# - - - - - C'est sur cette zone qu'on définit une Frame - - - -
zone1 = tk.Frame(fenetre, bg='darkgrey')
#bouOrange = tk.Button(zone1, image=photoimage2,text="+", fg="white", bg="darkred", command = plus)
# - - - - - C'est sur cette zone qu'on définit une Frame - - - -

zone2 = tk.Frame(fenetre, bg='darkgrey')

#bouBleua = tk.Button(zone2,image=photoimage6, text="info", fg="white", bg="darkred", command = infos)
# bouBleub = tk.Button(zone2,image=photoimage3, text="caméra", fg="white", bg='darkred', command = camera)
# bouBleuc = tk.Button(zone2,image=photoimage5,text="paramètre", fg="white", bg='darkred', command = parametre)
# bouBleud = tk.Button(zone2,image=photoimage7,text="température", fg="white", bg='darkred', command = temp)

# bouNoir = tk.Button(fenetre, font=('Arial', 15), text="Quitter", fg="white", bg="black", command = fenetre.destroy)
# logo = tk.Label(fenetre,image = photoimage8)
# logo1 = tk.Label(fenetre,image = photoimage9)
# logo2 = tk.Label(fenetre,image = photoimage10)


# bouRouge.pack(fill=tk.X, ipady=10, padx=10,pady=10)

# bouVert.pack(fill=tk.X, ipady=10, padx=10,pady=10)


zone1.pack(fill=tk.X, padx=10,pady=10)
# bouOrange.pack( fill=tk.Y, ipady=20, ipadx=20, padx=10,pady=10)

# zone2.pack(fill=tk.X, padx=10,pady=10)
# bouBleua.pack(side=tk.LEFT, fill=tk.Y, ipady=30, ipadx=40, padx=120,pady=10)
# bouBleub.pack(side=tk.LEFT, fill=tk.Y, ipady=30,ipadx=40, padx=120,pady=10)
# bouBleuc.pack(side=tk.LEFT, fill=tk.Y, ipady=30,ipadx=40, padx=120,pady=10)
# bouBleud.pack(side=tk.LEFT, fill=tk.Y, ipady=30,ipadx=40, padx=120,pady=10)

# bouNoir.pack(fill=tk.X, ipady=20, padx=10,pady=10)

# logo.pack(side=tk.LEFT, fill=tk.Y, ipady=30, ipadx=20, padx=50,pady=10)
# logo1.pack(side=tk.LEFT, fill=tk.Y, ipady=30, ipadx=20, padx=50,pady=10)
# logo2.pack(side=tk.LEFT, fill=tk.Y, ipady=30, ipadx=20, padx=50,pady=10)







fenetre.mainloop()
#line = ser.readline()
#♫ser.close()







