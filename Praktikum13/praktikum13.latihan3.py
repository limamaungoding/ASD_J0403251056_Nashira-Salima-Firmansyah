# Nama  : Nashira Salima Firmansyah
# NIM : J0403251056
# Kelas : TPL A2
# Praktikum 13 - Graph III: Spanning Tree

import heapq 
graph = { 
'A': {'B': 4, 'C': 2, 'D': 5}, 
'B': {'A': 4, 'D': 3}, 
'C': {'A': 2, 'D': 1}, 
'D': {'A': 5, 'B': 3, 'C': 1} 
} 
def prim(graph, start): 
    visited = set([start]) 
    edges = [] 
    for neighbor, weight in graph[start].items(): 
        heapq.heappush(edges, (weight, start, neighbor)) 
    mst = [] 
    total_weight = 0 
    while edges: 
        weight, u, v = heapq.heappop(edges) 
        if v not in visited: 
            visited.add(v) 
            mst.append((u, v, weight)) 
            total_weight += weight 
            for neighbor, w in graph[v].items(): 
                if neighbor not in visited: 
                    heapq.heappush(edges, (w, v, neighbor)) 
    return mst, total_weight 

mst, total = prim(graph, 'A') 
print("Minimum Spanning Tree:") 
for edge in mst: 
    print(edge) 
print("Total bobot =", total) 

# ==============================================================================
# Pertanyaan Analisis: 
# 1. Node awal apa yang digunakan? 
# 2. Edge mana yang dipilih pertama kali? 
# 3. Bagaimana Prim menentukan edge berikutnya? 
# 4. Berapa total bobot MST yang dihasilkan? 
# 5. Apa perbedaan pendekatan Prim dan Kruskal?
# ==============================================================================
# Jawaban Analisis:
#
# 1. Node awal apa yang digunakan? 
#    - Node awal yang digunakan pada kode di atas adalah node 'A', sesuai dengan 
#      argumen yang dimasukkan saat pemanggilan fungsi: `prim(graph, 'A')`.
#
# 2. Edge mana yang dipilih pertama kali? 
#    - Edge yang dipilih pertama kali adalah ('A', 'C') dengan bobot 2. 
#    - Alasan: Setelah berada di node 'A', semua tetangga node 'A' dimasukkan 
#      ke dalam priority queue (heap). Karena bobot ke 'C' (2) lebih kecil 
#      daripada ke 'B' (4) dan 'D' (5), maka edge inilah yang diambil duluan.
#
# 3. Bagaimana Prim menentukan edge berikutnya? 
#    - Algoritma Prim menentukannya dengan cara melihat semua edge yang terhubung 
#      dari node-node yang sudah dikunjungi (`visited`) menuju ke node-node yang 
#      belum dikunjungi. 
#    - Semua kandidat edge tersebut disimpan di dalam Min-Heap, dan algoritma akan 
#      selalu mengambil edge dengan bobot terkecil (`heapq.heappop`) selama node 
#      tujuannya belum dikunjungi (tidak membentuk cycle).
#
# 4. Berapa total bobot MST yang dihasilkan? 
#    - Total bobot MST yang dihasilkan adalah 6.
#    - Urutan edge yang terbentuk adalah:
#      1. ('A', 'C') dengan bobot 2
#      2. ('C', 'D') dengan bobot 1
#      3. ('D', 'B') dengan bobot 3
#      Total akumulasi bobot: $2 + 1 + 3 = 6$.
#
# 5. Apa perbedaan pendekatan Prim dan Kruskal? 
#    - Algoritma Prim bekerja secara **lokal/tumbuh dari satu titik**. Ia mulai 
#      dari