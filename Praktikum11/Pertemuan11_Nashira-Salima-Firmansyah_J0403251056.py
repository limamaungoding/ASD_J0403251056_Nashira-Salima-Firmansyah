"""
Praktikum 11 - Representasi Graph
Nama: Nashira Salima Firmansyah
NIM : J0403251056

Isi praktikum:
16. Membuat adjacency matrix
17. Membuat adjacency list
18. Konversi adjacency matrix ke adjacency list
19. Studi kasus dunia nyata - Peta Kota
"""


def tampilkan_matrix(matrix, nodes=None):
    """Menampilkan adjacency matrix dengan label node."""
    if nodes is None:
        nodes = list(range(len(matrix)))

    print("    " + " ".join(str(node) for node in nodes))
    for node, row in zip(nodes, matrix):
        print(f"{node} : " + " ".join(str(value) for value in row))


def tampilkan_adjacency_list(graph):
    """Menampilkan adjacency list."""
    for node, neighbors in graph.items():
        print(f"{node} -> {neighbors}")


def matrix_ke_list(matrix, nodes=None):
    """Mengubah adjacency matrix menjadi adjacency list."""
    if nodes is None:
        nodes = list(range(len(matrix)))

    adjacency_list = {}
    for i, node in enumerate(nodes):
        adjacency_list[node] = []
        for j, value in enumerate(matrix[i]):
            if value == 1:
                adjacency_list[node].append(nodes[j])
    return adjacency_list


def buat_matrix_tidak_berarah(nodes, edges):
    """Membuat adjacency matrix untuk graph tidak berarah."""
    index = {node: i for i, node in enumerate(nodes)}
    matrix = [[0 for _ in nodes] for _ in nodes]

    for asal, tujuan in edges:
        i = index[asal]
        j = index[tujuan]
        matrix[i][j] = 1
        matrix[j][i] = 1

    return matrix


def buat_list_tidak_berarah(nodes, edges):
    """Membuat adjacency list untuk graph tidak berarah."""
    graph = {node: [] for node in nodes}

    for asal, tujuan in edges:
        graph[asal].append(tujuan)
        graph[tujuan].append(asal)

    return graph


print("=" * 60)
print("16. Praktikum 1 - Membuat Adjacency Matrix")
print("=" * 60)

# Graph:
# 0 --- 1
# |    /
# |   /
# 2 --- 3
nodes_16 = [0, 1, 2, 3]
edges_16 = [
    (0, 1),
    (0, 2),
    (1, 2),
    (2, 3),
]
matrix_16 = buat_matrix_tidak_berarah(nodes_16, edges_16)

print("Adjacency Matrix:")
tampilkan_matrix(matrix_16, nodes_16)

print("\nArti setiap baris:")
print("Baris 0: node 0 terhubung dengan node 1 dan 2.")
print("Baris 1: node 1 terhubung dengan node 0 dan 2.")
print("Baris 2: node 2 terhubung dengan node 0, 1, dan 3.")
print("Baris 3: node 3 terhubung dengan node 2.")


print("\n" + "=" * 60)
print("17. Praktikum 2 - Membuat Adjacency List")
print("=" * 60)

# Graph:
# A --- B
# |     |
# C --- D
graph_17 = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"],
}

print("Adjacency List:")
tampilkan_adjacency_list(graph_17)


print("\n" + "=" * 60)
print("18. Praktikum 3 - Konversi Matrix ke List")
print("=" * 60)

matrix_18 = [
    [0, 1, 1, 0],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [0, 0, 1, 0],
]

nodes_18 = ["A", "B", "C", "D"]
graph_18 = matrix_ke_list(matrix_18, nodes_18)

print("Matrix awal:")
tampilkan_matrix(matrix_18, nodes_18)
print("\nHasil konversi ke adjacency list:")
tampilkan_adjacency_list(graph_18)


print("\n" + "=" * 60)
print("19. Praktikum 4 - Studi Kasus Dunia Nyata")
print("=" * 60)
print("Digit akhir NIM: 6")
print("Studi kasus    : Peta Kota")

nodes_kota = ["Bogor", "Depok", "Jakarta", "Bandung", "Sukabumi"]
edges_kota = [
    ("Bogor", "Depok"),
    ("Bogor", "Sukabumi"),
    ("Depok", "Jakarta"),
    ("Depok", "Sukabumi"),
    ("Jakarta", "Bandung"),
    ("Bandung", "Sukabumi"),
]

graph_kota = buat_list_tidak_berarah(nodes_kota, edges_kota)
matrix_kota = buat_matrix_tidak_berarah(nodes_kota, edges_kota)

print("\nNode / Vertex:")
for kota in nodes_kota:
    print(f"- {kota}")

print("\nEdge / Hubungan antar kota:")
for asal, tujuan in edges_kota:
    print(f"- {asal} terhubung dengan {tujuan}")

print("\nAdjacency List Peta Kota:")
tampilkan_adjacency_list(graph_kota)

print("\nAdjacency Matrix Peta Kota:")
tampilkan_matrix(matrix_kota, nodes_kota)
