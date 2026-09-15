# contoh break - berhenti saat ketemu angka 5
for i in range(1, 11):
    if i == 5:
        break           # keluar dari loop
    print(i, end=" ")
# output: 1 2 3 4 

print()

# contoh continue - lewat angka genap
for i in range(1, 11):
    if i % 2 == 0:
        continue        # lewati interaksi ini
    print(i, end=" ")   # cetak ganjil saja
# output: 1 3 5 7 9