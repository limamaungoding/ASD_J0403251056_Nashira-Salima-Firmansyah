# ==========================================================
# Studi Kasus: Generator PIN
# Nama: Nashira Salima Firmansyah
# NIM: J0403251056
# Kelas: TPL A2
# ==========================================================
# Diskusi dan jelaskan: Bagaimana cara mencegah angka yang sama muncul berulang?
def buat_pin(panjang, hasil=""):
    if len(hasil) == panjang:
        print("PIN:", hasil)
        return
    for angka in ["0", "1", "2"]:
        if angka not in hasil:   # Mencegah angka yang sudah dipakai
            buat_pin(panjang, hasil + angka)

buat_pin(3)

