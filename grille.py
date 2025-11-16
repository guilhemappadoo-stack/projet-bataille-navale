class Grille:
    def __init__(self, lignes, colonnes):
        self.lignes = lignes
        self.colonnes = colonnes
        self.vide = "."
        self.grille = [self.vide] * (lignes * colonnes)

    def _index(self, ligne, colonne):
        return ligne * self.colonnes + colonne

    def tirer(self, ligne, colonne, marque="x"):
        index = self._index(ligne, colonne)
        self.grille[index] = marque

    def ajoute(self, bateau):
        for (l, c) in bateau.positions:
            if l < 0 or l >= self.lignes or c < 0 or c >= self.colonnes:
                return False
            index = self._index(l, c)
            if self.grille[index] != self.vide:
                return False
        for (l, c) in bateau.positions:
            index = self._index(l, c)
            self.grille[index] = bateau.marque
        return True

    def __str__(self):
        lignes = []
        for l in range(self.lignes):
            debut = l * self.colonnes
            fin = debut + self.colonnes
            lignes.append("".join(self.grille[debut:fin]))
        return "\n".join(lignes)
