import tkinter as tk
import tkinter.ttk as ttk

CHOIX = ["oui", "non", "peut-être"]
VALEURS = ['Lundi', 'Mardi', 'Mercredi',
           'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']


class DemoWidget(tk.Frame):

    def __init__(self, root):
        super().__init__(root)
        self._create_gui()
        self.pack()

    def _create_gui(self):
        label = tk.Label(self, text="Un message")
        label.grid(column=0, row=0)

        text = tk.Entry(self)
        text.grid(column=1, row=0, columnspan=2)

        label = tk.Label(self, text="Un choix")
        label.grid(column=0, row=1)

        combo = ttk.Combobox(self, text="choix", values=VALEURS)
        combo.grid(column=1, row=1, columnspan=2)

        for i, rb_label in enumerate(CHOIX):
            rb = ttk.Radiobutton(self, text=rb_label, value=i)
            rb.grid(column=i, row=2)

        checkButton = ttk.Checkbutton(self, text="Accepter les conditions")
        checkButton.grid(column=0, row=3, columnspan=3)

        button = tk.Button(self, text="Fermer", command=app.destroy)
        button.grid(column=1, row=4)


app = tk.Tk()
app.title("Demo Widgets")
DemoWidget(app)
app.mainloop()
