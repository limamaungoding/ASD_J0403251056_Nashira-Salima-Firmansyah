# ==========================================================
# Praktikum 12: Weighted Graph dan Perhitungan Jalur
# Nama: Nashira Salima Firmansyah
# NIM : J0403251056
# ==========================================================


# ==========================================================
# Latihan 1: Weighted Graph dan Perhitungan Jalur
# ==========================================================
# Representasi weighted graph menggunakan dictionary bersarang
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}
# Menghitung dua kemungkinan jalur dari A ke D
jalur_1 = graph['A']['B'] + graph['B']['D'] # A -> B -> D
jalur_2 = graph['A']['C'] + graph['C']['D'] # A -> C -> D
print("Jalur 1: A -> B -> D =", jalur_1)
print("Jalur 2: A -> C -> D =", jalur_2)
if jalur_1 < jalur_2:
     print("Jalur terpendek adalah A -> B -> D")
else:
    print("Jalur terpendek adalah A -> C -> D")

# Pertanyaan Analisis:
# 1. Berapa total bobot jalur A -> B -> D?
# 2. Berapa total bobot jalur A -> C -> D?
# 3. Jalur mana yang dipilih sebagai jalur terpendek?
# 4. Mengapa jalur terpendek tidak selalu ditentukan dari jumlah edge yang paling sedikit?

# Jawaban Analisis:
# 1. Total bobot jalur A -> B -> D adalah 4 (A ke B) + 5 (B ke D) = 9.
# 2. Total bobot jalur A -> C -> D adalah 2 (A ke C) + 1 (C ke D) = 3.
# 3. Jalur terpendek yang dipilih adalah A -> C -> D karena memiliki total bobot yang lebih rendah (3) dibandingkan dengan jalur A -> B -> D (9).
# 4. Jalur terpendek tidak selalu ditentukan dari jumlah edge yang paling sedikit karena bobot pada setiap edge dapat berbeda. Jalur dengan 
#    lebih banyak edge bisa memiliki total bobot yang lebih rendah dibandingkan dengan jalur yang memiliki lebih sedikit edge jika bobot pada 
#    edge tersebut lebih kecil. Oleh karena itu, dalam menentukan jalur terpendek, kita harus mempertimbangkan total bobot dari jalur tersebut,
#    bukan hanya jumlah edge.
