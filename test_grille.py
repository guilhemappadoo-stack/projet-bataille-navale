# test_grille.py

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
    idx = 1 * g.colonnes + 2
    assert g.grille[idx] == "x"

def test_str_grille():
    g = Grille(2, 3)
    attendu = "\n".join([
        g.vide * 3,
        g.vide * 3,
    ])
    assert str(g) == attendu

def test_ajoute_bateau():
    g = Grille(2, 3)
    b = Bateau(1, 0, longueur=2, vertical=False)
    ok = g.ajoute(b)
    assert ok is True
    assert g.grille == [
        g.vide, g.vide, g.vide,
        b.marque, b.marque, g.vide
    ]
