# Latihan 3 - Menambahkan Isi File
with open("data/catatan.txt", "a", encoding="utf-8") as file:
    file.write("Latihan append berhasil.\n")

print("Teks berhasil ditambahkan ke data/catatan.txt")