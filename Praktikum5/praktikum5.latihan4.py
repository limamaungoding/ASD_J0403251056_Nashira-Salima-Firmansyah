# ==========================================================
# Latihan 4: Kombinasi Huruf
# Nama: Nashira Salima Firmansyah
# NIM: J0403251056
# Kelas: TPL A2
# ==========================================================
def kombinasi(n, hasil=""):
    #if panjang string = n
    if len(hasil) == n:
        print(hasil)
        return
    # menambah 2 kemungkinan, A atau B
    kombinasi(n, hasil + "A")
    kombinasi(n, hasil + "B")
kombinasi(2)

#karena tiap langkah bercabang 2, maka total kombinasinya adalah
#2 * 2 = 4 
#4 kombinasi