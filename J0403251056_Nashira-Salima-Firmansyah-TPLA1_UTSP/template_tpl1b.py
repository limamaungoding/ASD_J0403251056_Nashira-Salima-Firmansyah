# ==============================================================================
# UJIAN TENGAH PRAKTIKUM - ALGORITMA & STRUKTUR DATA (TPL2106)
# Nama    : Nashira Salima Firmansyah
# NIM     : J0403251056
# Kelas   : TPLA2
# ==============================================================================

# 1. FILE HANDLING & DICTIONARY (Sub-CPMK 1)
def muat_data_buku(nama_file):
    """
    Fungsi untuk membaca 'buku.txt' dan menyimpannya ke Dictionary.
    Format file: kode_buku,judul,harga
    """
    database_buku = {}
    
    try:
        with open(nama_file, 'r') as file:
            for baris in file:
                # Menghapus spasi/newline di awal/akhir dan membagi berdasarkan koma
                data = baris.strip().split(',')
                
                # Memastikan baris memiliki 3 elemen (kode, judul, harga)
                if len(data) == 3:
                    kode_buku, judul, harga = data
                    
                    # Simpan ke dictionary dengan kode_buku sebagai key
                    database_buku[kode_buku] = {
                        "judul": judul,
                        "harga": int(harga) # Mengubah harga menjadi integer
                    }
    except FileNotFoundError:
        print(f"Error: File {nama_file} tidak ditemukan.")
    
    return database_buku

# 2. LINKED LIST - MANAJEMEN PROMOSI (Sub-CPMK 2) [cite: 32]
class Node:
    def __init__(self, judul):
        self.judul = judul
        self.next = None

class LinkedListPromosi:
    def __init__(self):
        self.head = None

    def tambah_buku_promosi(self, judul):
        """Menambahkan buku ke daftar promosi (Linked List)"""
        baru = Node(judul)
        
        # Jika list masih kosong, jadikan node baru sebagai head
        if self.head is None:
            self.head = baru
            return
        
        # Jika tidak kosong, cari node terakhir (tail)
        current = self.head
        while current.next:
            current = current.next
        
        # Sambungkan node terakhir ke node baru
        current.next = baru

    def tampilkan_promosi(self):
        """Menampilkan semua buku dalam daftar promosi"""
        if self.head is None:
            print("Daftar promosi kosong.")
            return

        print("Daftar Buku Promosi:")
        current = self.head
        while current:
            print(f"- {current.judul}")
            current = current.next
# 3. QUEUE - ANTIREAN KASIR (Sub-CPMK 3) [cite: 33]
class AntreanKasir:
    def __init__(self):
        self.antrean = []

    def tambah_antrean(self, nama_pelanggan):
        """Menambah antrean (Enqueue)"""
        # Menambahkan pelanggan ke urutan paling belakang
        self.antrean.append(nama_pelanggan)
        print(f"Pelanggan '{nama_pelanggan}' telah masuk ke antrean.")

    def layani_pelanggan(self):
        """Menghapus antrean (Dequeue)"""
        # Pastikan antrean tidak kosong sebelum dihapus
        if not self.antrean:
            print("Antrean kosong, tidak ada pelanggan untuk dilayani.")
            return None
        
        # Mengambil (menghapus) pelanggan dari urutan paling depan (index 0)
        pelanggan_dilayani = self.antrean.pop(0)
        print(f"Melayani pelanggan: {pelanggan_dilayani}")
        return pelanggan_dilayani

    def tampilkan_antrean(self):
        """(Opsional) Menampilkan status antrean saat ini"""
        if not self.antrean:
            print("Status: Antrean kosong.")
        else:
            print(f"Status Antrean: {' -> '.join(self.antrean)}")

# 4. SORTING - LAPORAN TRANSAKSI (Sub-CPMK 4) [cite: 34]
def urutkan_transaksi(list_harga):
    """
    Mengurutkan list harga secara manual menggunakan 
    Insertion Sort (Ascending).
    """
    # Mulai dari elemen kedua (indeks 1) karena elemen pertama dianggap sudah terurut
    for i in range(1, len(list_harga)):
        key = list_harga[i]  # Elemen yang akan disisipkan
        j = i - 1
        
        # Geser elemen list_harga[0..i-1] yang lebih besar dari key
        # ke satu posisi di depan posisi mereka sekarang
        while j >= 0 and key < list_harga[j]:
            list_harga[j + 1] = list_harga[j]
            j -= 1
        
        # Tempatkan key pada posisi yang benar
        list_harga[j + 1] = key
        
    return list_harga

# Data dari soal
data_harga = [150000, 50000, 200000, 75000, 120000]

# Eksekusi
print("Harga sebelum urut:", data_harga)
harga_terurut = urutkan_transaksi(data_harga)
print("Harga setelah urut (Ascending):", harga_terurut)

# ==============================================================================
# MAIN PROGRAM - MENU ANTARMUKA
# ==============================================================================
def main():
    # Inisialisasi Data
    file_db = ".data/buku.txt"
    data_buku = muat_data_buku(file_db)
    list_promosi = LinkedListPromosi()
    antrean_toko = AntreanKasir()
    
    # Data dummy awal untuk laporan transaksi
    riwayat_transaksi = [150000, 50000, 200000, 75000, 120000]

    while True:
        print("\n" + "="*35)
        print("   SISTEM MANAJEMEN TOKO BUKU")
        print("="*35)
        print("1. Lihat Katalog Buku (Dictionary)")
        print("2. Kelola Daftar Promosi (Linked List)")
        print("3. Kelola Antrean Kasir (Queue)")
        print("4. Lihat Laporan Penjualan (Sorting)")
        print("5. Keluar")
        print("-" * 35)
        
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            print("\n--- KATALOG BUKU ---")
            if not data_buku:
                print("Katalog kosong atau file tidak ditemukan.")
            else:
                print(f"{'Kode':<10} | {'Judul Buku':<25} | {'Harga':<10}")
                print("-" * 50)
                for kode, info in data_buku.items():
                    print(f"{kode:<10} | {info['judul']:<25} | Rp{info['harga']:,}")
        
        elif pilihan == '2':
            print("\n--- MANAJEMEN PROMOSI ---")
            print("a. Tambah Buku Promosi")
            print("b. Tampilkan Daftar Promosi")
            sub_pil = input("Pilih (a/b): ").lower()
            
            if sub_pil == 'a':
                judul_baru = input("Masukkan judul buku untuk promosi: ")
                list_promosi.tambah_buku_promosi(judul_baru)
            elif sub_pil == 'b':
                list_promosi.tampilkan_promosi()
            else:
                print("Pilihan sub-menu tidak valid.")

        elif pilihan == '3':
            print("\n--- ANTREAN KASIR ---")
            print("a. Tambah Pelanggan ke Antrean")
            print("b. Layani Pelanggan (Dequeue)")
            print("c. Lihat Status Antrean")
            sub_pil = input("Pilih (a/b/c): ").lower()

            if sub_pil == 'a':
                nama = input("Nama Pelanggan Baru: ")
                antrean_toko.tambah_antrean(nama)
            elif sub_pil == 'b':
                antrean_toko.layani_pelanggan()
            elif sub_pil == 'c':
                antrean_toko.tampilkan_antrean()
            else:
                print("Pilihan tidak valid.")

        elif pilihan == '4':
            print("\n--- LAPORAN PENJUALAN ---")
            print("Harga Sebelum Urut:", riwayat_transaksi)
            # Gunakan copy() agar data asli tidak berubah jika ingin dibandingkan
            hasil_sort = urutkan_transaksi(riwayat_transaksi.copy())
            print("Harga Sesudah Urut (Ascending):", hasil_sort)

        elif pilihan == '5':
            print("\nProgram selesai. Selamat beristirahat, snekspie!")
            break
        else:
            print("\nPilihan tidak valid! Silakan masukkan angka 1-5.")

if __name__ == "__main__":
    main()