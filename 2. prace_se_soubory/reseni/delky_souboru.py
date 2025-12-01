cesta = r"2. prace_se_soubory\data\1984.txt"

with open(cesta, "r", encoding="utf-8") as file:
    radky = 0
    znaky = 0
    slova = 0

    for radek in file.readlines():
        radky += 1
        znaky += len(radek)
        slova += len(radek.split())

    print(f"Počet slov:  {slova}")
    print(f"Počet znaků: {znaky}")
    print(f"Počet řádků: {radky}")