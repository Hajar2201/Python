""" import random
boules_rouges = [1,2,4,6,7,9,12,13]
boules_bleues = [0,3,5,10,11,14]
nombres = boules_rouges + boules_bleues
mise = float(input("Combien voulez-vous miser :"))
choix = input("Quel est votre choix(N, P, I, R, B) :")
nombre_aleatoire = random.choice(nombres)
print(nombre_aleatoire)
if choix == "N" :
    nombre_choisi = float(input("Saisir un nombre de 0 à 14 :"))
if nombre_choisi == nombre_aleatoire:
    gain = mise * 5
    print(f"Vous avez gagné {gain}.")
else:
    print("Vous ne gagnez rien.")
elif choix == "P":
if nombre_aleatoire % 2 == 0:
    gain = mise * 3
    print(f"Vous avez gagné {gain}.")
else :
    print("Vous ne gagnez rien.")
elif choix == "I":
if nombre_aleatoire % 2 !=0:
    gain = mise * 3
 print(f"Vous avez gagné {gain}.")
else:
print ("Vous ne gagnez rien.")
elif choix == "R" :
if nombre_aleatoire in boules_rouges :
    gain = mise *2
     print(f"Vous avez gagné {gain}.")
else: 
    print ("Vous ne gagnez rien.")
elif choix == "B":
if nombre_aleatoire in boules_bleues:
    gain = mise * 2
     print(f"Vous avez gagné {gain}.")
else :
   print ("Vous ne gagnez rien.")

else :
print() """

import random

boules_rouges = [1, 2, 4, 6, 7, 9, 12, 13]
boules_bleues = [0, 3, 5, 10, 11, 14]
nombres = boules_rouges + boules_bleues

mise = float(input("Combien voulez-vous miser : "))
choix = input("Quel est votre choix (N, P, I, R, B) : ").upper()

nombre_aleatoire = random.choice(nombres)
print(f"Numéro tiré : {nombre_aleatoire}")

gain = 0  # Initialisation du gain

if choix == "N":
    nombre_choisi = int(input("Saisir un nombre de 0 à 14 : "))
    if nombre_choisi == nombre_aleatoire:
        gain = mise * 5
        print(f"Vous avez gagné {gain}.")
    else:
        print("Vous ne gagnez rien.")

elif choix == "P":
    if nombre_aleatoire % 2 == 0:
        gain = mise * 3
        print(f"Vous avez gagné {gain}.")
    else:
        print("Vous ne gagnez rien.")

elif choix == "I":
    if nombre_aleatoire % 2 != 0:
        gain = mise * 3
        print(f"Vous avez gagné {gain}.")
    else:
        print("Vous ne gagnez rien.")

elif choix == "R":
    if nombre_aleatoire in boules_rouges:
        gain = mise * 2
        print(f"Vous avez gagné {gain}.")
    else:
        print("Vous ne gagnez rien.")

elif choix == "B":
    if nombre_aleatoire in boules_bleues:
        gain = mise * 2
        print(f"Vous avez gagné {gain}.")
    else:
        print("Vous ne gagnez rien.")

else:
    print("Choix invalide.")
