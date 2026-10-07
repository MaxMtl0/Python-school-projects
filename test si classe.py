import tkinter as tk
    
class DemoWidget(tk.Frame):

    def __init__(self, fenetre):
        super().__init__(fenetre)
        self.saucisse()
        self.carre_de_porc()
        self.infos()
        self.camera()
        self.parametre()
        self.plus()
        self.interrupteur(e)
        self.produit1()
        self.pack()
        
    def saucisse(self,fenetre):
        newWindow = tk.Toplevel(fenetre)
        newWindow.geometry("250x300")
        labelExample = tk.Label(self, newWindow, text = "saucisse")
        labelExample.place(x = 100, y = 0)
        buttonExample = tk.Button(self, newWindow, text = "vitesse")
        buttonExample.place(x = 100, y = 50)
        edit = Entry(self,newWindow)
        edit.place(x = 50, y = 100)
        buttonExample1 = tk.Button(self,newWindow, text = "couple")
        buttonExample1.place(x = 100, y = 150)
        edit1 = Entry(self,newWindow)
        edit1.place(x = 50, y = 200)
        buttonExample1 = tk.Button(self,newWindow, text = "lancer")
        buttonExample1.place(x = 100, y = 250)
    
    def carre_de_porc(self,fenetre):
        newWindow = tk.Toplevel(fenetre)
        newWindow.geometry("250x300")
        labelExample = tk.Label(self,newWindow, text = "carre de porc")
        labelExample.place(x = 80, y = 0)
        buttonExample = tk.Button(self,newWindow, text = "vitesse")
        buttonExample.place(x = 100, y = 50)
        edit = Entry(self,newWindow)
        edit.place(x = 50, y = 100)
        buttonExample1 = tk.Button(self,newWindow, text = "couple")
        buttonExample1.place(x = 100, y = 150)
        edit1 = Entry(self,newWindow)
        edit1.place(x = 50, y = 200)
        buttonExample1 = tk.Button(self,newWindow, text = "lancer")
        buttonExample1.place(x = 100, y = 250)
        
    def infos(fenetre):
        print('infos')
        
    def camera(fenetre):
        print('camera')
    
    def parametre(fenetre):
        newWindow = tk.Toplevel(fenetre)
        newWindow.geometry("250x200")
        labelExample = tk.Label(self,newWindow, text = "parametre")
        buttonExample = tk.Button(self,newWindow, text = "bouton inutile")
        labelExample.place(x = 100, y = 100)
        buttonExample.place(x = 100, y = 100)
    
    def plus(fenetre):
        bouPurpule = Button(self,fenetre, fg="white", bg="red", command = produit1)
        bouPurpule.pack(fill=X, ipady=10, padx=10,pady=10)


    def produit1(fenetre):
        newWindow = tk.Toplevel(fenetre)
        newWindow.geometry("250x600")
        cb = IntVar()
        Checkbutton(self,newWindow, text="renommer", variable=cb, onvalue=1, offvalue=0, command=interrupteur).place(x = 50, y = 50)
        edit = Entry(self,newWindow)
        edit.place(x = 50, y = 100)
        nom = edit.get()
        if  cb.get() == 0:
            labelExample = tk.Label(self,newWindow, text = nom)
            labelExample.place(x = 100, y = 0)
            edit.delete('end')
        buttonExample = tk.Label(self,newWindow, text = "vitesse")
        buttonExample.place(x = 100, y = 150)
        edit = Entry(self,newWindow)
        edit.place(x = 50, y = 200)
        buttonExample1 = tk.Label(self,newWindow, text = "couple")
        buttonExample1.place(x = 100, y = 250)
        edit1 = Entry(self,newWindow)
        edit1.place(x = 50, y = 300)
        buttonExample1 = tk.Button(self,newWindow, text = "lancer")
        buttonExample1.place(x = 100, y = 350)
    
#     def interrupteur():
        


fenetre = Tk()

fenetre.title("speed-air cochon")

fenetre.geometry("500x800")


bouRouge = Button(fenetre, text="saucisse", fg="white", bg="red", command = saucisse)

bouVert = Button(fenetre, text="carré de porc", fg="white", bg="red", command = carre_de_porc)

bouOrange = Button(fenetre, text="+", fg="white", bg="blue", command = plus)


# - - - - - C'est sur cette zone qu'on définit une Frame - - - -

zone2 = Frame(fenetre, bg='#777777')

bouBleua = Button(zone2, text="info", fg="white", bg="blue", command = infos)
bouBleub = Button(zone2, text="caméra", fg="white", bg='black', command = camera)
bouBleuc = Button(zone2, text="paramètre", fg="white", bg='gray', command = parametre)


bouNoir = Button(fenetre, text="QUIT", fg="white", bg="black", command = fenetre.destroy)


bouRouge.pack(fill=X, ipady=10, padx=10,pady=10)

bouVert.pack(fill=X, ipady=10, padx=10,pady=10)

bouOrange.pack(fill=X, ipady=20, padx=10,pady=10)


zone2.pack(fill=Y, padx=10,pady=10)

bouBleua.pack(side=LEFT, fill=Y, ipady=30, padx=10,pady=10)

bouBleub.pack(side=LEFT, fill=Y, ipady=30, padx=10,pady=10)

bouBleuc.pack(side=LEFT, fill=Y, ipady=30, padx=10,pady=10)


bouNoir.pack(fill=X, ipady=20, padx=10,pady=10)


fenetre.mainloop()



