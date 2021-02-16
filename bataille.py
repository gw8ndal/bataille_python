import random
import time
import os

VALEURS = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'VALET', 'DAME', 'ROI', 'AS')
COULEURS = ('COEUR', 'CARREAU', 'TREFLE', 'PIQUE')

jeu = []

jeu1 = []

jeu2 = []

table = []

def creer_jeu():
    for n in VALEURS:
        for c in COULEURS:
            carte = (n, c)
            jeu.append(carte)

    return(jeu)

def melanger(jeu):
    random.shuffle(jeu)
    return(jeu)

def distribuer(jeu):
    jeu1 = jeu[0:len(jeu)//2]
    jeu2 = jeu[len(jeu)//2:-1]
    return(jeu1, jeu2)

def jouer(jeu1, jeu2):
    while len(jeu1) != 0 or len(jeu2) != 0:

        carte1 = jeu1[0]
        jeu1 = jeu1[1:-1]
        carte2 = jeu2[0]
        jeu2 = jeu2[1:-1]
        print('Joueur 1 : ', carte1, 'Joueur 2 : ', carte2)

        table.append(carte1)
        table.append(carte2)
        if VALEURS.index(carte1[0]) > VALEURS.index(carte2[0]):
            jeu1.extend(table)
            jeu2.pop(0)
        if VALEURS.index(carte2[0]) > VALEURS.index(carte1[0]):
            jeu2.extend(table)
            jeu1.pop(0)
        print('table : ',table)
        print('jeu1 : ',jeu1)
        print('jeu2 : ',jeu2)
        os.system('pause')



def demarrer_partie():
    """
    Créer un jeu de carte, mélange les cartes, les distribue en 2 paquets et lance le jeu.
    lancer un jeu
    retourne le tuple jeu1, jeu2
    """
    jeu = creer_jeu()
    jeu = melanger(jeu)
    jeu1, jeu2 = distribuer(jeu)
    return jouer(jeu1, jeu2)

print(demarrer_partie())
