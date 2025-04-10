class Kucing:
    def __init__(self, nama, ras, umur):
        self.nama = nama
        self.ras = ras
        self.umur = umur

    def info(self):
        print("Nama:", self.nama)
        print("Ras :", self.ras)
        print("Umur:", self.umur)

class Sapi:
    def __init__(self, nama, jenis, usia):
        self.nama = nama
        self.jenis = jenis
        self.usia = usia

    def info(self):
        print("Nama :", self.nama)
        print("Jenis:", self.jenis)
        print("Usia :", self.usia)

class Ular:
    def __init__(self, nama, jenis, panjang):
        self.nama = nama
        self.jenis = jenis
        self.panjang = panjang

    def info(self):
        print("Nama :", self.nama)
        print("Jenis :", self.jenis)
        print("Panjang:", self.panjang)

hewan_list = []

for i in range(3):
    nama = input(f"Masukkan nama kucing ke-{i+1}: ")
    ras = input(f"Masukkan ras kucing ke-{i+1}: ")
    umur = int(input(f"Masukkan umur kucing ke-{i+1}: "))
    hewan_list.append(Kucing(nama, ras, umur))

for i in range(3):
    nama = input(f"Masukkan nama sapi ke-{i+1}: ")
    jenis = input(f"Masukkan jenis sapi ke-{i+1}: ")
    usia = int(input(f"Masukkan usia sapi ke-{i+1}: "))
    hewan_list.append(Sapi(nama, jenis, usia))

for i in range(3):
    nama = input(f"Masukkan nama ular ke-{i+1}: ")
    jenis = input(f"Masukkan jenis ular ke-{i+1}: ")
    panjang = input(f"Masukkan panjang ular ke-{i+1}: ")
    hewan_list.append(Ular(nama, jenis, panjang))

def tampilkan_info(hewan_list):
    for hewan in hewan_list:
        hewan.info()
        print("-")

tampilkan_info(hewan_list)