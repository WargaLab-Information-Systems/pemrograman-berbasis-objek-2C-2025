from abc import ABC, abstractmethod

class Manusia(ABC):
    @abstractmethod
    def berbicara(self):
        pass

    @abstractmethod
    def bekerja(self):
        pass

    @abstractmethod
    def makan(self):
        pass

class Orang(Manusia):
    def __init__(self, nama, bicara, kerja, makan):
        self.nama = nama
        self.bicara = bicara
        self.kerja = kerja
        self.makanfav = makan

    def berbicara(self):
        print(f"Saya suka berbicara tentang {self.bicara}")

    def bekerja(self):
        print(f"Saya bekerja sebagai {self.kerja}")

    def makan(self):
        print(f"Saya suka makan {self.makanfav}")


list_orang = []

while True:
    print("=== Masukkan data orang ===")
    nama = input("Nama : ")
    bicara = input("Topik yang disukai untuk dibicarakan : ")
    kerja = input("Pekerjaan : ")
    makan = input("Makanan : ")

    orang = Orang(nama, bicara, kerja, makan)
    list_orang.append(orang)

    ulang = input("\nMau nambah lagi gaa? (y/n) : ")
    if ulang != 'y':
        break

print("\n=== Data Orang yang sudah diinput ===")
for orang in list_orang:
    print(f"-- {orang.nama} --")
    orang.berbicara()
    orang.bekerja()
    orang.makan()
    print()