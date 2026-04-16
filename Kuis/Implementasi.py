# ==================================
# Nama: Nashira Salima Firmansyah
# NIM: J0403251056
# Kelas: TPL A2
# MATERI MERGE SORT
# ==================================

def merge_sort(arr) :
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

#  1. Kita siapkan list angka yang berantakan
data_angka = [38, 27, 43, 3, 9, 82, 10]
print(f"Data sebelum diurutkan: {data_angka}")

# 2. Panggil fungsi merge_sort
# Karena list di Python bersifat mutable, data_angka akan langsung berubah di tempat
merge_sort(data_angka)

# 3. Tampilkan hasil akhirnya
print(f"Data setelah diurutkan: {data_angka}")

