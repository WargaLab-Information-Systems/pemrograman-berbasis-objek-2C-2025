class BangunDatar:
    def luas(self):
        return 0

class Persegi(BangunDatar):
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi * self.sisi

class Lingkaran(BangunDatar):
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def luas(self):
        pi = 3.14159
        return pi * self.jari_jari ** 2

class Segitiga(BangunDatar):
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def luas(self):
        return 0.5 * self.alas * self.tinggi

def cetak_luas(bangun):
    print(f"Luas {bangun.__class__.__name__}: {bangun.luas():.2f}")

while True:
    print("\n=== Hitung Luas Bangun Datar ===")
    print("1. Persegi\n2. Lingkaran\n3. Segitiga")
    pilihan = input("Pilih bangun datar (1/2/3): ")

    if pilihan == "1":
        sisi = float(input("Masukkan sisi persegi: "))
        b = Persegi(sisi)
    elif pilihan == "2":
        jari = float(input("Masukkan jari-jari lingkaran: "))
        b = Lingkaran(jari)
    elif pilihan == "3":
        alas = float(input("Masukkan alas segitiga: "))
        tinggi = float(input("Masukkan tinggi segitiga: "))
        b = Segitiga(alas, tinggi)
    else:
        print("Pilihan tidak valid!")
        continue

    cetak_luas(b)

    lagi = input("Ingin menghitung lagi? (y/n): ").lower()
    if lagi != "y":
        break
