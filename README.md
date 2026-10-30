
# Pertemuan 12 - File I/O dan Error Handling

Nama: Iren Ihdina Zulfa
NIM: 2225250019
Kelas: 3E

## Tujuan
Membaca, memvalidasi, mengolah, dan menulis data file
menggunakan Python serta menangani error dasar
dengan try-except.

## Format File Input
File data/nilai.txt menggunakan format NIM,nilai.

Contoh:
A001,85
A002,78
A003,92
A004,abc
A005,74
A006,88

## Cara Menjalankan
Buka terminal VS Code dari folder utama proyek.

Jalankan latihan:
python latihan/01_tulis_file.py
python latihan/02_baca_file.py
python latihan/03_append_file.py
python latihan/04_proses_baris.py
python latihan/05_file_not_found.py
python latihan/06_value_error.py

Jalankan tugas:
python tugas/rekap_nilai_file.py

## Error yang Ditangani

1. FileNotFoundError
Terjadi ketika file yang ingin dibaca tidak ditemukan.
Program menampilkan pesan tanpa berhenti secara kasar.

2. ValueError
Terjadi ketika data nilai tidak dapat diubah menjadi angka.
Program melewati baris tersebut dan melanjutkan proses.

## Test Case

| Kondisi | Hasil yang Diharapkan | Status |
|---|---|---|
| Data normal | Rekap sesuai data | Berhasil |
| File tidak ada | Pesan error tampil | Berhasil |
| Nilai A004,abc | Baris dilewati | Berhasil |
| Baris kosong | Baris dilewati | Berhasil |
| Nilai 60 | Dihitung lulus | Berhasil |

## Hasil Rekap
Jumlah data valid: 5
Rata-rata: 83.40
Minimum: 74.00
Maksimum: 92.00
Jumlah lulus: 5

## Refleksi
Pada praktik ini, saya mempelajari cara membaca,
menulis, dan menambahkan isi file menggunakan Python.

Salah satu kesalahan yang dapat terjadi adalah
ValueError ketika data nilai berisi huruf, seperti
"abc", sehingga tidak dapat dikonversi menjadi angka.

Untuk mengatasinya, saya menggunakan try-except
agar data yang salah dapat dilewati dan program
tetap memproses data lainnya.

Saya juga mempelajari penggunaan FileNotFoundError
untuk menangani file yang tidak ditemukan.
