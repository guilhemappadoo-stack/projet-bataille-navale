# test_bateau.py

from bateau import Bateau

def test_positions_horizontales():
    b = Bateau(2, 3, longueur=3, vertical=False)
    assert b.positions == [(2, 3), (2, 4), (2, 5)]

def test_positions_verticales():
    b = Bateau(2, 3, longueur=3, vertical=True)
    assert b.positions == [(2, 3), (3, 3), (4, 3)]
