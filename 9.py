from matplotlib import pyplot as plt

kunlar = [1, 2, 3, 4, 5, 6, 7]
natijalar = [12, 15, 14, 18, 20, 19, 25]

plt.plot(kunlar, natijalar, marker="o")

plt.title("haftalik natijalar")
plt.xlabel("kunlar")
plt.ylabel("natijalar")
plt.grid()

plt.savefig("natija.png")
plt.show()

print("grafik natija.png nomi bilan saqlandi.")