#=====================================================================
# Nama    : Nashira Salima Firmansyah
# NIM     : J0403251056
# Kelas   : TPL A2
#=====================================================================

#=====================================================================
#Implementasi dasar: Node pada linked list
#=====================================================================

class Node:
    #konstruktor yang dijalanakan secara otomatis ketika class Node dipanggil / diinstantiasi
    def __init__(self,data):
        self.data = data #menyimpan nilai atau data pada list
        self.next = None #pointer ini menunjuk ke note berikutnya (awal = none)

# 1) Membuat node dengan instantiasi class node
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

# 2) Mendefinisikan head dan menghubungkan Node : A -> B -> C -> None
head = nodeA
nodeA.next = nodeB
nodeB.next = nodeC

# 4) Traversal : menelusuri node dari head sampai ke none
current = head
while current is not None:
    print(current.data) #menampilkan data pada node saat ini
    current = current.next #pindah ke node berikutnya
    
#=====================================================================
#Implementasi dasar: Stack
#=====================================================================