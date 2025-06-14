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

    # Method status
    def status(self):
        print(f"Tipe perangkat: {type(self).__name__}")
        print(f"Energi tersisa: {self.energi_tersisa}%\n")

# Subclass Laptop
class Laptop(PerangkatElektronik):
    def nyalakan(self):
        print("Laptop dinyalakan.")

    def matikan(self):
        print("Laptop dimatikan.")

    def gunakan(self, jam: int):
        penggunaan = 10 * jam
        self.energi_tersisa -= penggunaan
        if self.energi_tersisa < 0:
            self.energi_tersisa = 0
            print("Baterai habis! Harap diisi ulang.")
        else:
            print(f"Laptop digunakan selama {jam} jam.")

# Subclass Kulkas
class Kulkas(PerangkatElektronik):
    def nyalakan(self):
        print("Kulkas dinyalakan.")

    def matikan(self):
        print("Kulkas dimatikan.")

    def gunakan(self, jam: int):
        penggunaan = 5 * jam
        self.energi_tersisa -= penggunaan
        if self.energi_tersisa < 0:
            self.energi_tersisa = 0
        print(f"Kulkas beroperasi selama {jam} jam.")
        if self.energi_tersisa < 20:
            print("Energi rendah, kulkas butuh daya tambahan!")

print("=== Laptop ===")
laptop_kerja = Laptop()
laptop_kerja.nyalakan()
laptop_kerja.gunakan(5)  
laptop_kerja.status()
laptop_kerja.gunakan(6)  
laptop_kerja.status()
laptop_kerja.matikan()

print("\n=== Kulkas ===")
kulkas_dapur = Kulkas()
kulkas_dapur.nyalakan()
kulkas_dapur.gunakan(10)  
kulkas_dapur.status()
kulkas_dapur.gunakan(7)   
kulkas_dapur.status()
kulkas_dapur.matikan()