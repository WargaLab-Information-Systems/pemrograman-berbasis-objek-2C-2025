class kucing:
    def __init__(self, nama, jenis, warna):
        self.nama = nama
        self.jenis = jenis
        self.warna = warna

    def suara(self):
        print(f"{self.nama} bersuara: Meong")

    def info(self):
        print(f"Kucing - Nama : {self.nama}, Jenis : {self.jenis}, Warna : {self.warna}")

class anjing:
    def __init__(self, nama, jenis, warna):
        self.nama = nama
        self.jenis = jenis
        self.warna = warna

    def suara(self):
        print(f"{self.nama} bersuara: Guk-guk-guk")

    def info(self):
        print(f"Anjing - Nama: {self.nama}, Jenis: {self.jenis}, Warna: {self.warna} ")

class ular:
    def __init__(self, nama, jenis, warna):
        self.nama = nama
        self.jenis = jenis
        self.warna = warna

    def suara(self):
        print(f"{self.nama} mendesis: stttsst")

    def info(self):
        print(f"Ular - Nama: {self.nama}, Jenis: {self.jenis}, Warna : {self.warna}")

daftar_kucing = []
daftar_anjing = []
daftar_ular = []

jumlah = 3

print("~Input Data Kucing~")
for i in range(jumlah):
    nama = input(f"Nama Kucing ke-{i+1}: ")
    jenis = input("Jenis: ")
    warna = input("Warna: ")
    daftar_kucing.append(kucing(nama, warna, jenis))


print("\n~Input Data Anjing~")
for i in range(jumlah):
    nama = input(f"Nama Anjing ke-{i+1}: ")
    jenis = input("Jenis: ")
    umur = input("Warna: ")
    daftar_anjing.append(anjing(nama, jenis, umur))


print("\n~Input Data Ular~")
for i in range(jumlah):
    nama = input(f"Nama Ular ke-{i+1}: ")
    jenis = input("Jenis: ")
    warna = input("Warna: ")
    daftar_ular.append(ular(nama, jenis, warna))


print("\n~Data Hewan~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`")
for kucing in daftar_kucing:
    kucing.info()
    kucing.suara()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`")
for anjing in daftar_anjing:
    anjing.info()
    anjing.suara()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`")
for ular in daftar_ular:
    ular.info()
    ular.suara()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`")