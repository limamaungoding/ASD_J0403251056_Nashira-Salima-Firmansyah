class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def print_list(self):
        if not self.head:
            return "kosong"
        temp = self.head
        res = ""
        while temp:
            res += f"{temp.data} -> "
            temp = temp.next
        return res + "null"

    def merge(self, other_list):
        if not self.head:
            self.head = other_list.head
            return
        if not other_list.head:
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = other_list.head

# --- TESTING ---

# CONTOH TAMPILAN #1
print("-" * 30)
print("Contoh Tampilan #1 :")
ll1 = LinkedList()
ll2 = LinkedList()

data1 = [1, 3, 5, 7]
data2 = [2, 4, 6, 8]

print(f"Masukkan elemen untuk Linked List 1: {', '.join(map(str, data1))}")
for d in data1:
    ll1.insert_at_end(d)

print(f"Masukkan elemen untuk Linked List 2: {', '.join(map(str, data2))}")
for d in data2:
    ll2.insert_at_end(d)

print(f"Linked List 1: {ll1.print_list()}")
print(f"Linked List 2: {ll2.print_list()}")

ll1.merge(ll2)
print(f"Linked List setelah digabungkan: {ll1.print_list()}")

print("-" * 30)

# CONTOH TAMPILAN #2
print("Contoh Tampilan #2 :")
ll3 = LinkedList()
ll4 = LinkedList()

data3 = [5, 15, 25]

print(f"Masukkan elemen untuk Linked List 1: {', '.join(map(str, data3))}")
for d in data3:
    ll3.insert_at_end(d)

print(f"Masukkan elemen untuk Linked List 2: (Tidak ada elemen)")

print(f"Linked List 1: {ll3.print_list()}")
print(f"Linked List 2: {ll4.print_list()}")

ll3.merge(ll4)
print(f"Linked List setelah digabungkan: {ll3.print_list()}")