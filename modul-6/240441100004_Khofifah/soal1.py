import math

class BangunDatar:
    def luas(self):
        pass

class Persegi(BangunDatar):
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi * self.sisi

class Lingkaran(BangunDatar):
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def luas(self):
        return math.pi * self.jari_jari ** 2

class Segitiga(BangunDatar):
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def luas(self):
        return 0.5 * self.alas * self.tinggi

def cetak_luas(bangun):
    print(f"Luas {bangun.__class__.__name__}: {bangun.luas():.2f}")

def main():
    while True:
        print("\nPilih bangun datar:")
        print("1. Persegi")
        print("2. Lingkaran")
        print("3. Segitiga")
        print("4. Keluar")

        pilihan = input("Masukkan pilihan (1-4): ")

        if pilihan == "1":
            sisi = float(input("Masukkan panjang sisi: "))
            bangun = Persegi(sisi)

        elif pilihan == "2":
            jari_jari = float(input("Masukkan jari-jari lingkaran: "))
            bangun = Lingkaran(jari_jari)

        elif pilihan == "3":
            alas = float(input("Masukkan alas segitiga: "))
            tinggi = float(input("Masukkan tinggi segitiga: "))
            bangun = Segitiga(alas, tinggi)

        elif pilihan == "4":
            print("Terima kasih!")
            break

        else:
            print("Pilihan tidak valid!")
            continue

        cetak_luas(bangun)

if __name__ == "__main__":
    main()
