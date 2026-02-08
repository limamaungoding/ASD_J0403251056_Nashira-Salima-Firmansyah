# ==========================================================
# Praktikum 1: ADT & File Handling (Studi Kasus: Data Mahasiswa)
# Latihan 1: Load data dari file ke Dictionary
# ==========================================================

nama_file ="data_mahasiswa.txt"

def baca_data(nama_file):
    """
    Membaca data mahasiswa dari file.
    Format per baris: NIM,NAMA,NILAI
    Output:
    - data_dict (dictionary)
    key = NIM
    value = {"nama": NAMA, "nilai": NILAI(int)}
    """
    data_dict = {}
    with open(nama_file, 'r', encoding="utf-8") as file:
        for baris in file : 
            baris = baris.strip() #mengambil data perbaris
            nim, nama, nilai = baris.split(",") #ambil data per item data
            data_dict[nim]= {"nama": nama, "nilai": int(nilai)} #masukkan dalam dictionary 
    return data_dict

buka_data = baca_data(nama_file)
print ("Jumlah data terbaca", len(buka_data))


# ==========================================================
# Praktikum 1: ADT & File Handling (Studi Kasus: Data Mahasiswa)
# Latihan 2: Tampilkan semua data mahasiswa
# ==========================================================

def tampilkan_data(data_dict):
    print("\n======= Daftar Mahasiswa =======")
    print(f"{'NIM': <10} | {'Nama': <12} | {'Nilai':>5}")
    print("-"*33) #membuat garis

    for nim in sorted(data_dict.keys()):
        nama = data_dict[nim]["nama"]
        nilai = data_dict [nim] ["nilai"]
        print(f"{nim:<10} | {nama:<12} | {int(nilai):>5}")
    

#tampilkan_data(buka_data)
#Searching

# ==========================================================
# Praktikum 1: ADT & File Handling (Studi Kasus: Data Mahasiswa)
# Latihan 3: Cari data berdasarkan NIM
# ==========================================================

def cari_data(data_dict):
    nim_cari = input("Masukkan NIM Mahasiswa yang ingin dicari: ").strip()

    if nim_cari in data_dict:
        nama = data_dict[nim_cari] ["nama"]
        nilai = data_dict[nim_cari] ["nilai"]

        print("\n======= Daftar Mahasiswa Ditemukan =======")
        print(f"NIM     : {nim_cari}")
        print(f"Nama    : {nama}")
        print(f"Nilai   : {nilai}")
    else:
        print("Data tidak ditemukan. Pastikan NIM yang dimasukkan benar")

#memanggil fungsi search data(cari data)
#cari_data(buka_data)

# ==========================================================
# Praktikum 1: ADT & File Handling (Studi Kasus: Data Mahasiswa)
# Latihan 4: Update nilai mahasiswa (ubah nilai)
# ==========================================================

#Membuat fungsi update data
def ubah_data(data_dict):
    nim = input("Masukkan NIM mahasiswa yang ingin diubah datanya: ").strip()

    if nim not in data_dict:
        print("NIM Tidak ditemukan. Update dibatalkan")
        return
    
    try:
        nilai_baru = int(input("Masukkan nilai baru 0-100: ").strip())
    except ValueError:
        print("Nilai harus berupa angka. Update dibatalkan")

    if nilai_baru < 0 or nilai_baru > 100:
        print("Nilai harus diantara 0 sampai 100. Update dibatalkan")

    nilai_lama = data_dict[nim]["nilai"]
    data_dict[nim]["nilai"] = nilai_baru

    print(f"Update Berhasil. Nilai {nim} berubah dari {nilai_lama} menjadi {nilai_baru}")

#Memanggil fungsi ubah data
#ubah_data(buka_data)

# ==========================================================
# Praktikum 1: ADT & File Handling (Studi Kasus: Data Mahasiswa)
# Latihan 5: Simpan perubahan data mahasiswa (save)
# ==========================================================

#Simpan Data
def simpan_data(nama_file, data_dict):
    with open(nama_file, "w", encoding="utf-8") as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]["nama"]
            nilai = data_dict [nim] ["nilai"]
            file.write(f"{nim},{nama},{nilai}\n")

#Memanggil fungsi simpan data
#print("\nData Berhasil Disimpan ke File: ", nama_file)
#simpan_data(nama_file, buka_data)

# ==========================================================
# Praktikum 1: ADT & File Handling (Studi Kasus: Data Mahasiswa)
# Latihan 6: Menu interaktif
# ==========================================================

#fungsi yang dijalankan pertama kali (menggunakan main)
def main():
    buka_data = baca_data(nama_file)

    while True:
        print("\n=== MENU DATA MAHASISWA ===")
        print("1. Tampilkan Data Mahasiswa")
        print("2. Cari Data Mahasiswa")
        print("3. Ubah Nilai Mahasiswa")
        print("4. Simpan Data ke File")
        print("0. Keluar")

        pilihan = input("Pilih Menu: ").strip()

        if pilihan == "1":
            tampilkan_data(buka_data)
        elif pilihan == "2":
            cari_data(buka_data)
        elif pilihan == "3":
            ubah_data(buka_data)
        elif pilihan == "4":
            simpan_data(nama_file, buka_data)
            print("Data Berhasil Disimpan")
        elif pilihan == "0":
            print("Program Selesai")
            break
        else:
            print("Pilihan tidak valid. Silahkan coba lagi")

if __name__ == "__main__":
    main()
            
        




