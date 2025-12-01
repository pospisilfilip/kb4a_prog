import csv
import matplotlib.pyplot as plt

cesta = r"2. prace_se_soubory\data\teploty.csv"

with open(cesta, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    
    roky = []
    teploty_rano = []

    for radek in reader:
        if radek["TIME"] == "07:00": #or radek["TIME"] == "21:00":
            print(radek["YEAR"], radek["TEMPERATURE"])
            teplota = float(radek["TEMPERATURE"])
            teploty_rano.append(teplota)
            rok = int(radek["YEAR"])
            roky.append(rok)
    
    prumer = sum(teploty_rano) / len(teploty_rano)
    print(f"Průměrné ranní teploty jsou {round(prumer, 2)}°C")

    plt.bar(roky, teploty_rano)
    plt.title("Průměrné ranní teploty v ČR")
    plt.xlabel("Rok")
    plt.ylabel("Teploty [°C]")
    plt.show()