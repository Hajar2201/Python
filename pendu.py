import mots  # Importation du fichier mots.py

# Choisir un mot depuis mots.py
mot_a_deviner = mots.choisir_mot()

# Initialisation du jeu
mot_cache = ["_"] * len(mot_a_deviner)
tentatives = 6
lettres_trouvees = []
lettres_fausses = []

print("🎮 Bienvenue dans le jeu du Pendu ! 🎮")
print(" ".join(mot_cache))

while tentatives > 0 and "_" in mot_cache:
    lettre = input("\n Devinez une lettre : ").lower()

    # Vérifier si la lettre a déjà été proposée
    if lettre in lettres_trouvees or lettre in lettres_fausses:
        print("Vous avez déjà essayé cette lettre !")
        continue

    # Vérifier si la lettre est dans le mot
    if lettre in mot_a_deviner:
        print("✅ Bien joué ! La lettre est dans le mot.")
        lettres_trouvees.append(lettre)

        # Remplacement des "_" par la lettre trouvée
        for i in range(len(mot_a_deviner)):
            if mot_a_deviner[i] == lettre:
                mot_cache[i] = lettre
    else:
        print("❌ Mauvaise réponse !")
        tentatives -= 1
        lettres_fausses.append(lettre)
        print(f"Il vous reste {tentatives} tentatives.")

    print(" ".join(mot_cache))

# Fin du jeu
if "_" not in mot_cache:
    print("\n🎉 Félicitations ! Vous avez trouvé le mot :", mot_a_deviner)
else:
    print("\n💀 Vous avez perdu ! Le mot était :", mot_a_deviner)
