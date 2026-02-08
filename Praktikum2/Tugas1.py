# ==========================================================
# TUGAS HANDS-ON MODUL 1
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File .txt)
#
# Nama : Nashira Salima Firmansyah
# NIM : J0403251056
# Kelas : TPL A2
# ==========================================================

# -------------------------------
# Konstanta nama file
# -------------------------------
nama_file = "stok_barang.txt"

# -------------------------------
# Fungsi: Membaca data dari file
# -------------------------------

def baca_stok(nama_file):
    """
    Membaca data stok dari file teks.
    Format per baris: KodeBarang,NamaBarang,Stok
    Output:
    - stok_dict (dictionary)
    key = kode_barang
    value = {"nama": nama_barang, "stok": stok_int}
    """
    stok_dict = {}
# # TODO: Buka file dan baca seluruh baris (DONE)
# # Hint: with open(nama_file, "r", encoding="utf-8") as f: (DONE)
    with open(nama_file, 'r', encoding="utf-8") as file:

# # TODO: Untuk setiap baris:
# # - gunakan strip() untuk menghilangkan \n (DONE)
# # - split(",") untuk memisahkan kolom (DONE)
# # - simpan ke dictionary (DONE)
#     return stok_dict (DONE)
        for baris in file : 
                baris = baris.strip() #mengambil data perbaris
                KodeBarang, NamaBarang, Stok = baris.split(",") #ambil data per item data
                stok_dict[KodeBarang]= {"nama barang": NamaBarang, "stok": int(Stok)} #masukkan dalam dictionary 
        return stok_dict

    

# # -------------------------------
# # Fungsi: Menyimpan data ke file
# # -------------------------------
def simpan_stok(nama_file, stok_dict):
     
    """
    Menyimpan seluruh data stok ke file teks.
    Format per baris: KodeBarang,NamaBarang,Stok
    """
     
# # TODO: Tulis ulang seluruh isi file berdasarkan stok_dict  
# # Hint: with open(nama_file, "w", encoding="utf-8") as f:(DONE)

    with open(nama_file,"w", encoding="utf-8") as file:
          for KodeBarang in sorted(stok_dict.keys()):
               NamaBarang = stok_dict [KodeBarang]["nama barang"]
               stok = stok_dict [KodeBarang]["stok"]
               file.write(f"{KodeBarang}, {NamaBarang}, {stok}\n")
pass

# # -------------------------------
# # Fungsi: Menampilkan semua data
# # -------------------------------
def tampilkan_semua(stok_dict):

    """
    Menampilkan semua barang di stok_dict.
    """

# # TODO: Jika kosong, tampilkan pesan stok kosong (DONE)
# # TODO: Tampilkan dengan format rapi: kode | nama | stok (DONE)

    if not stok_dict:
         print("\n Stok masih kosong")
         return
    print("\n======= Daftar Stok Barang =======")
    print(f"{'Kode Barang': <10} | {'Nama Barang': <12} | {'Stok':>5}")
    print("-"*33) #membuat garis

    for KodeBarang in sorted(stok_dict.keys()):
        NamaBarang = stok_dict[KodeBarang]["nama barang"]
        stok = stok_dict [KodeBarang]["stok"]
        print(f"{KodeBarang:<10} | {NamaBarang:<12} | {int(stok):>5}")
pass         



# # -------------------------------
# # Fungsi: Cari barang berdasarkan kode
# # -------------------------------
def cari_barang(stok_dict):
    """
    Mencari barang berdasarkan kode barang.
    """

    KodeBarang = input("Masukkan kode barang: ").strip()

# # TODO: Cek apakah kode ada di dictionary
# # Jika ada: tampilkan detail barang (DONE)
# # Jika tidak ada: tampilkan 'Barang tidak ditemukan' (DONE)

    if KodeBarang in stok_dict:
        NamaBarang = stok_dict[KodeBarang]["nama barang"]
        stok = stok_dict [KodeBarang]["stok"]

        print("\n======= Detail Barang Ditemukan =======")
        print(f"Kode Barang     : {KodeBarang}")
        print(f"Nama Barang    : {NamaBarang}")
        print(f"Stok   : {stok}")
    else:
        print("Barang tidak ditemukan. Pastikan Kode Barang yang dimasukkan benar")
pass

# # -------------------------------
# # Fungsi: Tambah barang baru
# # -------------------------------

def tambah_barang(stok_dict):

    """
    Menambah barang baru ke stok_dict.
    """

    KodeBarang = input("Masukkan kode barang baru: ").strip()

# # TODO: Validasi kode tidak boleh duplikat
# # Jika sudah ada: tampilkan 'Kode sudah digunakan' dan return (done)
    
    if KodeBarang in stok_dict:
        print("Kode sudah digunakan. Gunakan kode lain")
        return

    NamaBarang = input("Masukkan nama barang: ").strip()

    nama_terdaftar = [item["nama barang"].lower() for item in stok_dict.values()]

# # TODO: Input stok awal (integer) (done)
# # Hint: stok_awal = int(input(...))
# # TODO: Simpan ke dictionary (done)

    if NamaBarang.lower() in nama_terdaftar:
        print(f"Gagal: Barang dengan nama '{NamaBarang}' sudah terdaftar!")
        return
    
    try:
        stok_awal = int(input("Masukkan jumlah stock awal: "))
    except ValueError:
        print("Gagal: stock harus berupa angka!")
        return
    
    stok_dict[KodeBarang] = {
        "nama barang" : NamaBarang,
        "stok" : stok_awal
    }
    print(f"\nSukses! {NamaBarang} dengan kode {KodeBarang} berhasil ditambahkan!")
pass




# # -------------------------------
# # Fungsi: Update stok barang
# # -------------------------------
def update_stok(stok_dict):
    """
    Mengubah stok barang (tambah atau kurangi).
    Stok tidak boleh menjadi negatif.
    """
# TODO: Cek apakah kode ada di dictionary
# # Jika tidak ada: tampilkan pesan dan return (DONE)

    KodeBarang = input("Masukkan kode barang yang ingin diupdate: ").strip()

    if KodeBarang not in stok_dict:
        print("Gagal: Kode barang tidak ditemukan")
        return

    NamaBarang = stok_dict[KodeBarang]["nama barang"]
    stok_sekarang = stok_dict[KodeBarang]["stok"]
    print(f"\nBarang: {NamaBarang} | Stok saat ini: {stok_sekarang}")

    while True:
        print("\nPilih jenis update:")
        print("1. Tambah stok")
        print("2. Kurangi stok")

# # TODO: Input jumlah perubahan stok
# # Hint: jumlah = int(input("Masukkan jumlah: ")) (DONE)
        pilihan_update = input("Masukkan pilihan (1/2): ").strip()

# # TODO:
# # - Jika pilihan 1: stok = stok + jumlah (DONE)
# # - Jika pilihan 2: stok = stok - jumlah (DONE)
# # - Jika hasil < 0: batalkan dan tampilkan error (DONE)
        if pilihan_update in ["1", "2"]:
            try:
                jumlah = int(input("Masukkan Jumlah: "))
                if jumlah < 0:
                    print("Gagal: Jumlah tidak boleh negatif")
                    continue
                if pilihan_update == "1":
                    stok_dict[KodeBarang]["stok"] += jumlah
                    print(f"Berhasil! Stok baru {NamaBarang}: {stok_dict[KodeBarang]['stok']}")
                    break
                elif pilihan_update == "2":
                    if stok_sekarang - jumlah < 0:
                        print(f"Gagal! Stok tidak cukup. Stok saat ini: {stok_sekarang}")
                    else:
                        stok_dict[KodeBarang]["stok"] -= jumlah
                        print(f"Berhasil! Stok baru {NamaBarang}: {stok_dict[KodeBarang]["stok"]}")
                    break
            except ValueError:
                print("Error! Masukkan angka yang valid")
        else:
            print("Pilihan tidak valid. Silahkan pilih 1 atau 2")

pass

# # -------------------------------
# # Program Utama
# # -------------------------------

def main():
# Membaca data dari file saat program mulai
    stok_barang = baca_stok(nama_file)
    while True:
        print("\n=== MENU STOK KANTIN ===")
        print("1. Tampilkan semua barang")
        print("2. Cari barang berdasarkan kode")
        print("3. Tambah barang baru")
        print("4. Update stok barang")
        print("5. Simpan ke file")
        print("0. Keluar")
        pilihan = input("Pilih menu: ").strip()
        if pilihan == "1":
            tampilkan_semua(stok_barang)
        elif pilihan == "2":
            cari_barang(stok_barang)
        elif pilihan == "3":
            tambah_barang(stok_barang)
        elif pilihan == "4":
            update_stok(stok_barang)
        elif pilihan == "5":
            simpan_stok(nama_file, stok_barang)
            print("Data berhasil disimpan.")
        elif pilihan == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silahkan coba lagi")

# Menjalankan program utama
if __name__ == "__main__":
    main()