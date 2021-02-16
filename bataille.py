import random
import time

nombres = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As')

couleurs = ('Carreau', 'Coeur', 'Pique', 'Trêfle')

jeu = []

joueur1 = []

joueur2 = []


# fonction pour assigner une couleur à chaque carte
def creer_jeu():
    
    for n in nombres:
        for c in couleurs:
            carte = (n, c)
            jeu.append(carte)

    return(jeu)

# fonction pour mélanger le jeu
def melanger_jeu():
    random.shuffle(jeu)
    return(jeu)

# fonction pour distribuer les cartes
def distribuer_jeu():
    joueur1 = jeu[0, len(jeu)//2]
    joueur2 = jeu[len(jeu//2), -1]
    return(joueur1, joueur2)




creer_jeu()
distribuer_jeu()
print('Joueur 1 : ', joueur1)
print('Joueur 2 : ', joueur2)

def jouer():
    for tour in range(len(jeu)//2):
        for carte1 in joueur1:
            for carte2 in joueur2:
                print('Joueur 1 : ', carte1, 'Joueur 2 : ', carte2)
                time.sleep(2)
 

jouer()


#    reste a faire : 
# - fonction pour montrer les cartes une par une
# - redonner la carte a celui qui a joué la plus haute
