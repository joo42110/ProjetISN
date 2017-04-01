from tkinter import *

fenetre1 = Tk()
fenetre1.title('Fenêtre principale')

def Quitter():
    fenetre1.destroy()

def NouvelleFenetre():
    fenetre2=Toplevel() #crée une fenêtre au dessus de la première
    fenetre2.grab_set() #s'assure "d'attraper" les commandes clavier et souris
    a=Button(fenetre2,text='Fermer fenêtre secondaire !',command=fenetre2.destroy)
    a.pack()

BoutonQuitter=Button(fenetre1,text="Quitter", command=Quitter)
BoutonQuitter.pack(side=BOTTOM, pady=10)

b = Button(fenetre1, text='Nouvelle fenêtre', command=NouvelleFenetre)
b.pack()

fenetre1.mainloop()
