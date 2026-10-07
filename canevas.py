from tkinter import * 

def viande():
    print('viande')
root = Tk()
root.geometry('1000x800')
root.title("speed-air cochon")

monCanvas = Canvas(root, width=950, height=750, bg='ivory')
monCanvas.place(x=25,y=25)

label = Label(root, text="Interface") 
label.place(x=0,y=0) 
btn = Button(root, text ="Fermer", command = root.destroy) 
btn.place(x=920,y=25)

bouRouge = Button(root, text="FILE", fg="white", bg="red", command = viande)
bouVert = Button(root, text="EDIT", fg="white", bg="green", command = viande)
bouBleu = Button(root, text="RUN", fg="white", bg="blue", command = viande)
bouNoir = Button(root, text="QUIT", fg="white", bg="black", command = viande)

bouRouge.place(x=30,y=30)
bouVert.place(x=60,y=30)
bouBleu.place(x=90,y=30)
bouNoir.place(x=120,y=30)

root.mainloop()