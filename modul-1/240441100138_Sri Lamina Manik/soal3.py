# Class 1: Kucing
class Kucing:
    def __init__(self, nama, umur, warna):
        self.nama = nama
        self.umur = umur
        self.warna = warna

    def meong(self):
        print(f"{self.nama} bilang: Meong~")

    def info(self):
        print(f"Kucing bernama {self.nama}, umur {self.umur} tahun, warna {self.warna}")

# Class 2: Burung
class Burung:
    def __init__(self, nama, jenis, bisa_terbang):
        self.nama = nama
        self.jenis = jenis
        self.bisa_terbang = bisa_terbang

    def berkicau(self):
        print(f"{self.nama} berkicau: Cuit cuit~")

    def info(self):
        status_terbang = "bisa terbang" if self.bisa_terbang else "tidak bisa terbang"
        print(f"Burung {self.nama} jenis {self.jenis}, {status_terbang}")

# Class 3: Ikan
class Ikan:
    def __init__(self, nama, habitat, panjang):
        self.nama = nama
        self.habitat = habitat
        self.panjang = panjang

    def berenang(self):
        print(f"{self.nama} sedang berenang di {self.habitat}")

    def info(self):
        print(f"Ikan {self.nama}, hidup di {self.habitat}, panjangnya {self.panjang} cm")


# Looping buat bikin beberapa objek
nama_kucing = ["Milo", "Luna", "Tom"]
nama_burung = ["Beo", "Kutilang", "Merpati"]
nama_ikan = ["Nemo", "Dory", "Buntal"]

print("=== Data Kucing ===")
for i in range(3):
    kucing = Kucing(nama_kucing[i], umur=2+i, warna="abu-abu")
    kucing.info()
    kucing.meong()

print("\n=== Data Burung ===")
for i in range(3):
    burung = Burung(nama_burung[i], jenis="tropis", bisa_terbang=(i % 2 == 0))
    burung.info()
    burung.berkicau()

print("\n=== Data Ikan ===")
for i in range(3):
    ikan = Ikan(nama_ikan[i], habitat="laut", panjang=10 + i*5)
    ikan.info()
    ikan.berenang()
