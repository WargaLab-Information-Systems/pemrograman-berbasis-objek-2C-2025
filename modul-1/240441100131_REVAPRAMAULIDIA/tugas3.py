class Kucing:
    def __init__(self, nama, ras, jumlah_kaki):
        self.nama = nama
        self.ras = ras
        self.jumlah_kaki = jumlah_kaki

    def jenis_makanan(self):
        return f"{self.nama} termasuk hewan pemakan Daging"

    def bergerak(self):
        return f"{self.nama} bergerak cepat menggunakan {self.jumlah_kaki} kaki"

class Kuda:
    def __init__(self, nama, warna, jumlah_kaki):
        self.nama = nama
        self.warna = warna
        self.jumlah_kaki = jumlah_kaki

    def jenis_makanan(self):
        return f"{self.nama} termasuk hewan pemakan Tumbuhan"

    def bergerak(self):
        return f"{self.nama} berlari cepat menggunakan {self.jumlah_kaki} kaki"

class Buaya:
    def __init__(self, nama, habitat, panjang_tubuh):
        self.nama = nama
        self.habitat = habitat
        self.panjang_tubuh = panjang_tubuh

    def jenis_makanan(self):
        return f"{self.nama} termasuk hewan pemakan Daging"

    def bergerak(self):
        return f"{self.nama} merayap dengan panjang tubuh {self.panjang_tubuh} meter"

list_kucing = []
list_kuda = []
list_buaya = []

jumlah = int(input("Jumlah hewan yang akan diinput: "))

while True:
    print("\n Menu ")
    print("1. Tambah Data Kucing")
    print("2. Tambah Data Kuda")
    print("3. Tambah Data Buaya")
    print("4. Keluar")

    pilihan = input("Pilih menu (1/2/3/4): ")

    if pilihan == "1":
        print("\nInput Data Kucing")
        for i in range(jumlah):
            print(f"Data Kucing ke-{i+1}")
            nama = input("Nama: ")
            ras = input("Ras: ")
            jumlah_kaki = int(input("Jumlah kaki: "))
            list_kucing.append(Kucing(nama, ras, jumlah_kaki))
        print(f"{jumlah} data kucing berhasil ditambahkan")

    elif pilihan == "2":
        print("\nInput Data Kuda")
        for i in range(jumlah):
            print(f"Data Kuda ke-{i+1}")
            nama = input("Nama: ")
            warna = input("Warna: ")
            jumlah_kaki = int(input("Jumlah kaki: "))
            list_kuda.append(Kuda(nama, warna, jumlah_kaki))
        print(f"{jumlah} data kuda berhasil ditambahkan")

    elif pilihan == "3":
        print("\nInput Data Buaya")
        for i in range(jumlah):
            print(f"Data Buaya ke-{i+1}")
            nama = input("Nama: ")
            habitat = input("Habitat: ")
            panjang_tubuh = float(input("Panjang tubuh (meter): "))
            list_buaya.append(Buaya(nama, habitat, panjang_tubuh))
        print(f"{jumlah} data buaya berhasil ditambahkan")

    elif pilihan == "4":
        print("Program selesai")
        break
    else:
        print("Pilihan tidak valid")