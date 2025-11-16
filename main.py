import random

from grille import Grille
from bateau import PorteAvion, Croiseur, Torpilleur, SousMarin


def placer_bateaux(grille):
    bateaux = []
    types = [PorteAvion, Croiseur, Torpilleur, SousMarin]

    for TypeBateau in types:
        place = False
        while not place:
            ligne = random.randint(0, grille.lignes - 1)
            colonne = random.randint(0, grille.colonnes - 1)
            vertical = random.choice([True, False])

            bateau = TypeBateau(ligne, colonne, vertical)

            if grille.ajoute(bateau):
                bateaux.append(bateau)
                place = True

    return bateaux


def tous_coules(bateaux, grille):
    for b in bateaux:
        if not b.coule(grille):
            return False
    return True


def main():
    grille = Grille(8, 10)

    bateaux = placer_bateaux(grille)

    print("Bataille navale ")

    while not tous_coules(bateaux, grille):
        print(grille)
        print()
        texte = input("Entrez 'ligne colonne' pour tirer (ou q pour quitter) : ")

        if texte.lower() == "q":
            print("Vous avez quitté la partie.")
            return

        try:
            ligne_str, col_str = texte.split()
            ligne = int(ligne_str)
            col = int(col_str)
        except ValueError:
            print("Entrée invalide. Exemple : 2 3\n")
            continue

        try:
            grille.tirer(ligne, col)
        except IndexError:
            print("Case en dehors de la grille.\n")
            continue

        touche = False
        for b in bateaux:
            if (ligne, col) in b.positions:
                touche = True
                print("Touché !")
                if b.coule(grille):
                    print("Coulé !")
                break

        if not touche:
            print("Plouf, dans l'eau...")

        print()

    print(grille)
    print("Bravo, tous les bateaux sont coulés !")


if __name__ == "__main__":
    main()
