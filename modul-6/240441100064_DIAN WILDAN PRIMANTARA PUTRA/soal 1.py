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
        return 3.14 * self.jari_jari * self.jari_jari

class Segitiga(BangunDatar):
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def luas(self):
        return 0.5 * self.alas * self.tinggi

def cetak_luas(bangun):
    print("Luas:", bangun.luas())

print("Pilih bangun datar:")
print("1. Persegi")
print("2. Lingkaran")
print("3. Segitiga")
pilihan = input("Masukkan pilihan (1/2/3): ")

if pilihan == "1":
    sisi = int(input("Masukkan panjang sisi: "))
    bangun = Persegi(sisi)
elif pilihan == "2":
    jari = int(input("Masukkan jari-jari lingkaran: "))
    bangun = Lingkaran(jari)
elif pilihan == "3":
    alas = int(input("Masukkan alas segitiga: "))
    tinggi = int(input("Masukkan tinggi segitiga: "))
    bangun = Segitiga(alas, tinggi)
else:
    print("Pilihan tidak valid.")
    exit()

cetak_luas(bangun)