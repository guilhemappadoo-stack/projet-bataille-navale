from grille import Grille


def main():
    # 1) créer une grille 5 x 8
    grille = Grille(5, 8)

    while True:
        # 2) afficher la grille
        print(grille)
        print()

        # 3) demander à l'utilisateur les coordonnées
        texte = input("Entrez 'ligne colonne' (ou q pour quitter) : ")

        if texte.lower() == "q":
            print("Fin de la user story.")
            break

        try:
            ligne_str, col_str = texte.split()
            ligne = int(ligne_str)
            col = int(col_str)
        except ValueError:
            print("Entrée invalide. Exemple : 2 3\n")
            continue

        # 4) tirer à l'endroit indiqué
        try:
            grille.tirer(ligne, col)
        except IndexError:
            print("Case en dehors de la grille.\n")
            continue

        # 5) on revient au début de la boucle (affichage puis nouvelle entrée)


if __name__ == "__main__":
    main()
