def sequentialSearch (data, value):
    pos = 0
    found = False

    while pos <len (data) and not found:
        if data[pos] == value:
            found = True
        else:
            pos = pos + 1
    if found:
        return pos
    else:
        return -1

data = [1, 2, 32, 8, 17, 19, 42, 13, 0, 2]
print (sequentialSearch (data, 3))
print (sequentialSearch (data, 13))

def sequentialSearchReturn(data, value):
    pos = 0
    indices = []
    
    while pos < len(data):
        if data[pos] == value:
            indices.append(pos)
        pos = pos + 1
            
    return indices
data = [1, 2, 32, 8, 17, 19, 42, 13, 0, 2]
print(sequentialSearchReturn(data, 2))  # Output: [1, 9]
print(sequentialSearchReturn(data, 100)) # Output: []

# Latihan:
# Modifikasi Program 4 di atas hingga program tersebut:
# 1. Mengembalikan posisi (indeks) pertama dari nilai yang dicari pada list.
# Apabila nilai tidak ditemukan, kembalikan -1.
# 2. Mengembalikan seluruh posisi dari nilai yang dicari pada list (Contoh: pada
# saat mencari 2, nilai yang dikembalikan adalah [1, 9].
