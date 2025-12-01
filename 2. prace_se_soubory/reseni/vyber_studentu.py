import random


cesta = r"2. prace_se_soubory\data\studenti.txt"

vybrani_studenti = []

with open(cesta, "r", encoding="utf-8") as file:
    studenti = file.readlines()
    while len(vybrani_studenti) < 5:
        novy_student = random.choice(studenti)
        if novy_student not in vybrani_studenti:
            vybrani_studenti.append(novy_student.strip())

vybrani_studenti.sort()

print(vybrani_studenti)

with open("zkouseni_studenti.txt", "w", encoding="utf-8") as file:
    #file.write("Ahoj světe")
    for s in vybrani_studenti:
        #file.write(s+"\n")
        file.write(f"{s}\n")
