class Kucing:
    def __init__(self, nama, warna, umur):
        self.nama = nama
        self.warna = warna
        self.umur = umur

    def meong(self):
        print(f"{self.nama} berkata: Meooong!")

    def info(self):
        print(f"Kucing bernama {self.nama}, warna {self.warna}, umur {self.umur} tahun.")

class Anjing:
    def __init__(self, nama, ras, umur):
        self.nama = nama
        self.ras = ras
        self.umur = umur

    def gonggong(self):
        print(f"{self.nama} menggonggong: Guk guk!")

    def info(self):
        print(f"Anjing bernama {self.nama}, ras {self.ras}, umur {self.umur} tahun.")

class Burung:
    def __init__(self, nama, jenis, bisa_terbang):
        self.nama = nama
        self.jenis = jenis  
        self.bisa_terbang = bisa_terbang

    def berkicau(self):
        print(f"{self.nama} berkicau: Cuit cuit!")

    def info(self):
        status = "bisa terbang" if self.bisa_terbang else "tidak bisa terbang"
        print(f"Burung bernama {self.nama}, jenis {self.jenis}, dan {status}.")

daftar_kucing = []
daftar_anjing = []
daftar_burung = []

nama_kucing = ["ciko", "Luna", "sico"]
warna_kucing = ["putih", "abu-abu", "hitam"]

for i in range(3):
    kucing = Kucing(nama_kucing[i], warna_kucing[i], i + 1)
    daftar_kucing.append(kucing)

nama_anjing = ["Rex", "Buddy", "Charlie"]
ras_anjing = ["Bulldog", "Golden Retriever", "Pomeranian"]

for i in range(3):
    anjing = Anjing(nama_anjing[i], ras_anjing[i], i + 2)
    daftar_anjing.append(anjing)

nama_burung = ["Tweety", "Rio", "Koko"]
jenis_burung = ["Kenari", "Macaw", "Beo"]
bisa_terbang_list = [True, True, False]

for i in range(3):
    burung = Burung(nama_burung[i], jenis_burung[i], bisa_terbang_list[i])
    daftar_burung.append(burung)

print("== Kucing ==")
for kucing in daftar_kucing:
    kucing.info()
    kucing.meong()

print("\n== Anjing ==")
for anjing in daftar_anjing:
    anjing.info()
    anjing.gonggong()

print("\n== Burung ==")
for burung in daftar_burung:
    burung.info()
    burung.berkicau()
