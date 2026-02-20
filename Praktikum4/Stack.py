#=====================================================================
# Nama    : Nashira Salima Firmansyah
# NIM     : J0403251056
# Kelas   : TPL A2
#=====================================================================

#=====================================================================
#Implementasi dasar: Stack
#=====================================================================

class Node:
    #konstruktor yang dijalanakan secara otomatis ketika class Node dipanggil / diinstantiasi
    def __init__(self,data):
        self.data = data #menyimpan nilai atau data pada list
        self.next = None #pointer ini menunjuk ke note berikutnya (awal = none)

# Stack ada operasi push(memasukkan head baru) and pop (menghapus head)
class stack:
    def __init__(self):
            self.top = None #top merujuk ke node paling atas (yg awalnya kosong)
    
    def push(self,data): #memasukkan data baru pada stack
        # 1) membuat node baru
        nodeBaru = Node(data)
        # 2) node baru merujuk ke top yg lama / head yg lama
        nodeBaru.next = self.top
        # 3) geser top pindah ke node baru
        self.top = nodeBaru

    def is_empty_(self):
        return self.top is None

    def pop(self): #mengambil/ menghapus node paling atas (top/head)
        if self.is_empty_():
            print("Stack kosong, tidak bisa pop")
            return None
        data_terhapus = self.top.data #soroti bagian top dan simpan di variabel
        self.top = self.top.next #geser top ke node berikutnya
        return data_terhapus
    
    def peek(self):
        # melihat data yang paling atas tanpa menghapus
        if self.is_empty_:
            return None
        return self.top.data

    def tampilkan(self):
        # Top -> A -> B
        current = self.top
        print("Top ->" , end=" " )
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("None")
        
# Instansi class stack
s = stack()
s.push("A")
s.push("B")
s.push("C")
s.tampilkan()
print("Peek (Lihat Top):", s.peek())
s.pop()
