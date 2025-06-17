from tkinter import *
fenetre = Tk()
fenetre.geometry("280x70")

label_1 = Label(fenetre, text="Bienvenue")
label_1.pack()


boutton_quitter = Button(fenetre, text="Quitter", command=fenetre.quit, width=20)
boutton_quitter.pack()


fenetre.mainloop()