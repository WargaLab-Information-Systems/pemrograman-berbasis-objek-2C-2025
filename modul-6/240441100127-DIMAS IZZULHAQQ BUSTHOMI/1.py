import math

class BangunDatar:
    def Luas(self):
        return 0

class Persegi(BangunDatar):
    def __init__(self, sisi):
        self.sisi = sisi

    def Luas(self):
        return self.sisi * self.sisi
        
class Lingkaran(BangunDatar):
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari
    
    def Luas(self):
        return math.pi * self.jari_jari * self.jari_jari
    
class Segitiga(BangunDatar):
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def Luas(self):
        return 0.5 * self.alas * self.tinggi
    
def results(bangunDatar):
    return bangunDatar.Luas()

while True:
    print("===== PENJUMLAHAN LUAS BANGUN DATAR =====")
    print("1. Persegi")
    print("2. Lingkaran")
    print("3. Segitiga")

    choose = int(input("Pilih menu : "))

    if choose == 1:
        print("=== LUAS PERSEGI ===")
        print("====" * 5)
        print("RUMUS PERSEGI SISI x SISI")
        print("====" * 5)
        while True:
            sisi = input("Masukkan SISI : ")
            if sisi.isdigit():
                sisi = int(sisi)
                p = Persegi(sisi)
                print(f"Luas Persegi : {results(p)}")
                break
            else:
                print("Inputan harus angka!")
        
    elif choose == 2:
        print("=== LUAS LINGKARAN ===")
        print("====" * 5)
        print("RUMUS LINGKARAN PHI x r x r")
        print("====" * 5)
        while True:
            r = input("Masukkan JARI - JARI : ")
            if r.isdigit():
                r = int(r)
                l = Lingkaran(r)
                print(f"Luas Lingkaran : {results(l)}")
                break
            else:
                print("Inputan harus angka!")

    elif choose == 3:
        print("=== LUAS SEGITIGA ===")
        print("====" * 5)
        print("RUMUS SEGITIGA 1/2 x ALAS x TINGGI")
        print("====" * 5)
        while True:
            alas = input("Masukkan ALAS   : ")
            tinggi = input("Masukkan TINGGI : ")
            if alas.isdigit() and tinggi.isdigit():
                alas = int(alas)
                tinggi = int(tinggi)
                s = Segitiga(alas, tinggi)
                print(f"Luas Segitiga   : {results(s)}")
                break
            else:
                print("Inputan harus angka!")

    else:
        print("Pilih sesuai menu!")
