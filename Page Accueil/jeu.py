from tkinter import *
import PIL.Image as img
import PIL.ImageTk as imgTk

jeu=Tk()
jeu.geometry('700x400+300+270')

niveau = img.open('niveau.png')
niveauPIL=imgTk.PhotoImage(niveau)
(l,h) = niveau.size

canvasNiv= Canvas(jeu, width=700, height=150)
canvasNiv.create_image(0,0,anchor=NW, image=niveauPIL)
canvasNiv.grid(row=2)

Canvas(jeu, width=700, height=250).grid(row=1)

########
jeu.mainloop()
