from matplotlib import pyplot as plt

ismlar = ["Ali", "Vali", "Sardor", "Malika", "Aziza", "Jasur"]
ballar = [78, 92, 65, 88, 95, 73]

plt.bar(ismlar, ballar, color="skyblue")

plt.title("o'quvchilar natijalari")
plt.xlabel("o'quvchilar")
plt.ylabel("ballar")
plt.grid(axis="y", linestyle=":")

eng_kop = ballar.index(max(ballar))
eng_kam = ballar.index(min(ballar))
ortacha = sum(ballar) / len(ballar)

print("eng yuqori ball:", ismlar[eng_kop], max(ballar))
print("eng past ball:", ismlar[eng_kam], min(ballar))
print("o'rtacha ball:", round(ortacha, 2))

plt.savefig("oquvchilar_natijasi.png")
plt.show()

print("\n3 ta xulosa:")
print("1. eng yuqori ballni Aziza olgan.")
print("2. eng past ballni Sardor olgan.")
print("3. o'rtacha ball:", round(ortacha, 2))