# Diberikan suatu list berikut:
# data = [1, 3, 5, 7, 9, 0, 2, 4, 6, 8]
# Apakah keluaran dari:
# ● data.index(3, 0, 3)
# ● data.index(3, 5, 6)
# ● data.index(3, 3, 0)
# ● data.index(3, 0, 11)

data = [1, 3, 5, 7, 9, 0, 2, 4, 6, 8]

try:
    print(f"Hasil data.index(3, 0, 3): {data.index(3, 0, 3)}")
except ValueError as e:
    print(f"Hasil data.index(3, 0, 3): {e}")

try:
    print(f"Hasil data.index(3, 5, 6): {data.index(3, 5, 6)}")
except ValueError as e:
    print(f"Hasil data.index(3, 5, 6): ValueError - {e}")

try:
    print(f"Hasil data.index(3, 3, 0): {data.index(3, 3, 0)}")
except ValueError as e:
    print(f"Hasil data.index(3, 3, 0): ValueError - {e}")

try:
    print(f"Hasil data.index(3, 0, 11): {data.index(3, 0, 11)}")
except ValueError as e:
    print(f"Hasil data.index(3, 0, 11): {e}")