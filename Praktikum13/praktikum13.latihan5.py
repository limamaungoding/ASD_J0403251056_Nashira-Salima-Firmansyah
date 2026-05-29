# Nama  : Nashira Salima Firmansyah
# NIM : J0403251056
# Kelas : TPL A2
# Praktikum 13 - Graph III: Spanning Tree
import heapq

# ==============================================================================
# REPRESENTASI WEIGHTED GRAPH (KASUS 2: JARINGAN KOMPUTER)
# Menggunakan adjacency list untuk merepresentasikan router dan bobot jalurnya.
# ==============================================================================
graph = {
    'RouterA': {'RouterB': 3, 'RouterC': 2},
    'RouterB': {'RouterA': 3, 'RouterD': 5, 'RouterC': 4},
    'RouterC': {'RouterA': 2, 'RouterD': 1, 'RouterB': 4},
    'RouterD': {'RouterB': 5, 'RouterC': 1}
}

# ==============================================================================
# IMPLEMENTASI ALGORITMA PRIM
# Membangun MST dari satu titik awal secara bertahap menggunakan Min-Heap.
# ==============================================================================
def prim_mst(graph, start_node):
    visited = set([start_node]) # Menyimpan router yang sudah masuk jaringan MST
    edges = []                  # Priority queue (Min-Heap) untuk menampung kandidat edge
    mst = []                    # Menyimpan daftar edge yang terpilih menjadi MST
    total_weight = 0            # Akumulasi total bobot minimum
    
    # Memasukkan semua tetangga dari router awal ke dalam heap
    for neighbor, weight in graph[start_node].items():
        heapq.heappush(edges, (weight, start_node, neighbor))
        
    while edges:
        # Mengambil edge dengan bobot terkecil dari heap
        weight, u, v = heapq.heappop(edges)
        
        # Jika router tujuan belum dikunjungi, masukkan ke dalam jaringan MST
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight
            
            # Tambahkan semua edge baru dari router yang baru saja dikunjungi
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))
                    
    return mst, total_weight

# Menjalankan algoritma Prim dimulai dari 'RouterA'
mst_result, total_bobot = prim_mst(graph, 'RouterA')

# ==============================================================================
# OUTPUT PROGRAM
# ==============================================================================
print("==================================================")
print("Minimum Spanning Tree (MST) Jaringan Komputer:")
print("==================================================")
for u, v, weight in mst_result:
    print(f"Koneksi: {u} - {v} | Bobot: {weight}")
print("--------------------------------------------------")
print("Total Bobot Minimum =", total_bobot)
print("==================================================")


# ==============================================================================
# Pertanyaan Analisis: 
# 1. Kasus apa yang dipilih? 
# 2. Algoritma apa yang digunakan? 
# 3. Edge mana saja yang dipilih dalam MST? 
# 4. Berapa total bobot MST? 
# 5. Mengapa edge tertentu tidak dipilih?
# ==============================================================================
# Jawaban Analisis:
#
# 1. Kasus apa yang dipilih?
#    - Kasus yang dipilih adalah **Kasus 2: Jaringan Komputer**, yang melibatkan 
#      koneksi antar 4 router (RouterA, RouterB, RouterC, dan RouterD).
#
# 2. Algoritma apa yang digunakan?
#    - Algoritma yang digunakan adalah **Algoritma Prim**. Algoritma ini dipilih 
#      karena sangat efisien ketika diimplementasikan dengan priority queue 
#      (heapq) untuk mencari jalur terpendek dari struktur yang tumbuh secara lokal.
#
# 3. Edge mana saja yang dipilih dalam MST?
#    - Berdasarkan hasil eksekusi program, edge yang dipilih adalah:
#      1. RouterA - RouterC dengan bobot 2
#      2. RouterC - RouterD dengan bobot 1
#      3. RouterA - RouterB dengan bobot 3
#
# 4. Berapa total bobot MST?
#    - Total bobot MST yang dihasilkan adalah **6**.
#    - Hasil ini didapatkan dari akumulasi bobot edge terpilih: $2 + 1 + 3 = 6$.
#
# 5. Mengapa edge tertentu tidak dipilih?
#    - Edge **RouterB - RouterC (4)** dan **RouterB - RouterD (5)** tidak dipilih 
#      karena semua router (A, B, C, D) sudah berhasil terhubung ke dalam 
#      jaringan pohon sebelum edge-edge tersebut sempat diproses. 
#    - Di dalam kode, kondisi `if v not in visited` menyaring edge tersebut. Jika 
#      edge tersebut dipaksakan masuk, maka akan terbentuk loop/siklus (cycle) 
#      antar router yang justru membuat pengiriman data di dalam jaringan menjadi 
#      tidak efisien (redundan).
# ==============================================================================