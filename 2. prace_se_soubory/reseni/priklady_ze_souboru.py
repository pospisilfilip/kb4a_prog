import random


cesta = "2. prace_se_soubory\data\priklady.txt"


def generuj_priklad(radek):
    # vstup: radek ze ktereho generuje
    # generuje proiklad a vraci bool zda jej uživatel vyřešil



    cislo1 = int(radek.split()[0])
    operace = radek.split()[1]
    cislo2 = int(radek.split()[2])

    print(f"Spočítej: {cislo1} {operace} {cislo2}")
    odpoved = int(input())

    if operace == "+":
        spravne = cislo1 + cislo2
    elif operace == "-":
        spravne = cislo1 - cislo2
    else:
        spravne = cislo1 * cislo2

    return odpoved == spravne


pocet_prikladu = random.randint(3, 6)
spravne_odpovedi = 0

with open(cesta, "r", encoding="utf-8") as file:
    radky = file.readlines()
    #for i in range(5):
    #    print(radky[i])

    for i in range(pocet_prikladu):
        if generuj_priklad(radky[i].strip()):
            spravne_odpovedi += 1

print(f"Počet správných odpovědí: {spravne_odpovedi}")
