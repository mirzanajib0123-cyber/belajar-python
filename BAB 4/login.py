# sistem login sederhana
username = "admin"
password = "admin123"

print("=== LOGIN SISTEM ===")
username = input("username:" )

if username == "admin":
    password = input("password: ")
    if password == password :
        print()
        print("LOGIN BERHASIL! SELAMAT DATANG,", username)
        print("akses ke sistem diberikan")
    else:
        print("LOGIN GAGAL! PASSWORD SALAH")
else:
    print("LOGIN GAGAL! USERNAME tidak ditemukan")