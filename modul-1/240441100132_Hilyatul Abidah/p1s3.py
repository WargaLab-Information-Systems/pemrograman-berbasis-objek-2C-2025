class Kucing:
    def __init__(self, nama, umur, warna, aktivitas):
        self.nama = nama
        self.umur = umur
        self.warna = warna
        self.aktivitas_kucing = aktivitas

    def suara(self):
        print(f"{self.nama} si kucing bersuara: Meong!")

    def deskripsi(self):
        print(f"{self.nama} berumur {self.umur} tahun dan berwarna {self.warna}.")

    def aktivitas(self):
        print(f"{self.nama} suka {self.aktivitas_kucing}.")


class Burung:
    def __init__(self, nama, jenis, warna, aktivitas):
        self.nama = nama
        self.jenis = jenis
        self.warna = warna
        self.aktivitas_burung = aktivitas

    def suara(self):
        print(f"{self.nama} si burung berkicau: Cuit cuit!")

    def deskripsi(self):
        print(f"{self.nama} adalah burung jenis {self.jenis} dengan warna {self.warna}.")

    def aktivitas(self):
        print(f"{self.nama} suka {self.aktivitas_burung}.")


class Ikan:
    def __init__(self, nama, ukuran, habitat, aktivitas):
        self.nama = nama
        self.ukuran = ukuran
        self.habitat = habitat
        self.aktivitas_ikan = aktivitas

    def suara(self):
        print(f"{self.nama} si ikan tidak bersuara, tapi lincah di air!")

    def deskripsi(self):
        print(f"{self.nama} berukuran {self.ukuran} dan hidup di {self.habitat}.")

    def aktivitas(self):
        print(f"{self.nama} suka {self.aktivitas_ikan}.")

kucing_list = []
burung_list = []
ikan_list = []

jumlah = int(input("Masukkan jumlah data hewan untuk tiap jenis: "))

print("--- Input Data Kucing ---")
for i in range(jumlah):
    print(f"Data Kucing ke-{i+1}")
    nama = input("Nama: ")
    umur = input("Umur: ")
    warna = input("Warna: ")
    aktivitas = input("Aktivitas: ")
    kucing = Kucing(nama, umur, warna, aktivitas)
    kucing_list.append(kucing)

print("--- Input Data Burung ---")
for i in range(jumlah):
    print(f"Data Burung ke-{i+1}")
    nama = input("Nama: ")
    jenis = input("Jenis: ")
    warna = input("Warna: ")
    aktivitas = input("Aktivitas: ")
    burung = Burung(nama, jenis, warna, aktivitas)
    burung_list.append(burung)

print("--- Input Data Ikan ---")
for i in range(jumlah):
    print(f"Data Ikan ke-{i+1}")
    nama = input("Nama: ")
    ukuran = input("Ukuran: ")
    habitat = input("Habitat: ")
    aktivitas = input("Aktivitas: ")
    ikan = Ikan(nama, ukuran, habitat, aktivitas)
    ikan_list.append(ikan)

print("___ DAFTAR KUCING ___")
for k in kucing_list:
    k.suara()
    k.deskripsi()
    k.aktivitas()

print("--- DAFTAR BURUNG ---")
for b in burung_list:
    b.suara()
    b.deskripsi()
    b.aktivitas()

print("... DAFTAR IKAN ...")
for i in ikan_list:
    i.suara()
    i.deskripsi()
    i.aktivitas()
