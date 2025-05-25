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
    def gunakan(self, jam):
        pass

    def status(self):
        print(f"Status {self.nama}: Energi {self.energi_tersisa}%")

class Laptop(PerangkatElektronik):
    def __init__(self):
        super().__init__("Laptop")

    def nyalakan(self):
        print("Laptop dinyalakan.")

    def matikan(self):
        print("Laptop dimatikan.")

    def gunakan(self, jam):
        print(f"Laptop digunakan selama {jam} jam.")
        self.energi_tersisa -= 10 * jam
        if self.energi_tersisa < 0:
            self.energi_tersisa = 0
            print("Laptop: Baterai habis!")

class Kulkas(PerangkatElektronik):
    def __init__(self):
        super().__init__("Kulkas")

    def nyalakan(self):
        print("Kulkas dinyalakan.")

    def matikan(self):
        print("Kulkas dimatikan.")

    def gunakan(self, jam):
        print(f"Kulkas digunakan selama {jam} jam.")
        self.energi_tersisa -= 5 * jam
        if self.energi_tersisa < 0:
            self.energi_tersisa = 0
        if self.energi_tersisa < 20:
            print("Kulkas: Energi rendah, butuh daya tambahan!")

print("=== LAPTOP ===")
l = Laptop()
l.nyalakan()
l.gunakan(3)
l.status()
l.matikan()

print("\n=== KULKAS ===")
k = Kulkas()
k.nyalakan()
k.gunakan(10)
k.status()
k.matikan()