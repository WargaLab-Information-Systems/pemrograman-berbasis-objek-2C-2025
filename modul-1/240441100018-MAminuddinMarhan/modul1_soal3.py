class Kucing:
    def __init__(self):
        self.nama = ""
        self.berat = 0
        self.usia = 0
    def input_kucing(self):
        try:
            self.nama = str(input("Masukkan Nama Hewan : "))
            self.berat = float(input("Masukkan Berat Hewan: "))
            if self.berat > 0:
                self.usia = float(input("Masukkan Usia Hewan : "))
                if self.usia > 0:
                    print()
                    return True
                else:
                    return False
            else:
                return False
        except ValueError:
            print("Input Tidak Valid")
            return False
    def tampilkan_kucing(self):
        print(f"Nama Hewan : {self.nama}")
        print(f"Berat Hewan: {self.berat} kg")
        print(f"Usia Hewan : {self.usia} Tahun")
        print()
class Anjing:
    def __init__(self):
        self.nama = ""
        self.berat = 0
        self.usia = 0
    def input_anjing(self):
        try:
            self.nama = str(input("Masukkan Nama Hewan : "))
            self.berat = float(input("Masukkan Berat Hewan: "))
            if self.berat > 0:
                self.usia = float(input("Masukkan Usia Hewan : "))
                if self.usia > 0:
                    print()
                    return True
                else:
                    return False
            else:
                return False
        except ValueError:
            print("Input Tidak Valid")
            return False
    def tampilkan_anjing(self):
        print(f"Nama Hewan : {self.nama}")
        print(f"Berat Hewan: {self.berat} kg")
        print(f"Usia Hewan : {self.usia} Tahun")
        print()
class Kura:
    def __init__(self):
        self.nama = ""
        self.berat = 0
        self.usia = 0
    def input_kura(self):
        try:
            self.nama = str(input("Masukkan Nama Hewan : "))
            self.berat = float(input("Masukkan Berat Hewan: "))
            if self.berat > 0:
                self.usia = float(input("Masukkan Usia Hewan : "))
                if self.usia > 0:
                    print()
                    return True
                else:
                    return False
            else:
                return False
        except ValueError:
            print("Input Tidak Valid")
            return False
    def tampilkan_kura(self):
        print(f"Nama Hewan : {self.nama}")
        print(f"Berat Hewan: {self.berat} kg")
        print(f"Usia Hewan : {self.usia} Tahun")
        print()
print("\n---Class Hewan: Kucing---")
binatang_kucing = []
for i in range(0, 3):
    hewan1 = Kucing()
    while not hewan1.input_kucing():
        print("Input tidak valid, silakan coba lagi")
    binatang_kucing.append(hewan1)
print("\n---Class Hewan: Anjing---")
binatang_anjing = []
for i in range(0, 3):
    hewan2 = Anjing()
    while not hewan2.input_anjing():
        print("Input tidak valid, silakan coba lagi")
    binatang_anjing.append(hewan2)
print("\n---Class Hewan: Kura---")
binatang_kura = []
for i in range(0, 3):
    hewan3 = Kura()
    while not hewan3.input_kura():
        print("Input tidak valid, silakan coba lagi")
    binatang_kura.append(hewan3)
print("\n---DAFTAR HEWAN---")
print("\n---Class Hewan: Kucing---")
for hewan1 in binatang_kucing:
    hewan1.tampilkan_kucing()
print("\n---Class Hewan: Anjing---")
for hewan2 in binatang_anjing:
    hewan2.tampilkan_anjing()
print("\n---Class Hewan: Kura---")
for hewan3 in binatang_kura:
    hewan3.tampilkan_kura()