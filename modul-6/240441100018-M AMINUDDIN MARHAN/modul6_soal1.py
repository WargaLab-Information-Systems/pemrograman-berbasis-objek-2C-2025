class BangunDatar:
    def luas(self):
        pass

class Persegi(BangunDatar):
    def __init__(self):
        while True:
            try:
                self.sisi = float(input("Masukkan panjang sisi persegi: "))
                if self.sisi <= 0:
                    print("Panjang sisi persegi harus lebih besar dari 0")
                    continue
                break
            except ValueError:
                print("Panjang sisi harus berupa angka")

    def luas(self):
        return f"Luas persegi adalah {self.sisi ** 2}"

class Lingkaran(BangunDatar):
    def __init__(self):
        while  True:
            try:
                self.jari_jari = float(input("Masukkan panjang jari-jari lingkaran: "))
                if self.jari_jari <= 0:
                    print("Panjang jari-jari harus lebih besar dari 0")
                    continue
                break
            except ValueError:
                print("Panjang jari-jari harus berupa angka")

    def luas(self):
        return f"Luas lingkaran adalah {22/7 * self.jari_jari ** 2}"

class Segitiga(BangunDatar):
    def __init__(self):
        while True:
            try:
                self.alas = float(input("Masukkan panjang alas segitiga: "))
                self.tinggi = float(input("Masukkan panjang tinggi segitiga: "))
                if self.alas <= 0 or self.tinggi <= 0:
                    print("Panjang alas dan tinggi harus lebih besar dari 0")
                    continue
                break
            except ValueError:
                print("Panjang alas dan tinggi harus berupa angka")

    def luas(self):
        return f"Luas segitiga adalah {1/2 * self.alas * self.tinggi}"

def cetak_luas(bentuk):
    print(bentuk.luas())

persegi = Persegi()
lingkaran = Lingkaran()
segitiga = Segitiga()
print()

cetak_luas(persegi)
cetak_luas(lingkaran)
cetak_luas(segitiga)