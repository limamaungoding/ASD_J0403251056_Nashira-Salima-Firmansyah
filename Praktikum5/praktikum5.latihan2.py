# ==========================================================
# Latihan 2: Tracing Rekursi
# Nama: Nashira Salima Firmansyah
# NIM: J0403251056
# Kelas: TPL A2
# ==========================================================

def countdown(n):
    # BASE CASE
    if n == 0:
        print("Selesai")
        return
    
    #dieksekusi sebelum masuk rekursi (turun)
    print("Masuk:", n)
    #memanggil diri sendiri
    countdown(n - 1)
    #execute after rekursi selesai
    print("Keluar:", n)

countdown(3)
#keluar terbalik karena sistem last in first out