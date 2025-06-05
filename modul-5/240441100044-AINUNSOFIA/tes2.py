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
        print(f"Energi tersisa: {self.energi_tersisa}%\n")


# Subclass Laptop
class Laptop(PerangkatElektronik):
    def nyalakan(self):
        print("Laptop dinyalakan.")

    def matikan(self):
        print("Laptop dimatikan.")

    def gunakan(self, jam: int):
        print(f"Laptop digunakan selama {jam} jam.")
        self.energi_tersisa -= 10 * jam
        if self.energi_tersisa <=5:
            print("Baterai sekarat! Harap diisi ulang.")
        elif self.energi_tersisa == 0:
            print("Baterai habis! Laptop dimatikan.")                
        self.status()


# Subclass Kulkas
class Kulkas(PerangkatElektronik):
    def nyalakan(self):
        print("Kulkas dinyalakan.")

    def matikan(self):
        print("Kulkas dimatikan.")

    def gunakan(self, jam: int):
        print(f"Kulkas dihidupkan selama {jam} jam.")
        self.energi_tersisa -= 5 * jam
        if self.energi_tersisa < 20:
            print("Energi kulkas rendah, kulkas butuh daya tambahan!")
        if self.energi_tersisa <=0:
            self.energi_tersisa = 0
        self.status()


# Membuat objek dan menguji semua metode
print("=== TEST LAPTOP ===")
laptop = Laptop()
laptop.nyalakan()
laptop.gunakan(9)
laptop.matikan()

print("\n=== TEST KULKAS ===")
kulkas = Kulkas()
kulkas.nyalakan()
kulkas.gunakan(-9)
kulkas.matikan()