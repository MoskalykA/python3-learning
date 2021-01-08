# Importation de la librairie Tkinter
from tkinter import * 

# Créations d'une variable et définissions d'une instance a la variable
fenetre = Tk()
fenetre.geometry("200x150")

 # Créations d'une variable et définissions d'une instance a la variable
frame = Frame(fenetre)
# Définissions de la positions
frame.pack()

# Créations d'une variable et définissions d'une instance a la variable
button = Button(frame, 
				text = "Button1",
                 fg = "#ecf0f1",
                 bd = 0,
				bg = "#10b981",
				command = quit,
				relief = "groove"
		 )
# Définissions de la positions
button.pack(pady = 5)

# 'Démarrage'
fenetre.mainloop()