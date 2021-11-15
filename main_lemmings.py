# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 15:22:53 2021

@author: jeffa
"""

#modules
from tkinter import *
from random import randint
from time import sleep

from lemmings_class import *

#creation de la fenetre
Mafenetre=Tk()
Mafenetre.geometry('500x500')
#zone de dessin
can1=Canvas(Mafenetre,bg="white",width=500,height=500)
can1.place(x=0,y=0)
# =============================================================================
# creation d'un niveau : images - matrice - dictionnaire
# =============================================================================
caseciel=PhotoImage(file="ciel.gif")
caseportail=PhotoImage(file="portail.gif")
casemur=PhotoImage(file="mur.gif")
caseangleg=PhotoImage(file="angleg.gif")
caseangled=PhotoImage(file="angled.gif")
casemilieu=PhotoImage(file="milieu.gif")
casesortie=PhotoImage(file="sortie.gif")
Pac_droite=PhotoImage(file="heroD.gif")
Pac_gauche=PhotoImage(file="heroG.gif")
#astuce : les cases de sortie sont toujours nommées S
L8=["MX","C","C","C","C","C","C","MX","C","MX"]
L9=["MX","C","AG","AD","C","C","C","MX","C","MX"]
L0=["MX","C","C","C","C","C","C","MX","C","MX"]
L1=["MX","AG","M","M","AD","C","C","MX","C","MX"]
L2=["MX","C","C","C","C","C","C","MX","C","MX"]
L3=["MX","AG","AD","PX","AG","M","M","AD","C","MX"]
L4=["MX","C","C","C","C","C","C","C","C","MX"]
L5=["MX","C","AG","M","M","M","M","M","AD","MX"]
L6=["MX","C","C","C","C","C","C","C","C","MX"]
L7=["MX","AG","M","M","M","M","M","AD","S","MX"]
ma_matrice=[L8,L9,L0,L1,L2,L3,L4,L5,L6,L7]

dico={"C":caseciel,"PX":caseportail,"MX":casemur,"S":casesortie,"M":casemilieu,"AG":caseangleg,"AD":caseangled}


niveau1 = Jeu(ma_matrice,dico,can1,["MX","PX","AG","AD","M"])
niveau1.dessine_matrice()
perso1 = Personnage(niveau1,1,0,1,Pac_droite,Pac_gauche)
perso1.affiche_lem()
niveau1.ajoute_liste_perso(perso1)



def deplace(perso):
    """deplace un perso en suivant les règles du jeu lemmings"""
    if niveau1.get_case_bas(perso) == "S":
        niveau1.changement_nature_case(perso)
        perso.efface_image()
        niveau1.enleve_liste_perso(perso)
    else:
        if niveau1.get_case_bas(perso)=="PX":
           perso.efface_image()
           niveau1.enleve_liste_perso(perso)
           n_perso = Personnage(niveau1,9,0,1,Pac_droite,Pac_gauche)
           n_perso.affiche_lem()
           niveau1.ajoute_liste_perso(n_perso)
           niveau1.changement_nature_case(perso)
        else:
            if niveau1.get_nature_case_dessous(perso) == True:
                niveau1.changement_nature_case(perso)
                perso.deplace_bas()
                niveau1.changement_nature_case(perso)
            elif perso.get_direction() == 0 and niveau1.get_nature_case_droite(perso) == True:
                niveau1.changement_nature_case(perso)
                perso.deplace_droite()
                niveau1.changement_nature_case(perso)
            elif perso.get_direction() == 1 and niveau1.get_nature_case_gauche(perso) == True:
                niveau1.changement_nature_case(perso)
                perso.deplace_gauche()
                niveau1.changement_nature_case(perso)
            elif perso.get_direction() == 0:
                perso.set_direction(1)
            elif perso.get_direction() == 1:
                perso.set_direction(0)
        
            
        
#boucle du jeu qui finit par Mafenetre.update()
compteur = 0
c=0
while niveau1.get_liste_perso() != []:
    sleep(0.5)
    for elt in niveau1.get_liste_perso() :
        deplace(elt)
    if compteur<40 and compteur%4==0:
        x = randint(1,6)
        n_perso = Personnage(niveau1,x,0,1,Pac_droite,Pac_gauche)
        n_perso.affiche_lem()
        niveau1.ajoute_liste_perso(n_perso)
    if c==0:
        Pac_droite=PhotoImage(file="heroD.gif")
        Pac_gauche=PhotoImage(file="heroG.gif")
    else:
        Pac_droite=PhotoImage(file="heroD1.gif")
        Pac_gauche=PhotoImage(file="heroG1.gif")
    compteur += 1
    c = randint(0,1)
    

        
    Mafenetre.update()

        
#lancement de la boucle tkinter       
Mafenetre.mainloop()

        