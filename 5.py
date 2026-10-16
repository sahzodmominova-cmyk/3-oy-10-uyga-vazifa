from matplotlib import pyplot as plt

mashgulot = [1, 2, 3, 4, 5, 6]
masofa = [2.0, 2.5, 2.3, 3.0, 3.5, 4.0]

plt.plot(mashgulot, masofa, color="green", marker="o", linewidth=3)

plt.title("yugurish masofasi")
plt.xlabel("mashg'ulot")
plt.ylabel("masofa (km)")
plt.grid(linestyle=":")

plt.show()

print("1. yugurish masofasi umumiy hisobda oshib borgan.")
print("2. 6-mashg'ulotda 4 km masofa yugurilgan.")