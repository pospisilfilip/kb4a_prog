import csv
import matplotlib.pyplot as plt


def graf():
    bez_viry = 0
    neuvedeno = 0
    verici = 0

    with open(r"2. prace_se_soubory/test_nabozenstvi/vira_v_cesku.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for radek in reader:
            nabozenstvi = radek["vira_txt"]
            hodnota = int(radek["hodnota"])

            if nabozenstvi == "Bez náboženské víry" or nabozenstvi == "ateismus":
                bez_viry += hodnota
            elif nabozenstvi == "Neuvedeno":
                neuvedeno += hodnota
            else:
                verici += hodnota

    kategorie = ["Bez víry + ateismus", "Neuvedeno", "Věřící"]
    hodnoty = [bez_viry, neuvedeno, verici]

    plt.bar(kategorie, hodnoty)
    plt.title("Víra v Česku")
    plt.ylabel("Počet osob")

    plt.show()


graf()
