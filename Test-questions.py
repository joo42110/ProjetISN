from Tkinter import *
import csv

def Quitter():
    jeu.destroy()



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
for row in monFich :
	print(row)
	
	
	
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
