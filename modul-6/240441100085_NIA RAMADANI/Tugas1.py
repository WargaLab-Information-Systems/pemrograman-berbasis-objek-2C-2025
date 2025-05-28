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
        phi = 3.14  
        return phi * self.jari_jari * self.jari_jari

class Segitiga(BangunDatar):
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def luas(self):
        return 0.5 * self.alas * self.tinggi

def cetak_luas(bentuk):
    print(f"Luas {bentuk.__class__.__name__}: {bentuk.luas():.2f}")

while True:
    print("\nPilih bangun datar:")
    print("1. Persegi")
    print("2. Lingkaran")
    print("3. Segitiga")
    print("4. Keluar")

    pilih = input("Masukkan pilihan (1-4): ")

    if pilih == '1':
        try:
            sisi = float(input("Masukkan panjang sisi: "))
            bentuk = Persegi(sisi)
            cetak_luas(bentuk)
        except ValueError:
            print("Input harus berupa angka.")
    elif pilih == '2':
        try:
            r = float(input("Masukkan jari-jari lingkaran: "))
            bentuk = Lingkaran(r)
            cetak_luas(bentuk)
        except ValueError:
            print("Input harus berupa angka.")
    elif pilih == '3':
        try:
            alas = float(input("Masukkan alas: "))
            tinggi = float(input("Masukkan tinggi: "))
            bentuk = Segitiga(alas, tinggi)
            cetak_luas(bentuk)
        except ValueError:
            print("Input harus berupa angka.")
    elif pilih == '4':
        print("Terima kasih. Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")