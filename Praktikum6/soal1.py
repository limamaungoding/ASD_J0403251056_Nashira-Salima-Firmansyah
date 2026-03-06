def quickSort(data):
    quickSortLen(data, 0, len(data)-1)

def quickSortLen(data, first, last):
    if first < last:
        splitpoint = partition(data, first, last)
        quickSortLen(data, first, splitpoint -1)
        quickSortLen(data, splitpoint +1, last)
                     
def partition(data, first, last):
    pivotvalue = data[first]
    leftmark = first + 1
    rightmark = last
    done = False

    while not done:
        while leftmark <= rightmark and data[leftmark] >= pivotvalue:
            leftmark = leftmark + 1

        while data[rightmark] <= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1
        
        if rightmark < leftmark:
            done = True
        
        else:
            temp = data [leftmark]
            data[leftmark] = data [rightmark]
            data[rightmark] = temp

    temp = data[first]
    data[first] = data[rightmark]
    data[rightmark] = temp

    return rightmark

data_skor = [43, 76, 12, 89, 33, 57, 98, 22, 68, 9]

quickSort(data_skor)

print("Hasil pengurutan (Descending):", data_skor)
print("1. Skor lima kandidat tertinggi:", data_skor[:5])
print("2. Kandidat yang lolos adalah yang memiliki skor:", data_skor[:5])
