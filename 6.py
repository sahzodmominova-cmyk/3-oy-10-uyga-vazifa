from matplotlib import pyplot as plt

mahsulotlar = ["Non", "Sut", "Tuxum", "Yog", "Shakar"]
sotuv = [45, 30, 60, 20, 25]

plt.bar(mahsulotlar, sotuv, color="orange")

plt.title("haftalik mahsulotlar savdosi")
plt.xlabel("mahsulotlar")
plt.ylabel("sotilgan soni")

eng_kop = sotuv.index(max(sotuv))
eng_kam = sotuv.index(min(sotuv))

print("eng ko'p sotilgan:", mahsulotlar[eng_kop])
print("eng kam sotilgan:", mahsulotlar[eng_kam])

plt.show()