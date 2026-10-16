from matplotlib import pyplot as plt

soat = [1, 2, 3, 4, 5, 6, 7]
ball = [40, 48, 55, 65, 72, 85, 90]

plt.scatter(soat, ball, color="purple", s=100)

plt.title("o'qish vaqti va test bali")
plt.xlabel("tayyorlanish vaqti (soat)")
plt.ylabel("test bali")
plt.grid()

plt.show()

print("tayyorlanish vaqti oshgani sari test ballari ham oshgan.")