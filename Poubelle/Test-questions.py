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
	for row in reader:
		liste=[]
		liste.append(row)
		print(liste)
		chaine="-".join(liste[0])
		print(chaine)
		lst=chaine.split("-")
		q=StringVar()
		q.set(lst[0])
		#print(q)
		Question=Label(jeu, textvariable=q)
		Question.grid()
		r1=StringVar()  
		r1.set(lst[1])
		r2=StringVar() 
		r2.set(lst[2])
		r3=StringVar() 
		r3.set(lst[3])
		Button(jeu, textvariable=r1).grid()
		Button(jeu, textvariable=r2).grid()
		Button(jeu, textvariable=r3).grid()
	file.close()
#try:
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
        #Question=Label(jeu, textvariable=row[1])
        #Question.grid()

	#finally:
	#	file.close()






######
jeu.mainloop()
