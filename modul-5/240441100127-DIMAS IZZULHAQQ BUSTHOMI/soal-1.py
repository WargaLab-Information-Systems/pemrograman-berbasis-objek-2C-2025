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
        print(f"Haloo masyrakat! saya {self.nama}")

    def bekerja(self):
        print(f"Pekerjaan saya adalah {self.pekerjaan}")

    def makan(self):
        print(f"makanan favorit saya {self.makanan}")

while True:
    nama = input("Nama: ")
    pekerjaan = input("Pekerjaan: ")
    makanan = input("Makanan: ")

    manusia = Orang(nama, pekerjaan, makanan)

    manusia.berbicara()
    manusia.bekerja()
    manusia.makan()