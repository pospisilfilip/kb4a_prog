cesta = "2. prace_se_soubory\data\\1984.txt"
radku = 0
delka_celkova = 0
znaky_celkove = 0

with open(cesta, "r", encoding="utf-8") as file:
    lines = file.readlines() 
    for line in lines:
        radku += 1
        slovo = line.strip()
        delka = len(slovo)
        delka_celkova += delka
        znaky = len(line)
        znaky_celkove += znaky


    slova = cesta.split()
    

    #len ischar =  pocet znaku


    print(f"v souboru je {radku} radku, {delka_celkova} slov a {znaky_celkove} znaku")

