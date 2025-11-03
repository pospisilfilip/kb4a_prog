import random

def generuj_priklad():
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    znaminko = random.choice(["+", "-", "*"])

    if znaminko == "+":
        vysledek = a+b

    elif znaminko == "-":
        vysledek = a-b

    elif znaminko == "*":
        vysledek = a*b

    print(a, znaminko, b, "=?.....")
    tip = int(input("?...."))
              
    if tip == vysledek:
        return True

    if tip != vysledek:
        return False


pocet = random.randint(3, 6)

spravne = 0
for i in range (pocet):
    if generuj_priklad():
        spravne += 1
    

print(f"Správně: {spravne}")