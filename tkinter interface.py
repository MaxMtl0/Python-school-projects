from tkinter import *  

def change_label_number():
    counter = int(str(labelExample['text']))
    counter += 1
    labelExample.config(text=str(counter))
    
def clic():
    print ('Clic gauche sur le bouton')
    
def boutonFourreTout():
    return(0)
    
root = Tk()
root.geometry('1000x800')

#text affiché sur le shell
button = tk.Button(root, text = 'toto', command = clic)
button.grid(row=0,column=0)

#addition
labelExample = tk.Button(root, text="0")
buttonExample = tk.Button(root, text="Increase", width=30, command=change_label_number)
buttonExample.grid(row=1,column=1)
labelExample.grid(row=2,column=2)


#text
label = Label(root, text="Hello World") 
label.grid(row=5,column=5)

# bouton de sortie
btn = Button(root, text ="Fermer", command = root.destroy) 
btn.grid(row=6,column=6)
#couleur
bouRouge = Button(root, text="FILE", fg="white", bg="red", command = boutonFourreTout)
bouVert = Button(root, text="EDIT", fg="white", bg="green", command = boutonFourreTout)
bouBleu = Button(root, text="RUN", fg="white", bg="blue", command = boutonFourreTout)
bouNoir = Button(root, text="QUIT", fg="white", bg="black", command = boutonFourreTout)


bouRouge.grid(row=1,column=7)
bouVert.grid(row=2,column=7)
bouBleu.grid(row=3,column=7)
bouNoir.grid(row=4,column=7)
root.mainloop()