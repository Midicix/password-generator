from tkinter import *
import tkinter.messagebox
import tkinter as tk
from random import randint

# Création de la fenêtre

##########################################
#color :
couleur_fond = "#555555" #On peut mettre les couleurs en hexadécimal, par exemple, ici, mettre "gray" ou "#5FB691"
couleur_titre = "black"
police_lettre = "Arial 12 bold"

#dimension
hauteur_page = 500
largeur_page = 500

##########################################

fenetre = Tk()
canvas = Canvas(fenetre, width=hauteur_page, height=largeur_page, bg = couleur_fond, highlightthickness=0)
canvas.pack(padx=0, pady=0)
fenetre.geometry('500x500')
fenetre.config(bg=couleur_fond)
fenetre.title("Générateur de mot de passe sécurisé")


confirmation_copie = canvas.create_text(380, 280, text="",
                fill=couleur_titre,
                font=police_lettre)

btn_generer = Button(fenetre, height=1, width=10, text="Créer", command=lambda: generer())
btn_generer.pack()
btn_copier = Button(fenetre, height=1, width=10, text="Copier", command=lambda: copier())
btn_copier.pack()

saisie = tkinter.Entry()
saisie.config(state = tkinter.NORMAL)

saisie_fenetre = canvas.create_window(250, 250, window=saisie)
btn_fenetre = canvas.create_window(250, 280, window=btn_generer)
"""btn_fenetre = canvas.create_window(465, 10, window=btn_copier)"""
btn_fenetre = canvas.create_window(380, 250, window=btn_copier)

liste_lettre_maj = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
liste_lettre_min = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
liste_chiffre = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def copier():
    fenetre.clipboard_clear()
    fenetre.clipboard_append(saisie.get())
    canvas.itemconfig(confirmation_copie, text="copié !")

def generer():
    global saisie
    canvas.itemconfig(confirmation_copie, text="")
    saisie.delete(0,len(saisie.get()))
    var_lettre = 0
    var_chiffre = 0
    text = ""
    compteur_while = 0
    while compteur_while <= 8 :
        compteur = randint(1,3)
        compteur_while += 1
        if compteur == 1 :
            var_lettre = randint(0,25)
            text += liste_lettre_maj[var_lettre]
        if compteur == 2 :
            var_lettre = randint(0,25)
            text += liste_lettre_min[var_lettre]
        if compteur == 3 :
            var_chiffre = randint(0,9)
            text += liste_chiffre[var_chiffre]
    saisie.insert(0, text)
