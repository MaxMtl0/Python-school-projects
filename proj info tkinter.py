import tkinter as tk
from tkPDFViewer import tkPDFViewer as pdf

def ab():
    def td():
        newWindow1 = tk.Toplevel(fenetre)
        newWindow1.geometry("650x850")
        v1 = pdf.ShowPdf() 
        v1.img_object_li.clear()
        v2 = v1.pdf_view(newWindow1, pdf_location = r"C:/Users/Max/Documents/pyzo/projet info pdf/td.pdf", width = 75, height = 100) 
        v2.pack() 
    
    def tp():
        newWindow1 = tk.Toplevel(fenetre)
        newWindow1.geometry("250x200")
        v1 = pdf.ShowPdf() 
        v1.img_object_li.clear()
        v2 = v1.pdf_view(newWindow1, pdf_location = r"C:/Users/Max/Documents/pyzo/projet info pdf/tp.pdf", width = 75, height = 100) 
        v2.pack() 
    
    def cc():
        newWindow1 = tk.Toplevel(fenetre)
        newWindow1.geometry("250x200")
        v1 = pdf.ShowPdf() 
        v1.img_object_li.clear()
        v2 = v1.pdf_view(newWindow1, pdf_location = r"C:/Users/Max/Documents/pyzo/projet info pdf/cc.pdf", width = 75, height = 100) 
        v2.pack() 
        
    def es():
        newWindow1 = tk.Toplevel(fenetre)
        newWindow1.geometry("250x200")
        v1 = pdf.ShowPdf() 
        v1.img_object_li.clear()
        v2 = v1.pdf_view(newWindow1, pdf_location = r"C:/Users/Max/Documents/pyzo/projet info pdf/es.pdf", width = 75, height = 100) 
        v2.pack() 
    
    def cb():
        newWindow1 = tk.Toplevel(fenetre)
        newWindow1.geometry("250x200")
        v1 = pdf.ShowPdf() 
        v1.img_object_li.clear()
        v2 = v1.pdf_view(newWindow1, pdf_location = r"C:/Users/Max/Documents/pyzo/projet info pdf/cb.pdf", width = 75, height = 100) 
        v2.pack() 
    
    def kholle():
        newWindow1 = tk.Toplevel(fenetre)
        newWindow1.geometry("250x200")
        v1 = pdf.ShowPdf() 
        v1.img_object_li.clear()
        v2 = v1.pdf_view(newWindow1, pdf_location = r"C:/Users/Max/Documents/pyzo/projet info pdf/kholle.pdf", width = 75, height = 100) 
        v2.pack() 
        
    def td3():
        newWindow1 = tk.Toplevel(fenetre)
        newWindow1.geometry("650x850")
        v1 = pdf.ShowPdf() 
        v1.img_object_li.clear()
        v2 = v1.pdf_view(newWindow1, pdf_location = r"C:/Users/Max/Documents/pyzo/projet info pdf/td.pdf", width = 75, height = 100) 
        v2.pack() 
    
    def tp3():
        newWindow1 = tk.Toplevel(fenetre)
        newWindow1.geometry("250x200")
        v1 = pdf.ShowPdf() 
        v1.img_object_li.clear()
        v2 = v1.pdf_view(newWindow1, pdf_location = r"C:/Users/Max/Documents/pyzo/projet info pdf/tp.pdf", width = 75, height = 100) 
        v2.pack() 
    
    def cc3():
        newWindow1 = tk.Toplevel(fenetre)
        newWindow1.geometry("250x200")
        v1 = pdf.ShowPdf() 
        v1.img_object_li.clear()
        v2 = v1.pdf_view(newWindow1, pdf_location = r"C:/Users/Max/Documents/pyzo/projet info pdf/cc.pdf", width = 75, height = 100) 
        v2.pack() 
        
    def es3():
        newWindow1 = tk.Toplevel(fenetre)
        newWindow1.geometry("250x200")
        v1 = pdf.ShowPdf() 
        v1.img_object_li.clear()
        v2 = v1.pdf_view(newWindow1, pdf_location = r"C:/Users/Max/Documents/pyzo/projet info pdf/es.pdf", width = 75, height = 100) 
        v2.pack() 
    
    def cb3():
        newWindow1 = tk.Toplevel(fenetre)
        newWindow1.geometry("250x200")
        v1 = pdf.ShowPdf() 
        v1.img_object_li.clear()
        v2 = v1.pdf_view(newWindow1, pdf_location = r"C:/Users/Max/Documents/pyzo/projet info pdf/cb.pdf", width = 75, height = 100) 
        v2.pack() 
    
    def kholle3():
        newWindow1 = tk.Toplevel(fenetre)
        newWindow1.geometry("250x200")
        v1 = pdf.ShowPdf() 
        v1.img_object_li.clear()
        v2 = v1.pdf_view(newWindow1, pdf_location = r"C:/Users/Max/Documents/pyzo/projet info pdf/kholle.pdf", width = 75, height = 100) 
        v2.pack() 
        
    newWindow = tk.Toplevel(fenetre)
    newWindow.geometry("250x200")
    sujetText = tk.Label(newWindow, text = "Sujets")
    sujetText.pack(side= tk.LEFT)
    correctionText = tk.Label(newWindow, text = "Corrections")
    correctionText.pack(side=tk.RIGHT)
    
    td1 = tk.Button(newWindow,text="TD", fg="white", bg="green", command = td)
    td1.pack(side=tk.LEFT,ipady=10,ipadx=20, padx=20)
    tp1 = tk.Button(newWindow,text="TP", fg="white", bg="green", command = tp)
    tp1.pack(side=tk.LEFT,ipady=10,ipadx=20, padx=20)
    cc1 = tk.Button(newWindow,text="CC", fg="white", bg="green", command = cc)
    cc1.pack(side=tk.LEFT,ipady=10,ipadx=20, padx=20)
    es1 = tk.Button(newWindow,text="ES", fg="white", bg="green", command = es)
    es1.pack(side=tk.LEFT,ipady=10,ipadx=20, padx=20)
    #cb1 = tk.Button(newWindow,text="CB", fg="white", bg="green", command = cb)
    #cb1.pack(side=tk.LEFT,ipady=10,ipadx=20, padx=20)
    kholle1 = tk.Button(newWindow,text="KHOLLE", fg="white", bg="green", command = kholle)
    kholle1.pack(side=tk.LEFT,ipady=10,ipadx=20, padx=20)
    
    td2 = tk.Button(newWindow,text="TD", fg="white", bg="red", command = td3)
    td2.pack(side=tk.RIGHT,ipady=10,ipadx=20, padx=20)
    tp2 = tk.Button(newWindow,text="TP", fg="white", bg="red", command = tp3)
    tp2.pack(side=tk.RIGHT,ipady=10,ipadx=20, padx=20)
    cc2 = tk.Button(newWindow,text="CC", fg="white", bg="red", command = cc3)
    cc2.pack(side=tk.RIGHT,ipady=10,ipadx=20, padx=20)
    es2 = tk.Button(newWindow,text="ES", fg="white", bg="red", command = es3)
    es2.pack(side=tk.RIGHT,ipady=10,ipadx=20, padx=20)
    #cb2 = tk.Button(newWindow,text="CB", fg="white", bg="red", command = cb3)
    #cb2.pack(side=tk.RIGHT,ipady=10,ipadx=20, padx=20)
    kholle2 = tk.Button(newWindow,text="KHOLLE", fg="white", bg="red", command = kholle3)
    kholle2.pack(side=tk.RIGHT,ipady=10,ipadx=20, padx=20)
    
def nab():
    print('e')
    

    

    


fenetre = tk.Tk()

fenetre.title("si-search")

fenetre.geometry("500x700")

abonné = tk.Button(fenetre,text="abonné", fg="white", bg="blue", command = ab)
non_abonné = tk.Button(fenetre,text="non abonné", fg="white", bg="blue", command = nab)
abonné.pack()
non_abonné.pack()
fenetre.mainloop()          #id et mdp pour abonnés