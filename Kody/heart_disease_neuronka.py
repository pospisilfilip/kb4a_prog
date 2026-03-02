# Neuronová síť predikující šanci na onemocnění srdce na základě faktorů:
# age: age in years
# sex: sex (1 = male; 0 = female)
# cp: chest pain type
# trestbps: resting blood pressure (in mm Hg on admission to the hospital)
# chol: serum cholestoral in mg/dl
# fbs: (fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)

# heart_disease : 1 nebo 0 - Onemocnění srdce - ano(1)/ne(2)

# Další, nevyužité veličiny:

# restecg: resting electrocardiographic results
# thalach: maximum heart rate achieved
# exang: exercise induced angina (1 = yes; 0 = no)
# oldpeak = ST depression induced by exercise relative to rest
# slope: the slope of the peak exercise ST segment
# ca: number of major vessels (0-3) colored by flourosopy
# thal: 0 = normal; 1 = fixed defect; 2 = reversable

#Úspěšnost a využití: 
#Random forest: 98.54%
#Neuronová síť (MLPClassifier): 78.04%
#Random Forest dosáhl výrazně vyšší přesnosti (98.54%), což ukazuje, že tento model je pro tuto konkrétní úlohu silnější a lépe odhaluje vzory v datech.

# Model by v současné podobě nebyl vhodný jako samostatný diagnostický nástroj. 
# I když dosahuje poměrně slušné přesnosti, z konfuzní matice vyplývá, že hůře odhaluje skutečně nemocné pacienty, což je v medicíně zásadní problém.

# Využití by proto bylo možné spíše jako podpůrný nebo screeningový nástroj, nikoli jako náhrada lékařského rozhodování.
# Lékařům bych jej v této fázi doporučil pouze jako pomocný systém, nikoli jako plnohodnotný klinický nástroj.



import csv

from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay

X = []  # = vstupy
Y = []  # = výstupy

with open("3. strojove_uceni\data\heart_disease_dataset.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        age = float(row["age"])
        sex = float(row["sex"])
        cp = float(row["cp"])
        trestbps = float(row["trestbps"])
        chol = float(row["chol"])
        fbs = float(row["fbs"])


        heart_disease = int(row["heart_disease"])


        X.append([age, sex, cp, trestbps, chol, fbs])
        Y.append(heart_disease)



trening_X, test_X, trening_Y, test_Y  = train_test_split(
        X, Y,
        test_size=0.2,
        random_state=42)



neural_network = MLPClassifier(
    hidden_layer_sizes=(16, 8),  
    activation="relu",  # Nebo "tanh", davalo horsi vysledky "
    max_iter=4000,  
    verbose=2,  
    random_state=42,
    n_iter_no_change=40,  
    alpha=0.001,  
    solver="adam",  # Nebo "sgd, ale ta davala horsi vysledky"
)

neural_network.fit(trening_X, trening_Y)



from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Rozdělení dat na trénovací a testovací
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Model Random Forest
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)





#----------Predikce a vyhodnocení přesnosti-----------------
results = neural_network.predict(test_X)

correct = 0
for i in range(len(results)):
    if test_Y[i] == results[i]:
        correct += 1
print("Přesnost:", correct / len(results))

y_pred = rf.predict(X_test)
print("Přesnost Random Forest:", accuracy_score(y_test, y_pred))

# ---------- Confusion matrix ----------
# zobrazuje jaké odpovědi dává neuronka pro dané vstupy
ConfusionMatrixDisplay.from_predictions(
    test_Y, results)
plt.show()


