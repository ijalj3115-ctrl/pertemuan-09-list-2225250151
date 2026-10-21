def rata_rata(data):
    if len(data) == 0:
        return 0
    return sum(data) / len(data)

def nilai_lulus(data, batas=60):
    list_lulus = []
    for x in data:
        if x >= batas:
            list_lulus.append(x)
    return list_lulus

# 11. Siapkan list nilai (berisi 10 data sesuai gambar)
nilai = [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]

# 12. Hitung banyak data menggunakan len
banyak_data = len(nilai)

# 13. Hitung total, minimum, maksimum, dan rata-rata
total_nilai = sum(nilai)
nilai_min = min(nilai)
nilai_max = max(nilai)
nilai_rata2 = rata_rata(nilai)

# 14 & 15. Dapatkan list mahasiswa yang lulus berdasarkan batas kelulusan 60
list_mahasiswa_lulus = nilai_lulus(nilai, batas=60)

# 16. Hitung jumlah lulus dan belum lulus
jumlah_lulus = len(list_mahasiswa_lulus)
jumlah_belum_lulus = banyak_data - jumlah_lulus

# 17. Tampilkan seluruh hasil dengan format yang rapi dan mudah dibaca
print("=== RINGKASAN STATISTIK & KELULUSAN ===")
print(f"Seluruh Data Nilai : {nilai}")
print(f"Banyak Data        : {banyak_data}")
print("-" * 40)
print(f"Total Nilai        : {total_nilai}")
print(f"Rata-rata Nilai    : {nilai_rata2:.2f}")
print(f"Nilai Minimum      : {nilai_min}")
print(f"Nilai Maksimum     : {nilai_max}")
print("-" * 40)
print(f"Daftar Nilai Lulus : {list_mahasiswa_lulus}")
print(f"Jumlah Lulus       : {jumlah_lulus} mahasiswa")
print(f"Jumlah Belum Lulus : {jumlah_belum_lulus} mahasiswa")
print("=======================================")