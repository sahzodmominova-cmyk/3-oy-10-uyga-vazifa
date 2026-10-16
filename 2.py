from matplotlib import pyplot as plt

fanlar = ["Matematika", "Python", "Ingliz tili", "Fizika", "Tarix"]
ballar = [85, 95, 72, 80, 88]

plt.bar(fanlar, ballar)

plt.title("fanlardan olingan ballar")
plt.xlabel("fanlar")
plt.ylabel("ballar")

plt.show()