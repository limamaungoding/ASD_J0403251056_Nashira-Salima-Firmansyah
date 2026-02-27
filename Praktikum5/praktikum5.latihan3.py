# ==========================================================
# Latihan 3: Mencari Nilai Maksimum
# Nama: Nashira Salima Firmansyah
# NIM: J0403251056
# Kelas: TPL A2
# ==========================================================
def cari_maks(data, index=0):
    # Base case
    if index == len(data) - 1:
        return data[index] #mengembalikan ke nilai terakhir jika sudah di elemen terakhir
    
    # Recursive case untuk cek sisa elemen after current index
    maks_sisa = cari_maks(data, index + 1) #maju one step
    #membandingkan current data dengan hasil sisa list
    if data[index] > maks_sisa:
        return data[index]
    else:
        return maks_sisa

angka = [3, 7, 2, 9, 5]
print("Nilai maksimum:", cari_maks(angka))

