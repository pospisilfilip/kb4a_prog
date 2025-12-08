import matplotlib.pyplot as plt


plt.bar(["Babka", "Dědeček"], [4, 2])

plt.title("Počty jablek v dětských říkankách")
plt.xlabel("Postava")
plt.ylabel("Jablka [ks]")

plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.show()
