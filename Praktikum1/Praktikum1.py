
print("====Membuka file dalam 1 string ====")
with open('data_mahasiswa.txt', 'r',encoding="utf-8") as file:
    isi_file = file.read()
    print(isi_file)

    print("Tipe Data : ", type(isi_file))
# Latihan 1
    print("==== Membuka file per baris ====")
    with open("data_mahasiswa.txt", "r") as file:
        nomor = 1
        for baris in file:
            isi_bersih = baris.strip() 
            print(f"Baris ke- {nomor}")
            print(f"Isinya: {isi_bersih}")
            nomor += 1
# Latihan 2
with open('data_mahasiswa.txt', 'r',encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(',')
        print ("NIM :", nim, "| Nama :", nama, "| Nilai :", nilai)


data_list = [] #inisialisasi list untuk menampung data
# Latihan 3
with open('data_mahasiswa.txt', 'r',encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(',')
        data_list.append([nim, nama, int(nilai)])
print("menampilkan list")
print(data_list)
print("Contoh record ke-1", data_list[0])
print("Contoh record ke-2", data_list[1])

print("jumlah record", len(data_list))

data_dict = {}
with open('data_mahasiswa.txt', 'r',encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(',')
        data_dict[nim] = {
            'nama': nama,
            'nilai': int(nilai)
        }
print ("menampilkan dictionary")
print (data_dict)
