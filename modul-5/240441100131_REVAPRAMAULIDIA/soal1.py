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
        return pi * self.jari_jari * self.jari_jari

class Segitiga(BangunDatar):
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
    
    def luas(self):
        return 0.5 * self.alas * self.tinggi

def is_float_positif(string):
    if string.count('.') == 1:
        bagian1, bagian2 = string.split('.')
        return bagian1.isdigit() and bagian2.isdigit()
    return False

def input_angka(pesan):
    while True:
        nilai = input(pesan)
        if nilai.isdigit() or is_float_positif(nilai):
            return float(nilai)
        else:
            print("Input harus angka positif")

def luas_bangun(bangun):
    return bangun.luas()

print("Pilih Bangun Datar")
print("1. Persegi")
print("2. Lingkaran")
print("3. Segitiga")

pilihan = input("Masukkan pilihanmu (1/2/3): ")

if pilihan == "1":
    sisi = input_angka("Masukkan panjang sisi: ")
    persegi = Persegi(sisi)
    hasil = luas_bangun(persegi)
    print("Luas persegi =", hasil)

elif pilihan == "2":
    jari_jari = input_angka("Masukkan jari-jari lingkaran: ")
    lingkaran = Lingkaran(jari_jari)
    hasil = luas_bangun(lingkaran)
    print("Luas lingkaran =", hasil)

elif pilihan == "3":
    alas = input_angka("Masukkan alas segitiga: ")
    tinggi = input_angka("Masukkan tinggi segitiga: ")
    segitiga = Segitiga(alas, tinggi)
    hasil = luas_bangun(segitiga)
    print("Luas segitiga =", hasil)
else:
    print("Pilihan tidak valid")