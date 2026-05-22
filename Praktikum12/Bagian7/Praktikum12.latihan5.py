# ==========================================================
# Praktikum 12: Weighted Graph dan Perhitungan Jalur
# Nama: Nashira Salima Firmansyah
# NIM : J0403251056
# ==========================================================

# ==========================================================
# Praktikum 12: Weighted Graph dan Perhitungan Jalur
# ==========================================================
import heapq
# Graph berbobot yang merepresentasikan hubungan antar kota
graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},
    'Depok': {'Jakarta': 2, 'Bandung': 6},
    'Jakarta': {'Bandung': 7},
    'Bandung': {}
}
def dijkstra(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Dijkstra.
    """
    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}
    # Jarak dari start ke start adalah 0
    distances[start] = 0
    # Priority queue menyimpan pasangan (jarak, node)
    priority_queue = [(0, start)]
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        # Jika jarak saat ini lebih besar dari jarak yang sudah tercatat,
        # maka proses dilewati
        if current_distance > distances[current_node]:
            continue
        # Periksa semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
        # Jika ditemukan jarak yang lebih kecil, perbarui jaraknya
        if distance < distances[neighbor]:
            distances[neighbor] = distance
        heapq.heappush(priority_queue, (distance, neighbor))
    return distances
hasil = dijkstra(graph, 'Bogor')
print("Jarak terpendek dari Bogor:")
for node, distance in hasil.items():
    print("Bogor ->", node, "=", distance)

# Pertanyaan Analisis:
# 1. Node awal yang digunakan apa?
# 2. Node mana yang memiliki jarak paling kecil dari node awal?
# 3. Node mana yang memiliki jarak paling besar dari node awal?
# 4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus yang Anda buat.

# Jawaban Analisis:
# 1. Node awal yang digunakan adalah Bogor.
# 2. Node yang memiliki jarak paling kecil dari node awal adalah Bogor dengan jarak 0, karena itu adalah node awalnya sendiri.
# 3. Node yang memiliki jarak paling besar dari node awal adalah Bandung dengan jarak 8.
# 4. Algoritma Dijkstra bekerja dengan memulai dari node awal (Bogor) dan secara iteratif memperbarui jarak ke node tetangga 
#    berdasarkan bobot edge yang menghubungkan mereka. Algoritma menggunakan priority queue untuk memastikan bahwa node dengan 
#    jarak terpendek diproses terlebih dahulu. Proses ini terus berlanjut hingga semua node telah diproses, menghasilkan jarak 
#    terpendek dari node awal ke semua node lainnya dalam graph.