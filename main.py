# main.py

import random
from grille import Grille
from bateau import PorteAvion, Croiseur, Torpilleur, SousMarin, Bateau

def peut_placer(grille: Grille, bateau: Bateau) -> bool:
    """Vérifie si un bateau peut être placé sur la grille sans débordement ni chevauchement."""
    for (l, c) in bateau.positions:
        if not (0 <= l < grille.lignes and 0 <= c < grille.colonnes):
            return False
        idx = grille._index(l, c)
        if grille.grille[idx] != grille.vide:
            return False
    return True

def placer_bateaux_aleatoirement(grille: Grille):
    bateaux = []
    types = [PorteAvion, Croiseur, Torpilleur, SousMarin]

    for cls in types:
        place = False
        while not place:
            vertical = bool(random.getrandbits(1))
            # on essaye toutes les positions possibles
            positions_valides = []
            for l in range(grille.lignes):
                for c in range(grille.colonnes):
                    b = cls(l, c, vertical=vertical)
                    if peut_placer(grille, b):
                        positions_valides.append(b)

            if not positions_valides:
                # si aucune position possible avec cette orientation, on change d’orientation
                vertical = not vertical
                for l in range(grille.lignes):
                    for c in range(grille.colonnes):
                        b = cls(l, c, vertical=vertical)
                        if peut_placer(grille, b):
                            positions_valides.append(b)

            if positions_valides:
                b = random.choice(positions_valides)
                grille.ajoute(b)
                bateaux.append(b)
                place = True

    return bateaux

def tous_coules(bateaux, grille):
    return all(b.coule(grille) for b in bateaux)

def main():
    g = Grille(8, 10)
    bateaux = placer_bateaux_aleatoirement(g)
    nb_coups = 0

    print("Bienvenue dans la bataille navale !")

    while not tous_coules(bateaux, g):
        print(g)
        print("Entrez une ligne et une colonne pour tirer (ex: '2 3'), ou 'q' pour quitter :")
        s = input("> ")
        if s.lower() == "q":
            print("Abandon du jeu.")
            return

        try:
            l_str, c_str = s.split()
            l = int(l_str)
            c = int(c_str)
            g.tirer(l, c, touche="x")
            nb_coups += 1

            # Vérifier si on a touché un bateau et/ou coulé
            touche = False
            for b in bateaux:
                if (l, c) in b.positions:
                    touche = True
                    print("Touché !")
                    if b.coule(g):
                        print("Coulé !")
                        # on révèle le bateau avec sa marque
                        for (ll, cc) in b.positions:
                            idx = g._index(ll, cc)
                            g.grille[idx] = b.marque
                    break

            if not touche:
                print("Plouf dans l'eau…")

        except Exception:
            print("Entrée invalide. Format attendu : 'ligne colonne'.")

    print(g)
    print(f"Bravo ! Tous les bateaux sont coulés en {nb_coups} coups.")

if __name__ == "__main__":
    main()
