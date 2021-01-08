# Importation de la librairie Tkinter
from tkinter import * 

# Créations d'une variable et définissions d'une instance a la variable
fenetre = Tk()

# Créations d'une variable et définissions d'une instance a la variable
label = Label(fenetre, text="Hello World")
# Définissions de la positions
label.pack()

# 'Démarrage'
fenetre.mainloop()