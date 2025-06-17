class BangunDatar:
    def __init__(self):
        self.nama = "Bangun Datar"

    def luas(self):
        return 0

class Persegi(BangunDatar):
    def __init__(self, sisi):
        self.nama = "Persegi"
        self.sisi = sisi

    def luas(self):
        return self.sisi ** 2

class Lingkaran(BangunDatar):
    def __init__(self, jari_jari):
        self.nama = "Lingkaran"
        self.jari_jari = jari_jari

    def luas(self):
        return 3.14 * self.jari_jari ** 2

class Segitiga(BangunDatar):
    def __init__(self, alas, tinggi):
        self.nama = "Segitiga"
        self.alas = alas
        self.tinggi = tinggi

    def luas(self):
        return 0.5 * self.alas * self.tinggi

def cetak_luas(bangun_datar):
    print(f"Luas {bangun_datar.nama}: {bangun_datar.luas()}")

while True:
    print("\nPilih bangun datar:")
    print("1. Persegi")
    print("2. Lingkaran")
    print("3. Segitiga")
    print("4. Keluar")

    pilihan = input("Masukkan pilihan (1-4): ")

    if pilihan == "1":
        sisi = float(input("Masukkan sisi persegi: "))
        bangun = Persegi(sisi)
    elif pilihan == "2":
        jari = float(input("Masukkan jari-jari lingkaran: "))
        bangun = Lingkaran(jari)
    elif pilihan == "3":
        alas = float(input("Masukkan alas segitiga: "))
        tinggi = float(input("Masukkan tinggi segitiga: "))
        bangun = Segitiga(alas, tinggi)
    elif pilihan == "4":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid.")
        continue

    cetak_luas(bangun)
