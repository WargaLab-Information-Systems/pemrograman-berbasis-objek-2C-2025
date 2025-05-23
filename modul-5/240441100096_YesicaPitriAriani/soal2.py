from abc import ABC, abstractmethod

class PerangkatElektronik(ABC):
    def __init__(self):
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
        print(f"Tipe perangkat: {self.__class__.__name__}")
        print(f"Energi tersisa: {self.energi_tersisa}%")

class Laptop(PerangkatElektronik):
    def nyalakan(self):
        print("Laptop dinyalakan")

    def matikan(self):
        print("Laptop dimatikan")

    def gunakan(self, jam: int):
        print(f"Laptop digunakan selama {jam} jam.")
        self.energi_tersisa -= 10 * jam
        if self.energi_tersisa < 0:
            self.energi_tersisa = 0
            print("Baterai habis!")

class Kulkas(PerangkatElektronik):
    def nyalakan(self):
        print("Kulkas dinyalakan")

    def matikan(self):
        print("Kulkas dimatikan")

    def gunakan(self, jam: int):
        print(f"Kulkas digunakan selama {jam} jam")
        self.energi_tersisa -= 5 * jam
        if self.energi_tersisa < 0:
            self.energi_tersisa = 0
            print("daya kulkas habis")
        if self.energi_tersisa < 20:
            print("Energi rendah, kulkas butuh daya tambahan!")

laptop = Laptop()
laptop.nyalakan()
laptop.gunakan(3)  
laptop.status()
laptop.matikan()

print("-" * 30)

kulkas = Kulkas()
kulkas.nyalakan()
kulkas.gunakan(17) 
kulkas.status()
kulkas.matikan()
