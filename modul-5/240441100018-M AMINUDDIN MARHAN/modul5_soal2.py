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

class Laptop(PerangkatElektronik):
    def __init__(self):
        super().__init__()

    def nyalakan(self):
        print("Laptop dinyalakan.")

    def matikan(self):
        print("Laptop dimatikan.")

    def gunakan(self, jam: int):
        if not isinstance(jam, int):
            print("Error: Jam harus bertipe integer.")
            return
        if jam > 0:
            if self.energi_tersisa < 0:
                print("Baterai habis.")
            else:
                self.energi_tersisa -= 10 * jam
        else:
            print("Durasi penggunaan harus lebih dari 0 jam.")

    def status(self):
        print("Tipe perangkat: Laptop")
        print(f"Energi tersisa: {max(0, self.energi_tersisa)}%")

class Kulkas(PerangkatElektronik):
    def __init__(self):
        super().__init__()

    def nyalakan(self):
        print("Kulkas dinyalakan.")

    def matikan(self):
        print("Kulkas dimatikan.")

    def gunakan(self, jam: int):
        if not isinstance(jam, int):
            print("Error: Jam harus bertipe integer.")
            return
        if jam > 0:
            if self.energi_tersisa < 20:
                print("Energi rendah, kulkas butuh daya tambahan!")
            else:
                self.energi_tersisa -= 5 * jam
        else:
            print("Durasi penggunaan harus lebih dari 0 jam.")

    def status(self):
        print("Tipe perangkat: Kulkas")
        print(f"Energi tersisa: {max(0, self.energi_tersisa)}%")

laptop = Laptop()
kulkas = Kulkas()

laptop.nyalakan()
kulkas.nyalakan()
print()

laptop.gunakan(1)
kulkas.gunakan(1)
laptop.status()
kulkas.status()
print()

laptop.gunakan(2)
kulkas.gunakan(3)
laptop.status()
kulkas.status()
print()

laptop.matikan()
kulkas.matikan()