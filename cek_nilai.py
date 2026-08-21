# progam cek kondisi nilai
nama = input("nama siswa : ")
nilai = int(input("nilai ujian : "))
hadir = input("hadir 80%? (iya/tidak): ")

# operator perbandingan
print()
print("=== HASIL CEK ===")
print("Nilai >= 75 :", nilai >=75)
print("Nilai >= 90 :", nilai >= 90)
print("Nilai antara 75-89:", nilai >= 75 and nilai <= 89)

# operator logika
hadir_ok = hadir == "ya"
lulus    = nilai >= 75 and hadir_ok
remidial = nilai < 75 or not hadir_ok

print("LULUS         :", lulus)
print("PERLU REMIDIAL:", remidial)