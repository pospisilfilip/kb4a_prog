def mince():
    import random

    zustatek = 100
    
    while zustatek > 0:
        print("Máš", zustatek, "Kč")
        sazka = int(input("Kolik chceš vsadit?"))
        tip = input("Tipni si (panna/orel):").lower

        vysledky = ["panna", "orel"]
        vysledek = random.choice(vysledky)
        
        

        print("Padlo:", vysledek)

        if tip == vysledek:
            zustatek+=sazka
            print("Vyhravas", sazka, "Kc!")

        else:
            zustatek-=sazka
            print("Prohravas", sazka, "Kc!")


        znova = input("Hrat znovu (a/n)")
        if znova == "n":
            zustatek = 0


mince()



