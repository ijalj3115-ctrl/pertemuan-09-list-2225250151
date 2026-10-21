# Pertemuan 09 - List dan Pengolah Data Numerik

Nama: Rijal Munawarudin
NIM: 2225250151
Kelas: 3F

## Tujuan
Mengolah kumpulan data numerik dengan list Python.

## Struktur Program
Jelaskan file latihan dan praktik.
* `latihan/01_buat_list.py`: Membuat list nilai awal dan menghitung panjang atau banyak data dalam list.
* `latihan/02_indeks_slicing.py`: Mengakses elemen list menggunakan indeks (positif/negatif) dan memotong data list (slicing).
* `latihan/03_manipulasi_list.py`: Mengubah nilai elemen, menambah data baru (`append`/`insert`), dan menghapus data (`remove`).
* `latihan/04_agregasi_nilai.py`: Melakukan perhitungan statistik dasar (Total, Rata-rata, Minimum, dan Maksimum) pada data list.
* `latihan/05_filter_kelulusan.py`: Menyaring data nilai menggunakan perulangan dan kondisi untuk memisahkan mahasiswa yang lulus.
* `latihan/06_fungsi_statistik.py`: Membungkus logika perhitungan rata-rata ke dalam sebuah fungsi (`def`) agar bisa digunakan berulang kali.
* `praktik/analisis_nilai_mahasiswa.py`: Program utama terintegrasi untuk menganalisis total nilai, rata-rata, batas kelulusan, dan ringkasan statistik dari 10 data nilai mahasiswa.

## Cara Menjalankan
Karena perintah bawaan `python3` atau `python` mengalami masalah pembacaan jalur (PATH) di Windows, jalankan file program menggunakan perintah **Python Launcher (`py`)** melalui terminal:

```bash
py praktik/analisis_nilai_mahasiswa.py
```

## Test Case
Catat data, hasil yang diharapkan, hasil aktual, dan status.

| Nama File Uji | Data Input | Hasil yang Diharapkan | Hasil Aktual | Status |
| :--- | :--- | :--- | :--- | :--- |
| `01_buat_list.py` | `[75, 80, 65, 90, 88]` | Banyak data = 5 | Banyak data = 5 | **LULUS** |
| `02_indeks_slicing.py` | `[75, 80, 65, 90, 70]` | Elemen indeks tertentu & potongan list tepat | Sesuai dengan pembatasan indeks slicing | **LULUS** |
| `03_manipulasi_list.py` | Perubahan nilai & fungsi list | List akhir: `[75, 70, 82, 90]` | List akhir: `[75, 70, 82, 90]` | **LULUS** |
| `04_agregasi_nilai.py` | `[75, 82, 90, 88, 63]` | Total=398, Rata2=79.60, Min=65, Max=90 | Total=398, Rata2=79.60, Min=65, Max=90 | **LULUS** |
| `05_filter_kelulusan.py`| `[75, 80, 60, 45, 90]` | Nilai lulus >= 60, Jumlah lulus = 4 | Nilai lulus = `[75, 80, 60, 90]`, Jumlah = 4 | **LULUS** |
| `06_fungsi_statistik.py`| `[75, 80, 65, 90, 88]` | Rata-rata = 79.60 | Rata-rata = 79.60 | **LULUS** |
| `analisis_nilai_mahasiswa.py`| `[78, 55, 90, 67, 60, 82, 45, 71, 88, 59]` | Ringkasan statistik lengkap, 7 Lulus, 3 Belum Lulus | Ringkasan statistik lengkap, 7 Lulus, 3 Belum Lulus | **LULUS** |

## Refleksi
Tuliskan satu hal yang Anda pahami tentang indeks/list dan satu kesalahan yang berhasil diperbaiki.
* **Hal yang saya pahami**: Saya memahami bahwa struktur data *list* di Python sangat fleksibel karena bisa dimanipulasi nilainya (ditambah, disisip, atau dihapus) serta sangat mudah dihitung nilai statistiknya secara langsung menggunakan fungsi bawaan seperti `sum()`, `len()`, `min()`, dan `max()`.
* **Kesalahan yang berhasil diperbaiki**: Saya sempat mengalami error *CommandNotFound* / *Python tidak ditemukan* saat mencoba menjalankan file menggunakan perintah `python`. Kesalahan ini berhasil diatasi dengan mengganti perintah eksekusi terminal menjadi `py` (Python Launcher) yang mendeteksi instalasi lokal secara tepat.