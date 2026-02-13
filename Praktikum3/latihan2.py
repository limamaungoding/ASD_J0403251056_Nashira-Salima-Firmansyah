class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new_node
        new_node.next = self.head

    def search(self, key):
        if not self.head:
            print("Circular Linked List kosong. Tidak ada elemen yang bisa dicari.")
            return
        temp = self.head
        while True:
            if temp.data == key:
                print(f"Elemen {key} ditemukan dalam Circular Linked List.")
                return
            temp = temp.next
            if temp == self.head:
                break
        print(f"Elemen {key} tidak ditemukan dalam Circular Linked List.")

# --- TESTING ---
cll = CircularLinkedList()

# tAMPILAN 1
elemen = [3, 7, 12, 19, 25]

print(f"Masukkan elemen ke dalam Circular Linked List: {', '.join(map(str, elemen))}")
for e in elemen:
    cll.insert_at_end(e)

cari = 12
print(f"Masukkan elemen yang ingin dicari: {cari}")
cll.search(cari)

print("-" * 30)
# TAMPILAN 2

print("Contoh Tampilan #2 :")
data2 = [5, 10, 15, 20, 30]
print(f"Masukkan elemen ke dalam Circular Linked List: {', '.join(map(str, data2))}")
for d in data2:
    cll.insert_at_end(d)

cari2 = 25
print(f"Masukkan elemen yang ingin dicari: {cari2}")
cll.search(cari2)

print("-" * 30)

# TAMPILAN 3
print("Contoh Tampilan #3 :")
print("Masukkan elemen ke dalam Circular Linked List: (Tidak ada elemen)")

cari3 = 10
print(f"Masukkan elemen yang ingin dicari: {cari3}")
cll.search(cari3)


