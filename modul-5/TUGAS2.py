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
        print("Laptop dinyalakan.")

    def matikan(self):
        print("Laptop dimatikan.")

    def gunakan(self, jam: int):
        self.energi_tersisa -= 10 * jam
        if self.energi_tersisa < 0:
            self.energi_tersisa = 0
            print("Baterai habis.")
        print(f"Setelah digunakan selama {jam} jam, energi tersisa: {self.energi_tersisa}%")

class Kulkas(PerangkatElektronik):
    def nyalakan(self):
        print("Kulkas dinyalakan.")

    def matikan(self):
        print("Kulkas dimatikan.")

    def gunakan(self, jam: int):
        self.energi_tersisa -= 5 * jam
        if self.energi_tersisa < 20:
            print("Energi rendah, kulkas butuh daya tambahan!")
        print(f"Setelah digunakan selama {jam} jam, energi tersisa: {self.energi_tersisa}%")


laptop = Laptop()
kulkas = Kulkas()

laptop.nyalakan()
laptop.gunakan(5)  
laptop.status()
laptop.matikan()

print()

laptop.nyalakan()
laptop.gunakan(2)  
laptop.status()
laptop.matikan()

print() 


kulkas.nyalakan()
kulkas.gunakan(14)  
kulkas.status()
kulkas.matikan()

print()

kulkas.nyalakan()
kulkas.gunakan(6)  
kulkas.status()
kulkas.matikan()
