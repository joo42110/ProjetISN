from tkinter import *
import csv

def Quitter():
    jeu.destroy()
def Quitter2():
    jeu2.destroy()
    
jeu=Tk()
jeu.geometry('700x400+300+270')


Quitter=Button(jeu, text="Quitter", command=Quitter).grid()
	
monFich = []
	
		
def chargerCSV(a) : 
	with open(a, "r") as file:
		reader= csv.reader(file)
		for row in reader :
			monFich.append(row)		
		file.close()

def VerifRep1():
    global Bonne_Reponse
    if Bonne_Reponse=='1':
        win=0
    else:
        win=1
    suite(win)
    
def VerifRep2():
    global Bonne_Reponse
    if Bonne_Reponse=='2':
        win=0
    else:
        win=1
    suite(win)

def VerifRep3():
    global Bonne_Reponse
    if Bonne_Reponse=='3':
        win=0
    else:
        win=1
    suite(win)

               
def Qsuivant(n):
    global Bonne_Reponse
    Question=StringVar()
    Question.set(monFich[n][0])  
    Rep_1=StringVar()
    Rep_1.set(monFich[n][1])
    Rep_2=StringVar()
    Rep_2.set(monFich[n][2])
    Rep_3=StringVar()
    Rep_3.set(monFich[n][3])
    Bonne_Reponse=monFich[n][4]
    Q=Label(jeu, textvariable=Question).grid()
    R_1=Button(jeu, textvariable=Rep_1, command=VerifRep1).grid()
    R_2=Button(jeu, textvariable=Rep_2, command=VerifRep2).grid()
    R_3=Button(jeu, textvariable=Rep_3, command=VerifRep3).grid()


def suite(w):
    global n,jeu2
    if w==0:
        jeu2=Toplevel()
        jeu2.grab_set()
        s=Button(jeu2,text="suivant",command=Quitter2).grid()
        n+=1
        Label(jeu,text='Gagner').grid()
    else:
        Label(jeu,text='Perdu').grid()
        n+=1

#Qsuivant(n)
        
chargerCSV("ExCSV.csv")
n=0
Qsuivant(0)




jeu.mainloop()
