import csv
from openpyxl import Workbook   # knihovna pro práci s .xlsx

# Cílem je:
#   1. Otevřít soubor s teplotami
#   2. Najít všechny různé časové hodnoty (TIME)
#   3. Spočítat průměr teplot pro každý čas
#   4. Uložit výsledek do Excelu


with open("2. prace_se_soubory/data/teploty.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    casy = []            # seznam unikátních časů, např. ["AVG", "07:00", "14:00", "21:00"]
    soucty = []          # součet teplot pro každý čas ve stejném pořadí jako casy
    pocty = []           # počet měření pro každý čas ve stejném pořadí jako casy

    # projdeme všechny řádky v CSV
    for radek in reader:
        cas = radek["TIME"]
        teplota = float(radek["TEMPERATURE"])

        # pokud čas ještě nemáme v seznamu, přidáme ho
        if cas not in casy:
            casy.append(cas)
            soucty.append(teplota)
            pocty.append(1)
        else:
            # najdeme index času a přičteme hodnotu
            idx = casy.index(cas)
            soucty[idx] += teplota
            pocty[idx] += 1

# průměry pro každý čas
prumery = []
for i in range(len(casy)):
    prumer = soucty[i] / pocty[i]
    prumery.append(round(prumer, 2))


# Uložení do Excelu
wb = Workbook()
sheet = wb.active
sheet.title = "Průměrné teploty"

sheet.append(["Čas", "Průměrná teplota [°C]"])

for i in range(len(casy)):
    sheet.append([casy[i], prumery[i]])

wb.save("prumerne_teploty.xlsx")
print("Soubor byl vytvořen.")
