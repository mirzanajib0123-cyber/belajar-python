# progam biodata soswa
print("=" * 35)
print("        FROM BIODAT SISWA")
print("=" * 35)

nama    = input ("NAMA LENGKAP   :   ")
kelas   = input ("KELAS          :   ")
umur    = int (input("UMUR  (TAHUN)  :   "))
tinggi  = float(input("TINGGI   (CM) :   "))

print()
print("=" * 35)
print(" DATA TERSIMPAN")
print("=" * 35)
print("Nama :", nama)
print("kelas:", kelas)
print("umur :", umur)
print("tinggi:", tinggi, "tahun")
print("sudah dewasa:", umur >= 17)