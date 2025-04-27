class Anjing:
    def __init__(self, nama, ras, warna):
        self.nama = nama
        self.ras = ras
        self.warna = warna
    def info (self):
        print("Nama :", self.nama)
        print("Ras  :", self.ras)
        print("Warna:", self.warna)

class Burung:
    def __init__(self, nama, jenis, warna):
        self.nama = nama
        self.jenis = jenis
        self.warna = warna
    def info (self):
        print("Nama  :", self.nama)
        print("Jenis :", self.jenis)
        print("Warna :", self.warna)

class Ular:
    def __init__(self, nama, jenis, panjang):
        self.nama = nama
        self.jenis = jenis
        self.panjang = panjang
    def info (self):
        print("Nama   :", self.nama)
        print("Jenis  :", self.jenis)
        print("Panjang:", self.panjang)

hewan_list = []
anjing_nama = ["Zaki", "Ambaki", "Rizaki"]
burung_nama = ["Chichi", "Iggy", "Wiwi"]
ular_nama = ["Death Adder", "Taipan", "Black Mamba"]

for nama in anjing_nama:
    hewan_list.append(Anjing(nama, "Buldog", "Putih"))

for nama in burung_nama:
    hewan_list.append(Burung(nama, "Lovebird", "Hijau bercorak biru"))

for nama in ular_nama:
    hewan_list.append(Ular(nama, "Berbisa Tinggi", "2 meter"))

def tampilkan_info(hewan_list):
    for hewan in hewan_list:
        hewan.info()
        print("-------------------")
tampilkan_info(hewan_list)
