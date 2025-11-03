# Příklad cesty k souboru
# todo: možná bude nutné upravit cestu
cesta = "data/slova.txt"


# Otevření souboru v režimu pro čtení ("r") s UTF-8 kódováním
with open(cesta, "r", encoding="utf-8") as file:
    lines = file.readlines()  # Načtení pole všech řádků souboru
    for line in lines:
        slovo = line.strip()  # Odstraní přebytečné mezery a konce řádků
        print(slovo)

print("\n---\n")

# Ukázka použití .split()
veta = "I know he ***** swapped those numbers!"
slova = veta.split()
print(slova)

# split() může používat i jiný oddělovač než mezeru:
text = "Máma mele maso. Ola solí. Máma má mísu."
jednotlive_vety = text.split(".")
print(jednotlive_vety)
