from tkinter import *


#les fonctions
def Quitter():
    Accueil.destroy()

def Jouer():
    import fonctionPythonChargerCSV
    monFich= []
    fonctionPythonChargerCSV.chargerCSV("ExCSV.csv")
    print(monFich)
    Accueil.destroy()

def Regles():
    fich_regles=open('fichierRegles.txt','r')
    f_regles=Toplevel() #cree une fenetre au dessus de la premiere
    f_regles.grab_set() #s'assure "d'attraper" les commandes clavier et souris
    f_regles.geometry('700x400+300+270')
    a=Button(f_regles,text='Fermer fenÃªtre secondaire !',command=f_regles.destroy)
    a.pack()
    rules=fich_regles.read()
    print(rules)
    Label(f_regles, text=rules).pack()

def Page_1():
    global Accueil
    #Creation de la fenetre d'accueil
    Accueil=Tk()
    Accueil.title('Accueil')
    Accueil.geometry('700x400+300+270')
    Accueil.configure(bg="white")

    #Creation des boutons
    Button(Accueil,text="Quitter", command=Quitter,relief=RIDGE, bg='red', fg="green",activebackground="white").grid(row=5, column=10,sticky='nesw')
    Button(Accueil,text="Règles du jeu", command=Regles,relief=RIDGE, bg='red', fg="green",activebackground="white", width=10).grid(row=4, column=4)
    Button(Accueil,text="Jouer", command=Jouer,relief=RIDGE, bg='red', fg="green",activebackground="white", width = 10).grid(row=4, column=3)

    #lABEL PSEUDO
    Taille="-size 20"
    Indication=Label(Accueil,text="Entrez votre Pseudo",bg="white",font=Taille,fg='red').grid(row=1, column=2,columnspan=3,sticky='nesw')

    taille2="-size 30"
    Nom=StringVar()
    Pseudo=Entry(Accueil,textvariable=Nom,bg="#3FC425", font=taille2).grid(row=2,column=2,columnspan=3,sticky='nesw')

    #Image cote
    Gauche=PhotoImage(file="Rideau.gif")
    canvas=Canvas(Accueil,width=121, height=400,bg="white")
    canvas.create_image(0,0, anchor=NW, image=Gauche)
    canvas.grid(row=1,rowspan=5, column=1,sticky='nesw')

    Droite=PhotoImage(file="Rideau_d.gif")
    canvas=Canvas(Accueil,width=121, height=370,bg="white")
    canvas.create_image(0,0, anchor=NW, image=Droite)
    canvas.grid(row=1,rowspan=4, column=10,sticky='nesw')
    #Image milieu
    Came=PhotoImage(file="Mascotte.gif")
    canvas=Canvas(Accueil,width=220, height=249,bg="white")
    canvas.create_image(0,0, anchor=NW, image=Came)
    canvas.grid(row=3,rowspan=3, column=2, sticky='nesw')

    bulle=PhotoImage(file="bulle.gif")
    canvas=Canvas(Accueil,width=210, height=100,bg="white")
    canvas.create_image(0,0, anchor=NW, image=bulle)
    canvas.grid(row=3, column=3, columnspan=2,sticky='nesw')
    Accueil.mainloop()


Page_1()




