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

def cetak_luas(bangun):
    print(f"Luas {bangun.__class__.__name__} = {bangun.luas():.2f}")

def validasi_angka():
    while True:
        nilai = input("Masukkan disini: ").strip()
        if nilai.replace('.', '', 1).isdigit():
            val_float = float(nilai)
            if val_float > 0:
                return val_float
        print("Input harus angka positif, coba lagi.")

def main():
    while True:
        print("\n=== Hitung Luas Bangun Datar ===")
        print("1. Persegi")
        print("2. Lingkaran")
        print("3. Segitiga")
        print("4. Keluar")
        pilihan = int(input("Pilih bangun datar (1/2/3/4): "))

        if pilihan == 1:
            print("Berapa panjang sisinya:")
            sisi = validasi_angka()
            bangun = Persegi(sisi)
            cetak_luas(bangun)
        elif pilihan == 2:
            print("Berapa jari-jari lingkarannya:")
            jari = validasi_angka()
            bangun = Lingkaran(jari)
            cetak_luas(bangun)
        elif pilihan == 3:
            print("Berapa alas segitiganya:")
            alas = validasi_angka()
            print("Berapa tinggi segitiganya:")
            tinggi = validasi_angka()
            bangun = Segitiga(alas, tinggi)
            cetak_luas(bangun)
        elif pilihan == 4:
            print("Terima kasih, program selesai.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

main()