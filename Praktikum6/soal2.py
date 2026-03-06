def binarySearchTugas(data, item):
    data.sort() 
    
    first = 0
    last = len(data) - 1
    found = False
    index_ditemukan = -1 

    while first <= last and not found:
        midpoint = (first + last) // 2
        if data[midpoint] == item:
            found = True
            index_ditemukan = midpoint
        else:
            if item < data[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    
  
    sama_dengan_x = [data[index_ditemukan]] if found else []

    lebih_besar_x = data[first:] if not found else data[index_ditemukan + 1:]
    
    return sama_dengan_x, lebih_besar_x, data

data_nilai = [43, 76, 12, 89, 33, 57, 98, 22, 68, 9]
X = 50

hasil_sama, hasil_lebih, data_sorted = binarySearchTugas(data_nilai, X)

print(f"Data setelah diurutkan: {data_sorted}")
print(f"1. Nilai yang sama dengan {X}: {hasil_sama}")
print(f"2. Nilai yang lebih besar dari {X}: {hasil_lebih}")