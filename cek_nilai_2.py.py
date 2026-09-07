print("=" * 36)
for siswa in "  CEKNILAI SISWA":
    print(siswa, end=" ")
print()
print("=" * 36)

nama = input("masukan nama : ")
nilai = int(input("masukan nilai ujian (1-100) : "))

if nilai >=90:
    kategori = "A (sangat baik)"
    keterangan = "selamat " + nama + " kamu lulus ujian dengan nilai " + str(nilai) + " dan kategori " + kategori
elif nilai >=80:
    kategori = "B (baik)"
    keterangan = "selamat " + nama + " kamu lulus ujian dengan nilai " + str(nilai) + " dan kategori " + kategori
elif nilai >=70:
    kategiri = "C (cukup baik)"
    keterangan = "selamat " + nama + " kamu lulus ujian dengan nilai " + str(nilai) + "dan kategori " + kategori
elif nilai >=60:
    kategori = "D (kurang)"
    keterangan = "maaf " + nama + " kamu tidak lulus ujian dengan nilai " + str(nilai) + " dan kategori " + kategori
else:
    kategori = "E (sangat kurang)"
    keterangan = "maaf " + nama + " kamu tidak lulus ujian  dengan nilai " + str(nilai) + " dan kategori " + kategori

print()
print("nilai    :", nilai)
print("kategori :", kategori)
print("keterangan :", keterangan)
print("=" * 36)
for huruf in "    TERIMAKASIH":
    print(huruf, end=" ")
print()
print("=" * 36)