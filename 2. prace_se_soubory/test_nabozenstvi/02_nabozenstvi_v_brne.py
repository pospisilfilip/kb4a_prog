import csv


def uloz_brno_do_souboru():
    with open(r"2. prace_se_soubory/test_nabozenstvi/vira_v_cesku.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for radek in reader:
            if radek["uzemi_txt"] == "Brno":
                with open(r"vystup.txt", "a", encoding="utf-8") as file_zapis:
                    nazev_viry = radek["vira_txt"]
                    pocet_verici = radek["hodnota"]
                    file_zapis.write(f"{nazev_viry}: {pocet_verici}\n")

    print("Hotovo")


uloz_brno_do_souboru()