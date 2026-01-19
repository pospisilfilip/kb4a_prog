import csv


def statistiky_pro_nabozenstvi():
    hledane = input("Zadej název náboženství: ").lower()

    celkem = 0
    max_mesto = ""
    max_hodnota = -1

    with open(r"2. prace_se_soubory/test_nabozenstvi/vira_v_cesku.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        # projdi řádky jeden po druhém
        for radek in reader:

            # pokud název víry == hledaná víra
            if radek["vira_txt"].lower() == hledane:
                celkem += int(radek["hodnota"])

                # má město nejvíce věřících z dosavadních řádků?
                if int(radek["hodnota"]) > max_hodnota:
                    max_hodnota = int(radek["hodnota"])
                    max_mesto = radek["uzemi_txt"].strip()

    if celkem == 0:
        print("náboženství nenalezeno")
    else:
        print(f"Celkem věřících: {celkem}")
        print(f"Nejvíce věřících je v: {max_mesto}")


statistiky_pro_nabozenstvi()
