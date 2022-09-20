#!/usr/bin/python3.10
#-*-coding:utf-8-*-

from random import *
from math import *

gain = 0
compte = 2000
print("Bienvenue dans notre super casino !")
while 1:
    print("Vous avez", compte,"euros sur votre compte.")
    nbr = float(input("Choisissez un numéro compris entre 0 et 49: "))
    while nbr > 49 or nbr < 0:
        nbr = float(input("Nous avons demandé un nombre entre 0 et 49: "))
    som = float(input("Combien d'argent voulez-vous parier ? "))
    ngagnant = randrange(50)
    if nbr == ngagnant:
        gain = ceil(3*som)
        compte += gain
        print("Vous avez gagné", gain, "euros.")
    elif nbr%2 == ngagnant%2:
        gain = ceil(som/2)
        compte += gain
        print("Votre numéro possède la même couleur que le numéro gagnant, vous avez gagné", gain, "euros.")
    else:
        compte -= som
        print("Dommage, vous avez perdu", som, "euros.")
    print("Votre solde s'élève à",compte,"euros.")
    jouer = input("Voulez-vous continuer à jouer [oui/non] ? ")
    if jouer == "non":
        print("Merci et à bientôt !")
        break
    if compte == 0:
        print("Vous êtes ruiné, dehors !!!")
        break

