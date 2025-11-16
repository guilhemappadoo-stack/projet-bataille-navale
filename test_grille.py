from grille import Grille
from bateau import Bateau


def test_init_grille():
    g = Grille(5, 8)
    assert g.lignes == 5
    assert g.colonnes == 8
    assert len(g.grille) == 5 * 8
    assert all(case == g.vide for case in g.grille)


def test_tirer():
    g = Grille(3, 3)
    g.tirer(1, 2)
    index = 1 * g.colonnes + 2
    assert g.grille[index] == "x"


def test_str_grille():
    g = Grille(2, 3)
    texte = str(g)
    lignes = texte.split("\n")
    assert len(lignes) == 2
    assert lignes[0] == g.vide * 3
    assert lignes[1] == g.vide * 3


def test_ajoute_bateau():
    g = Grille(2, 3)
    b = Bateau(1, 0, longueur=2, vertical=False, marque="B")
    ok = g.ajoute(b)
    assert ok is True

    index0 = g._index(1, 0)
    index1 = g._index(1, 1)
    assert g.grille[index0] == "B"
    assert g.grille[index1] == "B"
