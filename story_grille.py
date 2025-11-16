# User Story : "Plouf dans l'eau"

from grille import Grille

def main():
    grille = Grille(5, 8)

    while True:
        print(grille)
        print()

        texte = input("Entrez 'ligne colonne' (ou q pour quitter) : ")

        if texte.lower() == "q":
            print("Fin de la user story.")
            break

        try:
            ligne_str, col_str = texte.split()
            ligne = int(ligne_str)
            col = int(col_str)
        except:
            print("Entrée invalide.\n")
            continue

        try:
            grille.tirer(ligne, col)
        except:
            print("Erreur : hors grille.\n")
            continue

if __name__ == "__main__":
    main()
