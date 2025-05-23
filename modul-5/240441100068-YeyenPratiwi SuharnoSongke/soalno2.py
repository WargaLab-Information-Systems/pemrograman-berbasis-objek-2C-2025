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
    def gunakan(self, jam):
        pass

    def status(self):
        print(f"Tipe perangkat: {self.__class__.__name__}")
        print(f"Energi tersisa: {self.energi_tersisa}%")
        print("-" * 30)

class Laptop(PerangkatElektronik):
    def nyalakan(self):
        print("Laptop dinyalakan.")

    def matikan(self):
        print("Laptop dimatikan.")

    def gunakan(self, jam):
        print(f"Laptop digunakan selama {jam} jam.")
        energi_dipakai = 10 * jam
        self.energi_tersisa -= energi_dipakai

        if self.energi_tersisa < 0:
            self.energi_tersisa = 0
            print("Baterai habis!")
        else:
            print("Laptop masih memiliki cukup energi.")

        self.status()

class Kulkas(PerangkatElektronik):
    def nyalakan(self):
        print("Kulkas dinyalakan.")

    def matikan(self):
        print("Kulkas dimatikan.")

    def gunakan(self, jam):
        print(f"Kulkas digunakan selama {jam} jam.")
        energi_dipakai = 5 * jam
        self.energi_tersisa -= energi_dipakai

        if self.energi_tersisa < 0:
            self.energi_tersisa = 0
            print("Energi kosong!")
        elif self.energi_tersisa < 20:
            print("Energi rendah, kulkas butuh daya tambahan!")
        else:
            print("Energi kulkas masih mencukupi.")

        self.status()


print("=== Laptop ===")
laptop = Laptop()
laptop.nyalakan()
laptop.gunakan(5)  
laptop.matikan()

print("\n=== Kulkas ===")
kulkas = Kulkas()
kulkas.nyalakan()
kulkas.gunakan(8) 
kulkas.matikan()

