# parameter biasa
def luas_persegi_panjang(panjang, lebar):
    print("luas:", panjang * lebar)

luas_persegi_panjang(8, 5)          # argumen posisional
luas_persegi_panjang(lebar=4, panjang=6)    #keyword argument

# nilai defalut
def sapa(nama, salam='hallo'):
    print(salam + ", " + nama + "!")

sapa('budi')                    # output: hallo, budi
sapa('ani', 'selamat pagi')     # output: selamat pagi, ani