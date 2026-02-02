# Načteme potřebné knihovny
import csv
from sklearn.neural_network import MLPClassifier  # Neuronová síť
from sklearn.model_selection import train_test_split  # Rozdělení dat na trénovací a testovací
import matplotlib.pyplot as plt  # Pro vykreslování grafů
from sklearn.metrics import ConfusionMatrixDisplay  # Pro zobrazení matice záměn

# ---------- Načtení dat z CSV a úprava ----------
X = []  # Vstupy (parametry: open, high, low, close, volume)
Y = []  # Výstupy (kategorie volatility)

# Načteme data z CSV souboru. CSV soubor by měl obsahovat sloupce: timestamp, open, high, low, close, volume.
with open("3. strojove_uceni/data/crypto_volatility_dec2025_FINAL_2025-12-09.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)  # Používáme DictReader pro lepší přístup k datům podle názvů sloupců
    
    for row in reader:
        # Získáme ceny z jednotlivých sloupců
        open_price = float(row["open"])    # Otevírací cena
        high_price = float(row["high"])    # Nejvyšší cena
        low_price = float(row["low"])      # Nejnižší cena
        close_price = float(row["close"])  # Zavírací cena
        volume = float(row["volume"])      # Objem obchodování
        
        # Výpočet volatility: rozdíl mezi nejvyšší a nejnižší cenou (vyjádřený jako podíl vůči otevřené ceně)
        volatility = (high_price - low_price) / open_price
        
        # Klasifikujeme volatilitu na tři kategorie:
        # 0 = Nízká volatilita (pokud volatilita je menší než 2%)
        # 1 = Střední volatilita (mezi 2% a 5%)
        # 2 = Vysoká volatilita (více než 5%)
        if volatility < 0.02:
            volatility_category = 0  # Nízká volatilita
        elif volatility < 0.05:
            volatility_category = 1  # Střední volatilita
        else:
            volatility_category = 2  # Vysoká volatilita
        
        # Přidáme do vstupů (X) a výstupů (Y)
        X.append([open_price, high_price, low_price, close_price, volume])
        Y.append(volatility_category)

# ---------- Rozdělení dat na trénovací a testovací sadu ----------
# Data rozdělíme na trénovací (80%) a testovací (20%) sadu.
# Parametr `stratify=Y` zajišťuje, že kategorie volatility budou rozděleny rovnoměrně mezi trénovací a testovací data.
trening_X, test_X, trening_Y, test_Y = train_test_split(
    X, Y,
    test_size=0.2,      # 20% dat bude testovací
    random_state=42,    # Pro reprodukovatelnost výsledků
    stratify=Y          # Stratifikace podle Y (kategorie volatility), aby každá kategorie byla reprezentována
)

# ---------- Vytvoření a trénování neuronové sítě ----------
# Používáme Multi-Layer Perceptron (MLP) pro klasifikaci.
# Tento model má dvě skryté vrstvy, první s 8 neurony a druhou s 4 neurony.
neural_network = MLPClassifier(
    hidden_layer_sizes=(8, 4),  # Dvě skryté vrstvy (8 a 4 neurony)
    activation="relu",          # ReLU aktivační funkce
    max_iter=2000,              # Maximální počet iterací pro trénink
    verbose=True,               # Vypisovat informace o trénování
    random_state=4              # Pro reprodukovatelnost výsledků
)

# Trénování modelu s trénovacími daty
neural_network.fit(trening_X, trening_Y)

# ---------- Vyhodnocení modelu ----------
# Predikce na testovací sadě
results = neural_network.predict(test_X)

# Výpočet přesnosti modelu: Kolik procent správně predikovaných kategorií máme.
correct = 0
for i in range(len(results)):
    if test_Y[i] == results[i]:
        correct += 1

# Vypíšeme přesnost modelu
print("Přesnost:", correct / len(results))

# ---------- Confusion Matrix ----------
# Pro zobrazení matice záměn použijeme ConfusionMatrixDisplay.
# Matice záměn ukáže, jak dobře model předpověděl každou kategorii (nízká, střední, vysoká volatilita).
ConfusionMatrixDisplay.from_predictions(
    test_Y, results, labels=[0, 1, 2]  # Ujistíme se, že všechny tři kategorie jsou zobrazeny
)
plt.show()

