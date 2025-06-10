class BangunDatar:
    def luas(self):
        return 0

class Persegi(BangunDatar):
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi * self.sisi

class Lingkaran(BangunDatar):
    def __init__(self, jari_jari, pi_input):
        self.jari_jari = jari_jari
        if pi_input == 1:
            self.pi = 22/7
        elif pi_input == 2:
            self.pi = 3.14
        else:
            print("\n-- Inputan tidak valid --")

    def luas(self):
        return self.pi * self.jari_jari ** 2

class Segitiga(BangunDatar):
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def luas(self):
        return 0.5 * self.alas * self.tinggi

def cetak_luas(bangun_datar):
    print(f"Hasil Luas: {bangun_datar.luas()}")

while True:
    print("\n=== Pilih bangun datar yang ===")
    print("===      ingin dihitung     ===")
    print("1. Persegi")
    print("2. Lingkaran")
    print("3. Segitiga")
    
    pilihan = int(input("Masukkan pilihan (1/2/3) : "))

    if pilihan == 1:
        print("\n--- PERSEGI ---")
        sisi = float(input("Masukkan panjang sisi persegi : "))
        bangun = Persegi(sisi)
        cetak_luas(bangun)
    elif pilihan == 2:
        print("\n--- LINGKARAN ---")
        jari_jari = float(input("Masukkan jari-jari lingkaran : "))
        print("PI Lingkaran:")
        print("1. 22/7")
        print("2. 3.14")
        pi_input = int(input("Masukkan PI lingkaran (1/2) : "))
        bangun = Lingkaran(jari_jari, pi_input)
        cetak_luas(bangun)
    elif pilihan == 3:
        print("\n--- SEGITIGA ---")
        alas = float(input("Masukkan alas segitiga : "))
        tinggi = float(input("Masukkan tinggi segitiga : "))
        bangun = Segitiga(alas, tinggi)
        cetak_luas(bangun)
    else:
        print("\n-- Pilihan tidak valid --")

    ulang = input("\nMau ngulang? (y/n): ")
    if ulang != 'y':
        print("Program selesai.")
        break