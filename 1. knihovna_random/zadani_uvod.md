# Úlohy – Generování náhody v Pythonu

### 1. Hod mincí se sázením
- Vytvoř program, který vygeneruje náhodně 0 nebo 1 a vypíše výsledek hodu mincí.  
- Pokud je výsledek `0`, vypiš `"panna"`.  
- Pokud je výsledek `1`, vypiš `"orel"`.  
- Uživatel má na začátku **100 Kč**.  
- Před každým hodem si zvolí, kolik chce vsadit.  
- Pokud uhodne, získá dvojnásobek vsazené částky. Pokud ne, vsazená částka se odečte.  

**Ukázka výstupu:**
```python
Máš 100 Kč
Kolik chceš vsadit? 20
Tipni si (panna/orel): panna
Padlo: panna
Vyhráváš 40 Kč! Stav účtu: 120 Kč
Hrát znovu [a/n]: n
```

---

### 2. Hod kostkou
- Vytvoř program, který vygeneruje hod kostkou (číslo 1–6).  
- Přidej možnost zvolit si **počet kostek**, které se hodí, a vypiš součet.  
- Přidej možnost zvolit si **počet stran kostek** (např. 20).  

**Ukázka vstupu/výstupu:**
```
Zadej počet kostek: 2
Zadej počet stěn kostky: 6
Hody: 3 5
Součet: 8
```

```
Zadej počet kostek: 1
Zadej počet stěn kostky: 20
Hod: 17
```

---

### 3. Generuj karty pokeru
- Napiš program, který generuje pokerové karty z balíčku.  
- Po stisknutí libovolné klávesy se vygeneruje **náhodná karta**, která ještě nebyla rozdána.  
- Zajisti, aby se karty **neopakovaly**.  

**Ukázka výstupu:**
```
Stiskni klávesu pro vygenerování karty...
Vytáhl jsi: Kříže - Král
Stiskni klávesu...
Vytáhl jsi: Srdce - 7
```

---

### 4. Generátor hesla
- Vytvoř program, který vygeneruje náhodné heslo.  
- Heslo musí:  
  - mít délku 7–12 znaků,  
  - obsahovat alespoň jedno číslo,  
  - obsahovat alespoň jeden znak z množiny `. , - #`,  
  - ostatní znaky budou písmena (malá/velká).  

**Ukázka výstupu:**
```
Vygenerované heslo: p7m.rQa
```
```
Vygenerované heslo: Zd3a#RkL8
```

---

### 5. Hádej číslo
- Program si vygeneruje náhodné číslo mezi 1 a 100.  
- Uživatel hádá číslo.  
- Po každém tipu program napíše:  
  - `Moc nízko!` pokud je tip menší,  
  - `Moc vysoko!` pokud je tip větší,  
  - `Uhodl jsi!` pokud se trefí.  
- Na konci vypiš počet pokusů a zeptej se, zda chce uživatel hrát znovu.  

**Ukázka vstupu/výstupu:**
```
Hádej číslo (1-100): 50
Moc nízko!
Hádej číslo (1-100): 75
Moc vysoko!
Hádej číslo (1-100): 62
Uhodl jsi! Počet pokusů: 3
Chceš hrát znovu? (a/n): n
```

---

## 6. Pokročilé úlohy

### 6.1 Simulace pokeru
- Napiš program, který simuluje ruku pokeru.  
- Vygeneruj 2 karty na stole a 3 karty v ruce hráče.  
- Program určí:  
  - nejvyšší kartu,  
  - zda má hráč **dvojici**,  
  - zda má hráč **postupku**.  
  - případně další...
 - Zkuste hru následně rozšířit o více hráčů. Generujte 3 karty na stole, 2 karty v ruce hráče A a 2 karty v ruce hráče B. Jaká je nejvyšší kombinae karet, kterou hráči mají? Kdo z nich by vyhrál?

Na podobném principu lze vytvořit celou hru *Texas hold 'em*.

---

### 6.2 Generátor sudoku
- Vytvoř program, který náhodně vygeneruje zadání sudoku.  
- Podle hodnoty proměnné `komplet`:  
  - pokud `komplet=True`, vypíše celé vyplněné sudoku,  
  - pokud `komplet=False`, vypíše jen část zadání (např. polovinu všech číslic).  
- Výstupem programu bude vykreslená deska se zadáním sudoku na terminál. Např.:

```
+-------+-------+-------+
| 5 3 . | . 7 . | . . . |
| 6 . . | 1 9 5 | . . . |
| . 9 8 | . . . | . 6 . |
+-------+-------+-------+
| 8 . . | . 6 . | . . 3 |
| 4 . . | 8 . 3 | . . 1 |
| 7 . . | . 2 . | . . 6 |
+-------+-------+-------+
| . 6 . | . . . | 2 8 . |
| . . . | 4 1 9 | . . 5 |
| . . . | . 8 . | . 7 9 |
+-------+-------+-------+
```

---

## 7. Monte Carlo simulace
- Pomocí generování náhodných bodů odhadni číslo π.  
- Vygeneruj `N` náhodných bodů v jednotkovém čtverci.  
- Spočítej, kolik jich leží v kruhu o poloměru 1.  
- Použij vztah:  
  ```
  π ≈ 4 * (počet bodů v kruhu / celkový počet bodů)
