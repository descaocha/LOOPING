bahan = ["eggs", "flour", "chocolate", "butter", "sugar", "salt"]

nilai = 0

print("Hai, kamu harus menebak 3 resep cookies!!!")

bahan1 = input("Bahan 1? ")

if bahan1 in bahan:
    print("Kamu berhasil menebak", bahan1)
    nilai += 1
else:
    print("Yah tebakan kamu salah")

bahan2 = input("Bahan 2? ")

if bahan2 in bahan:
    print("Kamu berhasil menebak", bahan2)
    nilai += 1
else:
    print("Yah tebakan kamu salah")

bahan3 = input("Bahan 3? ")

if bahan3 in bahan:
    print("Kamu berhasil menebak", bahan3)
    nilai += 1
else:
    print("Yah tebakan kamu salah")

print("Nilai kamu: ", nilai)