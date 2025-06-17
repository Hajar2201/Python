import random

# Liste de mots 
liste_mots = ["python", "raphael","ordinateur", "nourriture","programmation", "developpeur", "jeu", "intelligence", "amour","pique nique","telephone","chocolat","fruits"]

# Fonction pour choisir un mot aléatoirement dans la liste de mots ci dessus
def choisir_mot():
    return random.choice(liste_mots)
