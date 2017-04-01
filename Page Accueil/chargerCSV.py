from tkinter import *
import csv

def Quitter():
    jeu.destroy()
    
def Reponse_1():
    if r[1]==r[4]:
        print("okeeeeyyyyy")
    else:
        print("nooooon")


jeu=Tk()
jeu.geometry('700x400+300+270')

##fname = "CSV.csv"
##file = open(fname,'r')

Button(jeu, text="Quitter", command=Quitter).grid()
	
monFich = []
	
		
def chargerCSV(a) : 
	with open(a, "r") as file:
		reader= csv.reader(file)
		for row in reader :
			monFich.append(row)		
		file.close()

chargerCSV("ExCSV.csv")
print(monFich)
for liste in monFich :
    Label(jeu, text=liste[0]).grid()
    Button(jeu, text=liste[1], command=Reponse_1).grid()
    Button(jeu, text=liste[2]).grid()
    Button(jeu, text=liste[3]).grid()


	
#try:
##    #
##    # Utiliser ''DictReader'' au lieu de ''reader''...
##    #
##    reader = csv.reader(file)
## 
##    #
##    # ... permet de lire les lignes de donnees dans un *dictionnaire*
##    #
##    for row in reader:
##        #print(row[1])
        #Question=Label(jeu, textvariable=row[1])
        #Question.grid()

	#finally:
	#	file.close()






######
jeu.mainloop()
