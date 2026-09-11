
# Bikin variable dengan tipe data lists
x = ["Apple", "Mango", "Pizza"]
x2 = ["Burger", "Nasi Liwet"]

print(f"Data pertama didalam list x adalah : {x[0]}")
print(f"Data terakhir didalam list x adalah : {x[-1]}")

z = x + x2
print(f"Concatenation dari list x dan x2 adalah : {z}")


z[-1] = "Nasi Padang"
print(f"Hasil mengubah element terakhir dari list z : {z}")

z.append("Nasi Kebuli")
print(f"Hasil dari append list z adalah : {z}")

zx = z
zx[-1] = "Nasi Lemak"
print(f"Mengubah value dari list z dari variable yang mereferensinya : {z}")

print(f"Jumlah dari isi didalam list z menggunakan method len adalah : {len(z)}")

zz = [x, x2]
print(f"Nested list dari x dan x2 : {zz}")



