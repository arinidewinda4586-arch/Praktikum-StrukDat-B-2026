"""
dibuat ulang karena folder sebelumnya hilang
"""

class Jajan:
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok

    def tampilkan_info(self):
        print(f"Nama  : {self.nama}")
        print(f"Harga : {self.harga}")
        print(f"Stok  : {self.stok}")
        print("-" * 20)

    def beli(self, jumlah):
        if jumlah <= self.stok:
            self.stok -= jumlah
            print(f"{jumlah} {self.nama} berhasil dibeli.")
        else:
            print("Stok tidak cukup.")

jajan1 = Jajan("Risol Mayo", 5000, 20)
jajan2 = Jajan("Mie Ayam", 12000, 15)
jajan3 = Jajan("Matcha", 10000, 10)

jajan1.tampilkan_info()
jajan2.tampilkan_info()
jajan3.tampilkan_info()

#ubah salah satu atrbut
jajan3.harga = 12000

print("Setelah harga matcha diubah:")
jajan3.tampilkan_info()