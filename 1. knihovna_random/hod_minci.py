import random


def herni_smycka(ucet):
    sazka = int(input("Kolik chceš vsadit:"))
    if sazka > ucet:
        print("Nedostatečné finance")
        return ucet
    
    volba = input("Sázíš na [panna] nebo [orel]").lower()

    generovane = random.choice(["panna", "orel"])

    if volba == generovane:
        print("vyhrál jsi!!!")
        print("Bylo ti přičteno", sazka)
        ucet += sazka
    else:
        print("Prohrál jsi :(")
        print("Bylo ti odečteno", sazka)
        ucet -= sazka
    
    return ucet


ucet = 100
while input("Chceš hrát: [a/n]").lower() == "a":
    print("Na účtu máš:", ucet)
    ucet = herni_smycka(ucet)
