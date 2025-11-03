import random
import math

pocet_bodu = 100_000
pocet_bodu_kruh = 0

for i in range(pocet_bodu):
    x = random.random()
    y = random.random()

    if x*x + y*y < 1:
        pocet_bodu_kruh += 1

odhad = pocet_bodu_kruh * 4 / pocet_bodu
print("Odhadovana hodnota je: ", odhad)

rozdil = math.fabs(odhad - math.pi)
print("Rozdíl od pí je:", rozdil)
