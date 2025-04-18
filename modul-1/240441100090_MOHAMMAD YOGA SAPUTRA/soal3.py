class Kucing:
    def __init__(self, nama, ras, umur):
        self.nama = nama
        self.ras = ras
        self.umur = umur

    def info(self):
        print("Nama  :", self.nama)
        print("Ras   :", self.ras)
        print("Umur  :", self.umur)
        print("Suara : Meong")

class Sapi:
    def __init__(self, nama, jenis, usia):
        self.nama = nama
        self.jenis = jenis
        self.usia = usia

    def info(self):
        print("Nama  :", self.nama)
        print("Jenis :", self.jenis)
        print("Usia  :", self.usia)
        print("Suara : Moo")

class Ular:
    def __init__(self, nama, jenis, panjang):
        self.nama = nama
        self.jenis = jenis
        self.panjang = panjang

    def info(self):
        print("Nama    :", self.nama)
        print("Jenis   :", self.jenis)
        print("Panjang :", self.panjang)
        print("Suara   : Ssssss")

hewan_list = []

kucing_nama = ["Acil", "Ucil", "Boni"]
sapi_nama = ["Bowo", "Nono", "Wowo"]
ular_nama = ["Hijau", "Weling", "Anaconda"]

for nama in kucing_nama:
    hewan_list.append(Kucing(nama, "Anggora", 2))

for nama in sapi_nama:
    hewan_list.append(Sapi(nama, "Sapi Perah", 5))

for nama in ular_nama:
    hewan_list.append(Ular(nama, "Ular Sawah", "2 meter"))

def tampilkan_info(daftar_hewan):
    for hewan in daftar_hewan:
        hewan.info()
        print("-" * 30)
        
tampilkan_info(hewan_list)
