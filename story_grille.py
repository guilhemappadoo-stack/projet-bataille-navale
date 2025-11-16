# story_grille.py
#
# User Story : "Plouf dans l'eau"
# Utilisateur : un joueur
# Story : On veut pouvoir gérer les tirs de l'adversaire.
#
# Actions :
#   1. créer une grille à 5 lignes et 8 colonnes
#   2. afficher la grille à l'écran
#   3. demander à l'utilisateur de rentrer deux coordonnées x et y
#   4. tirer à l'endroit indiqué sur la grille
#   5. retour en 2
#
# ⚠️ Note :
# Les lignes qui dépendent de méthodes non encore codées dans Grille
# sont marquées comme "non encore fonctionnelles" pour respecter l'énoncé.

from grille import Grille


def main():
    # 1) Créer une grille 5x8
    grille = Grille(5, 8)

    while True:
        # 2) Afficher la grille
        print(grille)   # OK : __str__ doit fonctionner

        # 3) Demander les coordonnées au joueur
        saisie = input("Entrez deux coordonnées 'ligne colonne' (ou q pour quitter) : ")

        if saisie.lower() == "q":
            print("Fin de la user story.")
            break

        try:
            x_str, y_str = saisie.split()
            x = int(x_str)
            y = int(y_str)
        except:
            print("Format invalide. Essayez : 2 3\n")
            continue

        # 4) Tirer sur cette case
        # ⚠️ Cette ligne fonctionne seulement si la méthode tirer() a été programmée
        try:
            grille.tirer(x, y)  # si pas encore codé → "non encore fonctionnelle"
        except Exception as e:
            print("Erreur lors du tir (méthode tirer peut-être non codée) :", e)

        print()  # saut de ligne pour l'affichage


if __name__ == "__main__":
    main()
