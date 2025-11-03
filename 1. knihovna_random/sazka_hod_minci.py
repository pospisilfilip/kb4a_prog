from random import choice


ucet = 100
pokracovat = True

while ucet > 0 and pokracovat:
    print("Tvé finance:", ucet)

    sazka = int(input("Kolik sazíš: "))
    while sazka > ucet:
        print("Neplatné. Nedostatečné finance.")
        sazka = int(input("Kolik sazíš: "))

    vyber = input("Na co sázíš [panna/orel]:")

    padlo = choice(["panna", "orel"])
    print("Padlo:", padlo)

    if padlo == vyber:
        ucet += sazka
        print("Vyhrál jsi:", sazka)
    else:
        ucet -= sazka
        print("Prohrál jsi:", -sazka)

    if ucet > 0:
        pokracovat = input("Chceš pokračovat [a/n]").lower()[0] == "a"
    else:
        print("Prohrál jsi. Nemáš finance.")
