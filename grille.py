# grille.py

class Grille:
    """Représente la grille de bataille navale."""

    vide = "∿"  # caractère pour l'eau (case vide)

    def __init__(self, lignes: int, colonnes: int):
        self.lignes = lignes
        self.colonnes = colonnes
        # C * L cases, initialisées avec le caractère vide
        self.grille = [self.vide] * (lignes * colonnes)

    def _index(self, ligne: int, colonne: int) -> int:
        """Convertit (ligne, colonne) en index de la liste."""
        if not (0 <= ligne < self.lignes and 0 <= colonne < self.colonnes):
            raise IndexError("Case en dehors de la grille")
        return ligne * self.colonnes + colonne

    def tirer(self, ligne: int, colonne: int, touche: str = "x") -> None:
        """Marque un tir sur la grille à la position donnée."""
        idx = self._index(ligne, colonne)
        self.grille[idx] = touche

    def ajoute(self, bateau) -> bool:
        """
        Tente d'ajouter un bateau sur la grille.
        Renvoie True si le bateau a été ajouté, False sinon.
        """
        for (l, c) in bateau.positions:
            # hors grille
            if not (0 <= l < self.lignes and 0 <= c < self.colonnes):
                return False
            # déjà occupé
            if self.grille[self._index(l, c)] != self.vide:
                return False

        # Si tout est ok, on place le bateau
        for (l, c) in bateau.positions:
            self.grille[self._index(l, c)] = bateau.marque

        return True

    def __str__(self) -> str:
        """Affiche la grille ligne par ligne."""
        lignes = []
        for l in range(self.lignes):
            start = l * self.colonnes
            end = start + self.colonnes
            lignes.append("".join(self.grille[start:end]))
        return "\n".join(lignes)
