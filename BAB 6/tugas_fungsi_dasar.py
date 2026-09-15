# ——— fungsi tampa parameter dan retrun ———
def garis_pemisah():
    print("=" * 35)

# ——— fungsi dengan parameter, tampa retrun ———
def sapa_siswa(nama, kelas):
    print(f"haloo, {nama} dari kelas {kelas}!")

# ——— fungsi dengan parameter dan retrung ———
def hitung_luas_segitiga(alas, tinggi):
    luas = 0.5 * alas * tinggi
    return luas

def hitung_keliling_persegi(sisi):
    return 4 * sisi

# ——— memanggil semua fungsi ———
garis_pemisah()
sapa_siswa("budi", "X RPL")
sapa_siswa("ani", "X RPL")
garis_pemisah()

l_segitiga = hitung_luas_segitiga(10, 6)
print(f"luas ssegitiga (alas=10, tinggi=6): {l_segitiga}")

k_persegi = hitung_keliling_persegi(7)
print(f"keliling persegi (sisi=7): {k_persegi}")

# fungsi langsungdalam ekspresi
print(f"total luas + keliling = {l_segitiga + k_persegi}")

