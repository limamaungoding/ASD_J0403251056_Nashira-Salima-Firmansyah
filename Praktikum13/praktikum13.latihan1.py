# Nama  : Nashira Salima Firmansyah
# NIM : J0403251056
# Kelas : TPL A2
# Praktikum 13 - Graph III: Spanning Tree

# ==========================================
# LATIHAN 1
# ==========================================

# 1. Menampilkan daftar edge pada graph (Memakai List of Tuples)
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('C', 'D'),
    ('B', 'D')
]

# 2. Menampilkan contoh spanning tree yang valid
# (Menghubungkan semua vertex A, B, C, D tanpa membentuk loop/cycle)
spanning_tree = [
    ('A', 'C'),
    ('C', 'D'),
    ('D', 'B')
]

# Output Daftar Edge pada Graph
print("Edge pada graph:")
for edge in edges:
    print(edge)

# Output Daftar Edge pada Spanning Tree
print("\nSpanning Tree:")
for edge in spanning_tree:
    print(edge)

# 3 & 4. Menampilkan jumlah edge awal dan jumlah edge spanning tree
print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))


# ==============================================================================
# Pertanyaan Analisis
# 1. Apa perbedaan graph awal dan spanning tree? 
# 2. Mengapa spanning tree tidak boleh memiliki cycle? 
# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit? 
# ==============================================================================
# Jawaban Analisis:
#
# 1. Apa perbedaan graph awal dan spanning tree?
#    - Graph awal (original graph) adalah struktur data yang berisi semua vertex 
#      dan semua edge yang menghubungkan vertex tersebut, di mana jalurnya bisa 
#      memiliki sirkuit/siklus (cycle) atau rute ganda antar vertex.
#    - Spanning tree adalah subgraph (bagian dari graph awal) yang wajib 
#      menghubungkan seluruh vertex yang ada tanpa membentuk siklus (cycle) sama sekali.
#
# 2. Mengapa spanning tree tidak boleh memiliki cycle?
#    - Karena secara definisi matematis, sebuah "tree" (pohon) dalam teori graph 
#      adalah graph terhubung yang tidak memiliki siklus (acyclic connected graph). 
#      Jika terdapat cycle, maka struktur tersebut kembali menjadi graph biasa dan 
#      kehilangan sifat efisiensi jalur tunggal khas sebuah pohon.
#
# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit?
#    - Spanning tree bertujuan untuk menghubungkan semua titik dengan jumlah 
#      jalur seminimal mungkin. Jika sebuah graph memiliki $V$ buah vertex, 
#      maka spanning tree-nya akan selalu memiliki tepat $V - 1$ edge. 
#      Pada kasus ini, ada 4 vertex (A, B, C, D), sehingga spanning tree hanya 
#      membutuhkan 3 edge. Jumlah ini pasti lebih sedikit dari graph awal yang 
#      memiliki edge redundan (total 5 edge).
# ==============================================================================