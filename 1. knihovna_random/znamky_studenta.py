import random


def generuj_znamky(delka):
    znamky = []
    for i in range(delka):
        znamky.append(random.randint(1, 5))
    return znamky


def vypis_prumer(pole):
    prumer = sum(pole) / len(pole)
    print("Průměr", prumer)


def maximum(pole):
    maxim = 0
    for znamka in znamky:
        if znamka > maxim:
            maxim = znamka
    print(maxim)


znamky = generuj_znamky(10)
print("Známky:", znamky)
vypis_prumer(znamky)
print("Minimum: ", min(znamky))
print("Maximum: ", max(znamky))

prumer = sum(znamky) / len(znamky)
print("Student dostane: ", round(prumer))
