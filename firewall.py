#coding:utf-8

from cgitb import text
from hashlib import new
from tkinter import *
import tkinter
from tkinter import ttk
from tkinter.tix import InputOnly
from tokenize import String
from turtle import pos
from os import *
#initialisation de l'objet fenêtre mainapp
mainapp=Tk()

""" centrage de la fenêtre par rapport à l'écran"""
largeur_ecran=mainapp.winfo_screenwidth()
hauteur_ecran=mainapp.winfo_screenheight()
largeur_fenetre=800
hauteur_fenetre=600

posX=int((largeur_ecran/2)-(largeur_fenetre/2))
posY=int((hauteur_ecran/2)-(hauteur_fenetre/2))

geo="{}x{}+{}+{}".format(largeur_fenetre,hauteur_fenetre,posX,posY)
mainapp.geometry(geo)
mainapp.resizable(width=False,height=False)#taille fenêtre non modifiable
mainapp.title("Firewall")#nom de la fenêtre 

premier_frame=tkinter.LabelFrame(mainapp,text="terminal",width=400 , height=200)#frame pour le petit terminal
chemin=tkinter.StringVar()
chemin.set("firewall>")
chemin_label=tkinter.Label(premier_frame,textvariable=chemin)

log =tkinter.StringVar()
log.set("Firewall is presently Off")
log_label=tkinter.Label(premier_frame,textvariable=log)

chemin_label.grid(row=0 ,column=0)
log_label.grid(row=0 , column=1)

#definition de la méthode à utiliser en cas de changements de la variable rendu
#observateur update_status
def update_status(*args):
    if rendu.get():
        log.set("the Firewall is On")
    else:
        log.set("the firewall is Off")

def ligne_terminale():
    route=tkinter.Label(text="firewall#")   
    action=tkinter.Label(textvariable=log)
     


#fonction au clic du boutton +
def ajout_formulaire():
    form=Tk()
    form.geometry("350x450")
    form.title("Ajout de règle")
    form.resizable(width=False,height=False)



    #élément du formulaire(widget)
    def tracage(*args):
        if menu.get()=="INPUT":
            print("j'ai vu un INPUT")
        elif menu.get()=="OUTPUT":
            print("j'ai vu un OUTPUT")
        else:
            print("j'ai vu un FORWARD")
    
    methode_liste=["INPUT","OUTPUT","FORWARD"]
    menu=tkinter.StringVar()
    menu.trace_variable("w",tracage)
    methode_A=ttk.Combobox(form,values=methode_liste,textvariable=menu)
    label_underscore_A=tkinter.Label(form,text="méthode")


    #affichage du formulaire d'ajout de règle
    label_underscore_A.grid(row=0,column=3)
    methode_A.grid(row=0,column=4)

    form.mainloop()
    


#variable pour observer l'action de l'objet radio button       
rendu=tkinter.IntVar()
rendu.trace_variable("w", update_status)
On = tkinter.Radiobutton(mainapp,text ="On",value=1,variable=rendu)
Off = tkinter.Radiobutton(mainapp,text="Off", value=0,variable=rendu)



#button d'action
button_nvl_règle = tkinter.Button(mainapp,text="+",command=ajout_formulaire)
button_supr_regle= tkinter.Button(mainapp,text="-")

#affichage des éléments
On.grid(row=0 , column=3)
Off.grid(row=0 , column=4)
premier_frame.grid(row=7 ,column=7)
button_nvl_règle.grid(row=3 ,column=4)
button_supr_regle.grid(row=3 ,column=5)

#affichage de la fenêtre

mainapp.mainloop()


