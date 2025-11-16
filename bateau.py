# bateau.py

from dataclasses import dataclass

@dataclass
class Bateau:
    ligne: int
    colonne: int
    longueur: int = 1
    vertical: bool = False
    marque: str = "⛵"

    @property
    def positions(self):
        """Liste des positions (ligne, colonne) occupées par le bateau."""
        pos = []
        for i in range(self.longueur):
            if self.vertical:
                pos.append((self.ligne + i, self.colonne))
            else:
                pos.append((self.ligne, self.colonne + i))
        return pos

    def coule(self, grille) -> bool:
        """
        Renvoie True si toutes les cases du bateau sont marquées comme touchées
        (caractère 'x') sur la grille.
        """
        from grille import Grille  # import local pour éviter les cycles
        for (l, c) in self.positions:
            idx = grille._index(l, c)
            if grille.grille[idx] != "x":
                return False
        return True


# Sous-classes pour les différents types de bateaux

class PorteAvion(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=4, vertical=vertical, marque="🛳")


class Croiseur(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=3, vertical=vertical, marque="⛴")


class Torpilleur(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=2, vertical=vertical, marque="🚤")


class SousMarin(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=2, vertical=vertical, marque="⚓")
