from abc import ABC, abstractmethod

class Manusia(ABC):
    @abstractmethod
    def berbicara(self):
        pass
    def bekerja(self):
        pass
    def makan(self):
        pass


class orang (Manusia):
    def berbicara(self):
        nama = input("masukkan nama yang ingin anda cari: ")
        print(f"namanya adalah {nama}")
        print("dia berbicara dengan nada keras")
    def bekerja(self):
        print("dia bekerja di PT.Taruna Jaya")
    def makan(self):
        print("makanan favoritnya bakso")

namaorg = orang()
namaorg.berbicara()
namaorg.bekerja()
namaorg.makan()

#inputan nama hanya 1 soalnya methodnya sama saja


