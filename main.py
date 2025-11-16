import random
from grille import Grille
from bateau import PorteAvion, Croiseur, Torpilleur, SousMarin

def placer_bateaux(grille):
    bateaux = []
    types = [PorteAvion, Croiseur, Torpilleur, SousMarin]

    for T in types:
        place = False
        while not place:
            ligne = random.randint(0, grille.lignes - 1)
            colonne = random.randint(0, grille.colonnes - 1)
            vertical = random.choice([True, False])
            b = T(ligne, colonne, vertical)
            if grille.ajoute(b):
                bateaux.append(b)
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

    print("Bienvenue dans la bataille navale !")

    while not tous_coules(bateaux, grille):
        print(grille)
        print()
        t = input("Entrez 'ligne colonne' (ou q pour quitter) : ")
        if t == "q":
            return
        try:
            ls, cs = t.split()
            l = int(ls)
            c = int(cs)
        except:
            print("Entrée invalide.\n")
            continue
        try:
            grille.tirer(l, c)
        except:
            print("Hors grille.\n")
            continue

        touche = False
        for b in bateaux:
            if (l, c) in b.positions:
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
