class Node:
    def __init__(self, id_buku, judul):
        self.id = id_buku
        self.judul = judul
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    #insert data ke BST
    def insert(self, id_buku, judul):
        new = Node(id_buku, judul)

        if self.root is None:
            self.root = new
            print("insert:", id_buku, "-", judul)
            return

        N = None
        C = self.root

        #cari posisi yang cocok
        while C is not None:
            N = C
            if id_buku < C.id:
                C = C.left
            elif id_buku > C.id:
                C = C.right
            else:
                print("[INSERT] ID sudah ada!")
                return

        #masukin node ke kiri / kanan
        if id_buku < N.id:
            N.left = new
        else:
            N.right = new

        print(f"[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}")

    #cari data berdasarkan ID
    def search(self, id_buku):
        C = self.root
        while C is not None:
            if id_buku == C.id:
                return C
            elif id_buku < C.id:
                C = C.left
            else:
                C = C.right
        return None

    #traversal inorder (kiri - root - kanan)
    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(f"{node.id} - {node.judul}")
            self.inorder(node.right)

    #ambil ID terkecil
    def get_min(self):
        if self.root is None:
            return None
        C = self.root
        while C.left is not None:
            C = C.left
        return C

    #ambil ID terbesar
    def get_max(self):
        if self.root is None:
            return None
        C = self.root
        while C.right is not None:
            C = C.right
        return C

    #hitung tinggi tree
    def height(self, node):
        if node is None:
            return -1
        left_h = self.height(node.left)
        right_h = self.height(node.right)
        return max(left_h, right_h) + 1


print("SISTEM KATALOG PERPUSTAKAAN \"ILMU TERANG\"")
print("=========================================")

bst = BST()

#data awal
bst.insert(50, "Hujan")
bst.insert(30, "Pulang")
bst.insert(70, "Laut Bercerita")
bst.insert(20, "Serial Anak Mamak")
bst.insert(40, "Ayahku Bukan Pembohong")
bst.insert(60, "Filosofi Teras")
bst.insert(80, "Pergi")

#tampilkan isi BST
print("\n[INFO] Koleksi Buku (In-Order Traversal):")
bst.inorder(bst.root)

#search
print("\n[SEARCH] Mencari ID 60...", end=" ")
hasil = bst.search(60)
if hasil:
    print(f"Ketemu! Judul: {hasil.judul}")
else:
    print("Data ga ditemukan:(.")

print("[SEARCH] Mencari ID 100...", end=" ")
hasil = bst.search(100)
if hasil:
    print(f"Ketemu! Judul: {hasil.judul}")
else:
    print("Data ga ditemukan:(.")

#statistik
min_node = bst.get_min()
max_node = bst.get_max()

if min_node:
    print(f"\n[STATISTIK] ID Terkecil: {min_node.id}")
if max_node:
    print(f"[STATISTIK] ID Terbesar: {max_node.id}")

print(f"[INFO] Tinggi (Height) Tree: {bst.height(bst.root)}")

print("=========================================")
print("Simulasi Sudah Selesai!")