from abc import ABC, abstractmethod

class Manusia(ABC):
    def __init__(self, nama):
        self.nama = nama

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
    def __init__(self, nama, pekerjaan, makanan):
        super().__init__(nama)
        self.pekerjaan = pekerjaan
        self.makanan = makanan

    def berbicara(self):
        print(f"Halo, perkenalkan nama saya {self.nama}")

    def bekerja(self):
        print(f"Saya saat ini sedang {self.pekerjaan}")

    def makan(self):
        print(f"Saya sedang makan {self.makanan}")

def main():
    nama = input("Masukkan Nama: ")
    pekerjaan = input("Masukkan Pekerjaan: ")
    makanan = input("Sedang makan apa?: ")

    manusia = Orang(nama, pekerjaan, makanan)

    manusia.berbicara()
    manusia.bekerja()
    manusia.makan()

if __name__ == "__main__":
    main()
