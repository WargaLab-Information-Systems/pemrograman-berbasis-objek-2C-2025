from abc import ABC, abstractmethod

class PerangkatElektronik(ABC):
    def __init__(self, nama):
        self.nama = nama
        self.energi_tersisa = 100

    @abstractmethod
    def nyalakan(self):
        pass

    @abstractmethod
    def matikan(self):
        pass

    @abstractmethod
    def gunakan(self, jam: int):
        pass

    def status(self):
        print(f" - Tipe Perangkat      : {self.nama}")
        print(f" - Energi Tersisa      : {self.energi_tersisa}%\n")


class Laptop(PerangkatElektronik):
    def __init__(self):
        super().__init__("Laptop")

    def nyalakan(self):
        print(" <> Laptop telah dinyalakan\n")

    def matikan(self):
        print(" <> Laptop telah dimatikan\n")

    def gunakan(self, jam: int):
        print(f"{self.nama} telah digunakan selama {jam} jam")
        self.energi_tersisa -= 10 * jam
        self.status()
        if self.energi_tersisa == 0:
            print("!! Batrai laptop habis, segera isi daya.\n")


class Kulkas(PerangkatElektronik):
    def __init__(self):
        super().__init__("Kulkas")

    def nyalakan(self):
        print(" <> Kulkas telah dinyalakan\n")

    def matikan(self):
        print(" <> Kulkas telah dimatikan\n")

    def gunakan(self, jam: int):
        print(f"{self.nama} telah digunakan selama {jam} jam")
        self.energi_tersisa -= 5 * jam
        self.status()
        if self.energi_tersisa < 20:
            print("!! Energi rendah, kulkas butuh daya tambahan\n")


print("\n=========== LAPTOP ===========\n")
lpt = Laptop()
lpt.nyalakan()
lpt.gunakan(4)
lpt.gunakan(6)
lpt.matikan()


print("=========== KULKAS ============\n")
kls = Kulkas()
kls.nyalakan()
kls.gunakan(8)
kls.gunakan(9)
kls.matikan()