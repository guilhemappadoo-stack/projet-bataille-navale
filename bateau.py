class Bateau:
    def __init__(self, ligne, colonne, longueur=1, vertical=False, marque="B"):
        self.ligne = ligne
        self.colonne = colonne
        self.longueur = longueur
        self.vertical = vertical
        self.marque = marque

    @property
    def positions(self):
        resultat = []
        for i in range(self.longueur):
            if self.vertical:
                resultat.append((self.ligne + i, self.colonne))
            else:
                resultat.append((self.ligne, self.colonne + i))
        return resultat

    def coule(self, grille):
        for (l, c) in self.positions:
            index = grille._index(l, c)
            if grille.grille[index] != "x":
                return False
        return True


class PorteAvion(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=4, vertical=vertical, marque="P")


class Croiseur(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=3, vertical=vertical, marque="C")


class Torpilleur(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=2, vertical=vertical, marque="T")


class SousMarin(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=2, vertical=vertical, marque="S")
