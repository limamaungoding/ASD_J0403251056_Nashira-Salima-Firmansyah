# ==========================================================
# Latihan 1: Rekursi Pangkat
# Nama: Nashira Salima Firmansyah
# NIM: J0403251056
# Kelas: TPL A2
# ==========================================================
def pangkat(a, n):
    # Base case
    # Jika pangkat (n) sudah mencapai 0, hentikan pemanggilan dan kembalikan 1.
    if n == 0:
        return 1
    # Recursive case (memanggil diri sndiri)
    return a * pangkat(a, n - 1)

# Pemanggilan fungsi: 2 pangkat 4
# Proses: 2 * (2 * (2 * (2 * 1)))
print(pangkat(2, 4)) # Output: 16


