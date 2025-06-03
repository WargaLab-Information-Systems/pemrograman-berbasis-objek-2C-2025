class Kucing:
    def __init__(self, nama, warna, umur):
        self.nama = nama
        self.warna = warna
        self.umur = umur

    def mengeong(self):
        print(f"Kucing {self.nama} mengeong meminta makan")

    def tidur(self):
        print(f"Kucing {self.nama} tidur di sofa")

    def tampilkan(self):
        print(f"Nama kucing: {self.nama}, warna: {self.warna}, umur: {self.umur} tahun")
        self.mengeong()
        self.tidur()

class Rakun:
    def __init__(self, nama, kebiasaan, habitat):
        self.nama = nama
        self.kebiasaan = kebiasaan
        self.habitat = habitat

    def mencuri_makanan(self):
        print(f"Rakun {self.nama} mencari makanan dari tempat sampah")

    def bersembunyi(self):
        print(f"Rakun {self.nama} bersembunyi di {self.habitat}")

    def tampilkan(self):
        print(f"Nama rakun: {self.nama}, kebiasaan: {self.kebiasaan}, habitat: {self.habitat}")
        self.mencuri_makanan()
        self.bersembunyi()

class Rubah:
    def __init__(self, nama, warna_bulu, kecepatan):
        self.nama = nama
        self.warna_bulu = warna_bulu
        self.kecepatan = kecepatan

    def berburu(self):
        print(f"Rubah {self.nama} berburu di hutan dengan kecepatan {self.kecepatan} km/jam")

    def melolong(self):
        print(f"Rubah {self.nama} melolong di malam hari")

    def tampilkan(self):
        print(f"Nama rubah: {self.nama}, warna bulu: {self.warna_bulu}, kecepatan: {self.kecepatan} km/jam")
        self.berburu()
        self.melolong()

data_hewan = []

while True:
    jumlah = input("Masukkan jumlah data yang ingin diinput per jenis hewan: ")

    if jumlah.isdigit():
        jumlah = int(jumlah)

        for i in range(jumlah):
            print(f"\nInput data kucing ke {i+1}")
            nama = input("Nama kucing: ")
            warna = input("Warna kucing: ")
            umur = input("Umur kucing: ")
            data_hewan.append(Kucing(nama, warna, umur))

        for i in range(jumlah):
            print(f"\nInput data rakun ke {i+1}")
            nama = input("Nama rakun: ")
            kebiasaan = input("Kebiasaan rakun: ")
            habitat = input("Habitat rakun: ")
            data_hewan.append(Rakun(nama, kebiasaan, habitat))

        for i in range(jumlah):
            print(f"\nInput data rubah ke {i+1}")
            nama = input("Nama rubah: ")
            warna_bulu = input("Warna bulu rubah: ")
            kecepatan = input("Kecepatan rubah: ")
            data_hewan.append(Rubah(nama, warna_bulu, kecepatan))

        print("\nData Hewan")
        for hewan in data_hewan:
            print()
            hewan.tampilkan()
        break

    else:
        print("Input harus berupa angka")