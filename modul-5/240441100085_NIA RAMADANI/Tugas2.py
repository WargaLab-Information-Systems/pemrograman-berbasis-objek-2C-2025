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
        print(f"Tipe Perangkat : {self.__class__.__name__}")
        print(f"Energi Tersisa : {self.energi_tersisa}%\n")

class Laptop(PerangkatElektronik):
    def nyalakan(self):
        print("Laptop telah dinyalakan.")

    def matikan(self):
        print("Laptop telah dimatikan.")

    def gunakan(self, jam: int):
        energi_digunakan = 10 * jam
        self.energi_tersisa -= energi_digunakan

        if self.energi_tersisa <= 0:
            self.energi_tersisa = 0
            print("Baterai telah habis!")
        else:
            print(f"Laptop telah digunakan selama {jam} jam.")


class Kulkas(PerangkatElektronik):
    def nyalakan(self):
        print("Kulkas telah dinyalakan.")

    def matikan(self):
        print("Kulkas telah dimatikan.")

    def gunakan(self, jam: int):
        energi_digunakan = 5 * jam
        self.energi_tersisa -= energi_digunakan

        print(f"Kulkas digunakan selama {jam} jam.")
        if self.energi_tersisa < 20:
            print("Energi rendah, kulkas butuh daya tambahan!")




print("\n===== DAFTAR PERANGKAT ELEKTRONIK =====\n")

laptop = Laptop()
print(">>> Pengujian Laptop\n")
laptop.nyalakan()
laptop.gunakan(5)
laptop.matikan()
laptop.status()

print("========================================\n")

kulkas = Kulkas()
print(">>> Pengujian Kulkas\n")
kulkas.nyalakan()
kulkas.gunakan(10)
kulkas.matikan()
kulkas.status()


