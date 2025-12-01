import csv
import matplotlib.pyplot as plt

# CSV (comma-separated values) je datový formát sloužící ke kompaktnímu uložený dat
# Každý řádek je jeden záznam s hodnotami oddělenými čárkami


# Pracujeme s historickými daty teplot od https://www.chmi.cz
# Cílem je:
#   1. Otevřít soubor s teplotami
#   2. Načíst všechny teploty, které mají ve sloupci "TIME" 21:00
#   3. Získat průměr a maximum
#   4. Vykreslit změnu teploty pomocí grafu


# otevřeme CSV soubor v režimu čtení
with open("2. prace_se_soubory/data/teploty.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)  # DictReader načítá CSV jako slovníky podle názvů sloupců

    vsechny_teploty = []
    vsechny_roky = []

    for radek in reader:
        if radek["TIME"] == "21:00":
            teplota = float(radek["TEMPERATURE"])
            vsechny_teploty.append(teplota)
            vsechny_roky.append(radek["YEAR"])

    # Průměr:
    prumer = sum(vsechny_teploty) / len(vsechny_teploty)
    print(f"Průměrná teplota v 21:00 je {round(prumer, 2)}°C")

    # Maximum
    max_rok = 0
    max_teplota = 0
    for i in range(len(vsechny_teploty)):
        if vsechny_teploty[i] > max_teplota:
            max_teplota = vsechny_teploty[i]
            max_rok = vsechny_roky[i]
    print(f"Nejvyšší teplota {max_teplota}°C byla v roce {max_rok}")


    # Graf změny teploty
    plt.plot(vsechny_roky, vsechny_teploty,)
    plt.title("Večerní teplota podle roku")
    plt.xlabel("Rok")
    plt.ylabel("Teplota [°C]")
    #plt.xticks(vsechny_roky[::5])
    plt.show()

    # matplotlib je knihovna obsahující (mimo jiné) hezké prostředí pro zobrazení grafů
        # hezkou ukázku jejích možností najdete třeba zde: https://matplotlib.org/stable/plot_types/index.html
        # využití různých grafů ukazuje také school: https://www.w3schools.in/matplotlib/tutorials/plot-types
        # nebojte se pro stylistickou úpravu grafu googlovat nebo používat AI
        # ukázka sloupcového grafu: https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_colors.html#sphx-glr-gallery-lines-bars-and-markers-bar-colors-py