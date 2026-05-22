# ==========================================================
# Praktikum 12: Weighted Graph dan Perhitungan Jalur
# Nama: Nashira Salima Firmansyah
# NIM : J0403251056
# ==========================================================

# ==========================================================
# Latihan 4: Studi Kasus Jalur Terpendek Lokasi Kampus
# Algoritma: Dijkstra
# ==========================================================
import heapq
# Graph lokasi kampus
# Bobot menunjukkan waktu tempuh dalam menit
graph = {
    'Gerbang': {'Perpustakaan': 6, 'Kantin': 2},
    'Perpustakaan': {'Lab': 3},
    'Kantin': {'Lab': 4, 'Aula': 7},
    'Lab': {'Aula': 1},
    'Aula': {}
}
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

        if distance < distances[neighbor]:
            distances[neighbor] = distance
            heapq.heappush(priority_queue, (distance, neighbor))
    return distances
hasil = dijkstra(graph, 'Gerbang')

print("Jarak terpendek dari Gerbang Kampus:")
for lokasi, jarak in hasil.items():
    print(lokasi, "=", jarak, "menit")

# Pertanyaan Analisis:
# 1. Lokasi mana yang paling dekat dari Gerbang?
# 2. Berapa waktu tempuh terpendek dari Gerbang ke Aula?
# 3. Apakah jalur langsung selalu menghasilkan jarak paling kecil? Jelaskan.
# 4. Mengapa Dijkstra cocok digunakan pada kasus lokasi kampus ini?

# Jawaban Analisis:
# 1. Lokasi yang paling dekat dari Gerbang adalah Kantin dengan waktu tempuh 2 menit.
# 2. Waktu tempuh terpendek dari Gerbang ke Aula adalah 7 menit (melalui Kantin dan Lab).
# 3. Jalur langsung tidak selalu menghasilkan jarak paling kecil karena bobot pada edge (waktu tempuh) dapat berbeda. 
#    Dalam kasus ini, meskipun ada jalur langsung dari Gerbang ke Aula melalui Kantin, jalur tersebut memiliki waktu 
#    tempuh yang lebih lama dibandingkan dengan jalur melalui Perpustakaan dan Lab.
# 4. Dijkstra cocok digunakan pada kasus lokasi kampus ini karena graph yang digunakan memiliki bobot positif (waktu tempuh), 
#    dan algoritma Dijkstra dapat dengan efisien menemukan jarak terpendek dari satu node ke semua node lainnya dalam graph tersebut.

