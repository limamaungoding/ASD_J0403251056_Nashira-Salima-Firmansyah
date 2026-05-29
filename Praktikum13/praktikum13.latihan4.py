# Nama  : Nashira Salima Firmansyah
# NIM : J0403251056
# Kelas : TPL A2
# Praktikum 13 - Graph III: Spanning Tree

import heapq

# ==============================================================================
# REPRESENTASI WEIGHTED GRAPH
# Menggunakan adjacency list untuk merepresentasikan gedung dan biaya kabel.
# ==============================================================================
graph = {
    'GedungA': {'GedungB': 4, 'GedungC': 2, 'GedungD': 5},
    'GedungB': {'GedungA': 4, 'GedungD': 3},
    'GedungC': {'GedungA': 2, 'GedungD': 1},
    'GedungD': {'GedungA': 5, 'GedungB': 3, 'GedungC': 1}
}

# ==============================================================================
# IMPLEMENTASI ALGORITMA PRIM
# Algoritma ini dipilih karena sangat efisien dalam mencari Minimum Spanning Tree
# pada graph yang direpresentasikan dengan adjacency list dan priority queue.
# ==============================================================================
def prim_mst(graph, start_node):
    visited = set([start_node]) # Menyimpan gedung yang sudah terhubung kabel
    edges = []                  # Priority queue untuk menyimpan kandidat kabel
    mst = []                    # Menyimpan hasil akhir jaringan kabel terpilih
    total_cost = 0              # Akumulasi biaya minimum
    
    # Masukkan semua jalur kabel dari gedung awal ke dalam priority queue
    for neighbor, weight in graph[start_node].items():
        heapq.heappush(edges, (weight, start_node, neighbor))
        
    while edges:
        # Ambil jalur kabel dengan biaya (bobot) paling murah
        weight, u, v = heapq.heappop(edges)
        
        # Jika gedung tujuan belum terhubung, pasang kabel ke gedung tersebut
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            total_cost += weight
            
            # Tambahkan semua kandidat kabel baru dari gedung yang baru terhubung
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))
                    
    return mst, total_cost

# Run program dengan titik awal 'GedungA'
mst_result, total_biaya = prim_mst(graph, 'GedungA')

# ==============================================================================
# OUTPUT PROGRAM
# ==============================================================================
print("==================================================")
print("Jaringan Kabel Terpilih (Minimum Spanning Tree):")
print("==================================================")
for u, v, weight in mst_result:
    print(f"Hubungkan {u} ke {v} dengan Biaya: {weight}")
print("--------------------------------------------------")
print("Total Biaya Minimum =", total_biaya)
print("==================================================")


# ==============================================================================
# Pertanyaan Analisis: 
# 1. Algoritma apa yang digunakan? 
# 2. Edge mana saja yang dipilih? 
# 3. Berapa total biaya minimum? 
# 4. Mengapa MST cocok digunakan pada kasus ini?
# ==============================================================================
# Jawaban Analisis:
#
# 1. Algoritma apa yang digunakan?
#    - Algoritma yang digunakan dalam program di atas adalah **Algoritma Prim**.
#    - Algoritma ini bekerja dengan cara memilih satu node acak sebagai awal, 
#      lalu secara serakah (greedy) menarik edge dengan bobot terkecil yang 
#      terhubung langsung dengan node-node yang sudah dikunjungi.
#
# 2. Edge mana saja yang dipilih?
#    - Berdasarkan hasil eksekusi program, edge (jalur kabel) yang dipilih adalah:
#      1. GedungA ke GedungC dengan biaya 2
#      2. GedungC ke GedungD dengan biaya 1
#      3. GedungD ke GedungB dengan biaya 3
#
# 3. Berapa total biaya minimum?
#    - Total biaya minimum untuk membangun jaringan kabel tersebut adalah **6**.
#    - Perhitungannya didapat dari penjumlahan edge terpilih: $2 + 1 + 3 = 6$.
#
# 4. Mengapa MST cocok digunakan pada kasus ini?
#    - Kasus ini meminta kita untuk menghubungkan **seluruh gedung** agar saling 
#      terkoneksi dalam satu jaringan internet dengan **biaya seminimal mungkin**.
#    - Karakteristik ini sangat sesuai dengan konsep **Minimum Spanning Tree (MST)**, 
#      di mana tujuannya adalah menghubungkan semua vertex (gedung) menggunakan 
#      jumlah edge (kabel) paling sedikit tanpa membentuk loop/cycle (redundansi) 
#      sehingga total bobot akumulatifnya menjadi paling efisien.
# ==============================================================================