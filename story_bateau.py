# User Story : "Chevauchement"

from bateau import Bateau

def chevauchent(b1, b2):
    for pos in b1.positions:
        if pos in b2.positions:
            return True
    return False

def main():
    b1 = Bateau(2, 3, longueur=3, vertical=False)
    b2 = Bateau(2, 4, longueur=2, vertical=False)

    print("B1 :", b1.positions)
    print("B2 :", b2.positions)
    print("Chevauchent ?", chevauchent(b1, b2))

    print()

    b3 = Bateau(0, 0, longueur=2, vertical=False)
    b4 = Bateau(1, 0, longueur=2, vertical=False)

    print("B3 :", b3.positions)
    print("B4 :", b4.positions)
    print("Chevauchent ?", chevauchent(b3, b4))

if __name__ == "__main__":
    main()
