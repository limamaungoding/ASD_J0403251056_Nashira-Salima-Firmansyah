# Nama  : Nashira Salima Firmansyah
# NIM : J0403251056
# Kelas : TPL A2
# Praktikum 13 - Graph III: Spanning Tree

# ========================================================== 
# Implementasi Sederhana Algoritma Kruskal 
# ========================================================== 

# Daftar edge: (bobot, node1, node2) 
edges = [ 
    (1, 'C', 'D'), 
    (2, 'A', 'C'), 
    (3, 'B', 'D'), 
    (4, 'A', 'B'), 
    (5, 'A', 'D') 
] 

# Mengurutkan edge berdasarkan bobot terkecil 
edges.sort() 

mst = [] 
total_weight = 0 
connected = set() 

for weight, u, v in edges: 
    # Memilih edge yang tidak membentuk cycle sederhana
    if u not in connected or v not in connected: 
        mst.append((u, v, weight)) 
        total_weight += weight 
        connected.add(u) 
        connected.add(v) 

print("Minimum Spanning Tree:") 
for edge in mst: 
    print(edge) 

print("Total bobot =", total_weight)

# ==============================================================================
# Pertanyaan Analisis
# 1. Edge mana yang dipilih pertama kali? 
# 2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu? 
# 3. Berapa total bobot MST yang dihasilkan? 
# 4. Mengapa edge tertentu tidak dipilih? 
# ==============================================================================
# Jawaban Analisis:
#
# 1. Edge mana yang dipilih pertama kali?
#    - Edge yang dipilih pertama kali adalah ('C', 'D') dengan bobot 1.
#    - Hal ini terjadi karena algoritma Kruskal adalah algoritma greedy yang 
#      memproses edge berdasarkan urutan bobot dari yang terkecil setelah 
#      dilakukan proses pengurutan (sorting).
#
# 2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu?
#    - Karena tujuan utama dari algoritma Kruskal adalah untuk mencari "Minimum" 
#      Spanning Tree (MST), yaitu pohon merentang dengan total bobot akumulatif 
#      paling minimal. Dengan selalu memilih bobot terkecil terlebih dahulu 
#      (strategi greedy), algoritma memastikan efisiensi biaya/bobot di setiap 
#      langkahnya.
#
# 3. Berapa total bobot MST yang dihasilkan?
#    - Total bobot MST yang dihasilkan adalah 6.
#    - Berdasarkan logika kode di atas, edge yang sukses terpilih masuk ke MST 
#      adalah ('C', 'D') bobot 1, ('A', 'C') bobot 2, dan ('B', 'D') bobot 3. 
#      Maka totalnya: $1 + 2 + 3 = 6$.
#
# 4. Mengapa edge tertentu tidak dipilih?
#    - Edge ('A', 'B') dengan bobot 4 dan ('A', 'D') dengan bobot 5 tidak dipilih 
#      karena semua node (A, B, C, dan D) sudah berhasil terhubung ke dalam sistem 
#      (semuanya sudah masuk ke dalam `connected` set). 
#    - Jika edge tersebut dipaksakan masuk, maka kondisi `u not in connected or 
#      v not in connected` akan bernilai False, mencegah terjadinya siklus (cycle) 
#      redundandan menjaga struktur data tetap berupa pohon (tree).
# ==============================================================================