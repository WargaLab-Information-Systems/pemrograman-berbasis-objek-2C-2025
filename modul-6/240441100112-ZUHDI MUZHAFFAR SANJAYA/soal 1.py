import math

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
        return math.pi * self.jari_jari * self.jari_jari

class Segitiga(BangunDatar):
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def luas(self):
        return 0.5 * self.alas * self.tinggi

def cetak_luas(bangun_datar):
    print(f"Luas {type(bangun_datar).__name__}: {bangun_datar.luas():.2f}")

def main ():
    while True:
        print("pilihlah salah satu: ")
        print("1. persegi")
        print("2. lingkaran")
        print("3. segitiga")

        pilihan = int(input("masukkan pilihan: "))

        if pilihan == 1:
            s = int(input("masukkan jumlah sisi: "))
            p = Persegi(s)
            cetak_luas(p)
        elif pilihan == 2:
            j = int(input("masukkan jumlah jari-jari: "))
            l = Lingkaran(j)
            cetak_luas(l)
        elif pilihan == 3:
            a = int(input("masukkan alas: "))
            t = int(input("masukkan tinggi: "))
            hasil = Segitiga(a,t)
            cetak_luas(hasil)
        else:
            print("angka tidak valid")
            exit()
        n = input("mau pilih lagi? (y/n): ")
        if n != "y":
            break
main()