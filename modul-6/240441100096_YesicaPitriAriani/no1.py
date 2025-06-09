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
        pi = 3.14
        return pi * self.jari_jari ** 2

class Segitiga(BangunDatar):
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def luas(self):
        return 0.5 * self.alas * self.tinggi

# Polymorhisem / duck typing
def cetak_luas(bangun):
    print(f"Luas {bangun.__class__.__name__}: {bangun.luas():.2f}")

daftar_bangun = []

while True:
    print("\nPilih jenis bangun datar:")
    print("1. Persegi◻")
    print("2. Lingkaran〇")
    print("3. Segitiga△")
    print("4. Selesai")
    pilihan = input("masukkan pilihan (1,2,3,4): ")

    if pilihan == "1":
        sisi = float(input("masukkan sisi persegi: "))
        daftar_bangun.append(Persegi(sisi))

    elif pilihan == "2":
        jari = float(input("masukkan jari-jari lingkaran: "))
        daftar_bangun.append(Lingkaran(jari))

    elif pilihan == "3":
        alas = float(input("masukkan alas segitiga: "))
        tinggi = float(input("masukkan tinggi segitiga: "))
        daftar_bangun.append(Segitiga(alas, tinggi))

    elif pilihan == "4":
        print("terimakasih")
        break
    else:
        print("pilihan kamu tidak valid. coba lagi.")

print("\nHasil Luas Bangun Datar: ")
for bangun in daftar_bangun:
    cetak_luas(bangun)
