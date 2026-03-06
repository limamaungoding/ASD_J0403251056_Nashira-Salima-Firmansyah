def binarySearch(data, item):
    first = 0
    last = len(data)-1
    found = False

    while first<=last and not found:
        midpoint = (first + last)//2
        if data[midpoint] == item:
            found = True
        else:
            if item < data[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return found

data = [1, 2, 32, 8, 17, 19, 42, 13, 0, 2]
print(binarySearch(data, 3))
print(binarySearch(data, 13))