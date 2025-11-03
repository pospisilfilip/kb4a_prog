def vypis_delitele(cislo):
    print("Dělitelé tohoto čísla jsou:")
    for i in range(1, cislo + 1):
        if cislo % i == 0:
            print("    ", i)


cislo = int(input("Zadej číslo: "))
vypis_delitele(cislo)
