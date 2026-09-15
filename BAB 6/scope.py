x = 10      # variabel global

def fungsi_a():
    x = 99      # variabel lokal - berbeda dari x global!
    print("di dalam fungsi_a, x=", x)   # 99

def fungsi_b():
    print("di dalam fungsi_b, x =", x)   # 10 (pakai global)

fungsi_a()
fungsi_b()
print("di luar fungsi, x =", x)     # 10 (tidak berubah)