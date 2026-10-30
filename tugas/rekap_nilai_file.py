
# Tugas 5 - Rekap Nilai dari File

def baca_data(nama_file):
    data = []
    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for nomor, baris in enumerate(file, start=1):
                baris = baris.strip()
                if not baris:
                    continue

                try:
                    nim, teks_nilai = baris.split(",")
                    nilai = float(teks_nilai)

                    if not nim.strip():
                        raise ValueError("NIM kosong")

                    data.append((nim.strip(), nilai))

                except ValueError:
                    print(f"Baris {nomor} dilewati (data tidak valid): {baris}")

    except FileNotFoundError:
        print(f"File tidak ditemukan: {nama_file}")

    return data


def tulis_rekap(nama_file, data):
    if not data:
        print("Tidak ada data valid untuk direkap.")
        return

    nilai = [item[1] for item in data]

    rata_rata = sum(nilai) / len(nilai)
    jumlah_lulus = sum(1 for x in nilai if x >= 60)

    with open(nama_file, "w", encoding="utf-8") as file:
        file.write(f"Jumlah data valid: {len(nilai)}\n")
        file.write(f"Rata-rata: {rata_rata:.2f}\n")
        file.write(f"Minimum: {min(nilai):.2f}\n")
        file.write(f"Maksimum: {max(nilai):.2f}\n")
        file.write(f"Jumlah lulus: {jumlah_lulus}\n")

    print(f"Jumlah data valid: {len(nilai)}")
    print(f"Rata-rata: {rata_rata:.2f}")
    print(f"Minimum: {min(nilai):.2f}")
    print(f"Maksimum: {max(nilai):.2f}")
    print(f"Jumlah lulus: {jumlah_lulus}")
    print(f"Rekap disimpan ke {nama_file}")


input_file = "data/nilai.txt"
output_file = "data/hasil_rekap.txt"

data = baca_data(input_file)

if data:
    tulis_rekap(output_file, data)
