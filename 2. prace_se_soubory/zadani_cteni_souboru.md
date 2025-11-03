# Úlohy - čtení ze souboru
Všechny potřebné soubory by měly být uloženy ve složce *data*. Úlohy jsou seřazeny od jednodušších po složitější.


## 1) **Citát dne**
Vytvoř program, který generuje citát dne pro facebookovou stránku.

Tato stránka postuje citát ve formátu:
 1. *Citát dne:*
 2. 3-5 náhodných emoji z tohoto listu: ```["🌺", "🌼", "🌞", "🐻", "❤️‍", "🔥"]```
 3. Náhodný citát ze souboru *citaty.txt*
 4. Autor citátu ve stylu: *### autor ###*
 5. náhodné emoji z listu:   ```["💥", "🔥", "❤️‍", "😎", "🤣"]```

*Ukázka výstupu:*
```
Citát dne:
🌞🌼🔥🌼
Koupit psa je jediný způsob, jak získat za peníze lásku.
### G. B. Shaw ###
💥
```

---

## 2) **Výběr studentů** 
Načti soubor *studenti.txt* (1 řádek = 1 student). 

Vytvoř funkci, která na vstupu dostane název souboru a 1 číslo *n*. Program následně vypíše *n* náhodně ybraných unikátních jmen ze souboru.

Dej si pozor, aby se vypsaná jména naopakovala.

Vypiš jména vybraných studentů v abecedním pořadí.

*Ukázka výstupu (pro výběr 5 studentů):*
```
Eliška
Hynek
Matyáš
Renata
Sabina
```

---

## 3) **Kvíz z CSV** 
Načti soubor `otazky.csv`.

Vypiš uživateli tři náhodné otázky z tohoto souboru a dej mu na výběr z možností A, B, C. 

Vypiš uživateli, kolik odpovědí má správně.

*Ukázka výstupu:*
```
Kolik je 7*6?
 a) 42
 b) 36
 c) 56
Odpověď: A
...
```

---

## 4) **Zpracování textového souboru.**
Načti soubor *1984.txt*. Tvým úkolem bude analyzovat tento soubor a zjisti od něj několik zajímavostí.

1. Zjisti, z kolika znaků se skládá celý děj 1984.
2. Z kolika vět se text skládá? Můžeš počítat, že každá věta končí na ".", "?" nebo "!"
3. Kolikrát se v textu nachází slovo "*newspeak*"?
4. Uživatel ti zadá slovo. Spočítej, kolikrát se slovo v textu nachází.

---


## 5) **Šibenice**
Vytvoř hru šibenice, která vybere pro hádání náhodné slovo ze souboru slova.txt.

Uživatel má na začátku 7 životů. Nemusíš vypisovat obrázek šibenice- stačí uživateli říct, kolik životů mu zbývá.

---


# Obecné rady k implementaci
- Používej konstrukci `with open(..., encoding="utf-8") as f:`
- Pro reprodukovatelnost výsledků můžeš použít `random.seed(...)`.

---

*Ke generování textových souborů bylo využito AI.*