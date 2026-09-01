# progam penentuan kelulusan SMK TJP Tuban
print("=" * 40)
print("         SISTEM PENIALIAN SISWA")
print("=" * 40)
nama        = input("nama siswa        :")
nilai_uts   = float(input("nilai uts   (0-100):  "))
nilai_uas   = float(input("nilai uas   (0-100):  "))
nilai_tugas = float(input("nilai tugas        :  "))

#hiting rata rata
rata = (nilai_uts * 0.3) + (nilai_uas * 0.5) + (nilai_tugas * 0.2)

#temukan kategori
if rata >= 90:
    predikat = "A - sangat baik"
elif rata >= 80:
    predikat = "b - baik"
elif rata >= 70:
    predikat = "c - cukub"
elif rata >= 60:
    predikat = "d - kurang"
else:
    predikat = "e - sangat kurang"

lulus = rata >= 70

print()
print("=" * 40)
print("            HASIL PENILAIAN")
print("=" * 40)
print("nama     :", nama)
print("rata rata:", round(rata, 2))
print("predikat :", predikat)
print("status   :", "LULUS" if lulus else "TIDAK LULUS")