from matplotlib import pyplot as plt

testlar = [1, 2, 3, 4, 5]
guruh_a = [65, 70, 75, 80, 85]
guruh_b = [60, 72, 70, 88, 90]

plt.plot(testlar, guruh_a, color="blue", marker="o", label="guruh A")
plt.plot(testlar, guruh_b, color="red", marker="s", label="guruh B")

plt.title("ikki guruh test natijalari")
plt.xlabel("testlar")
plt.ylabel("ball")
plt.legend()
plt.grid()

ortacha_a = sum(guruh_a) / len(guruh_a)
ortacha_b = sum(guruh_b) / len(guruh_b)

print("guruh A o'rtacha bali:", ortacha_a)
print("guruh B o'rtacha bali:", ortacha_b)
print("o'rtacha natijaga ko'ra guruh B yaxshiroq.")

plt.show()