from bateau import Bateau


def chevauchent(b1, b2):

    for pos1 in b1.positions:
        if pos1 in b2.positions:
            return True
    return False


def main():
    # chevauchement
    b1 = Bateau(2, 3, longueur=3, vertical=False)
    b2 = Bateau(2, 4, longueur=2, vertical=False)

    print("Bateau 1 :", b1.positions)
    print("Bateau 2 :", b2.positions)
    print("Chevauchent ? :", chevauchent(b1, b2))  # True attendu

    print()

    #  pas de chevauchement
    b3 = Bateau(0, 0, longueur=2, vertical=False)
    b4 = Bateau(1, 0, longueur=2, vertical=False)

    print("Bateau 3 :", b3.positions)
    print("Bateau 4 :", b4.positions)
    print("Chevauchent ? :", chevauchent(b3, b4))  # False attendu


if __name__ == "__main__":
    main()
