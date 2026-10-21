
def rata_rata(data):
    if len(data) == 0:
        return 0
    return sum(data) / len(data)


def nilai_lulus(data, batas=60):
    lulus = []
    for nilai in data:
        if nilai >= batas:
            lulus.append(nilai)
    return lulus


nilai = [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]

print("=== ANALISIS NILAI MAHASISWA ===")
print(f"Daftar nilai     : {nilai}")
print(f"Jumlah data      : {len(nilai)}")
print(f"Total nilai      : {sum(nilai)}")
print(f"Rata-rata        : {rata_rata(nilai):.2f}")
print(f"Nilai minimum    : {min(nilai)}")
print(f"Nilai maksimum   : {max(nilai)}")

lulus = nilai_lulus(nilai)
tidak_lulus = len(nilai) - len(lulus)

print(f"Daftar nilai lulus: {lulus}")
print(f"Jumlah lulus      : {len(lulus)}")
print(f"Jumlah tidak lulus: {tidak_lulus}")
