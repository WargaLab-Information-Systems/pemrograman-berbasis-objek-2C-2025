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

class Karakter(Manusia):
    def berbicara(self):
        print("Saya senang kalau ada yang berbicara untuk membahas tentang teknologi.")

    def bekerja(self):
        print("Saya bekerja sebagai programmer di PT telkom Indonesia.")

    def makan(self):
        print("Saya suka makan Mie Goreng.")

nama = input("Masukkan nama karakter: ").lower()

karakter = Karakter()
karakter.berbicara()
karakter.bekerja()
karakter.makan()

# class nya 1 subclasnnya 1

