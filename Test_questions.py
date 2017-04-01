from tkinter import *
import csv

def Quitter():
    jeu.destroy()



jeu=Tk()
jeu.geometry('700x400+300+270')

##fname = "CSV.csv"
##file = open(fname,'r')

Button(jeu, text="Quitter", command=Quitter).grid()

with open("ExCSV.csv", "r") as file:
    reader= csv.reader(file)
    #for row in reader:
##        liste=StringVar()
##        liste.set(row[1])
##        Question=Button(jeu, textvariable=liste)
##        Question.grid()
    for row in reader:          #transformer liste en chaine pour faire split
        liste=[]
        liste.append(row)
        print(liste)
        essai="-".join(liste)
        print(essai)
        q=liste[0]
        print(q)
        r1=liste[1]
        r2=liste[2]
        r3=liste[3]
        print(r1)

##try:
##    #
##    # Utiliser ''DictReader'' au lieu de ''reader''...
##    #
##    reader = csv.reader(file)
## 
##    #
##    # ... permet de lire les lignes de données dans un *dictionnaire*
##    #
##    for row in reader:
##        #print(row[1])
##        Question=Label(jeu, textvariable=row[1])
##        Question.grid()

#finally:
   # file.close()






######
jeu.mainloop()
