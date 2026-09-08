"""
# cek apakah nilai siswa lulus atau tidak
nilai = int(input("Masukkan nilai: "))

if nilai >= 75:
    print("selamat kamu lulus!")

else:
    print("maaf kamu tidak lulus, silahkan ikut remidial")

    print("nilai kamu adalah", nilai)

print("terima kasih telah mengikuti ujian ini")

# program cek bilangan genap atau ganjil
angka = int(input("masukan angka: "))

if angka % 2 == 0:
    print( angka, "adalah  bilangan genap")
else:
    print( angka, "adalah bilangan ganjil")
"""
# kategori nilai 
nilai = int(input("masukan nilai (1-100):"))

if nilai >= 90:
    kategori = "A (sangat baik)"
elif nilai >= 80:
    kategori = "B (baik)"
elif nilai >= 70:
    kategori = "C (cukup baik)"
elif nilai >= 60:
    kategori = "D (kurang)"
elif nilai >= 50:
    kategori = "E (sangat kurang)"
else:
    kategori = "F (gagal)"

print("nilai    :", nilai)
print("kategori :", kategori)