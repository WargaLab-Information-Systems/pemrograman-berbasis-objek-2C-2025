from abc import ABC, abstractmethod

class PerangkatElektronik(ABC):
    def __init__(self, nama_perangkat):
        self.energi_tersisa = 100  
        self.nama_perangkat = nama_perangkat

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
        print("=== STATUS PERANGKAT ===")
        print(f"Nama Perangkat     : {self.nama_perangkat}")
        print(f"Sisa Energi Baterai: {self.energi_tersisa}%")
        print("========================\n")

class Laptop(PerangkatElektronik):
    def __init__(self):
        super().__init__("Laptop")

    def nyalakan(self):
        print("Laptop dinyalakan.")

    def matikan(self):
        print("Laptop dimatikan.")

    def gunakan(self, jam: int):
        if jam <= 0:
            print("Waktu penggunaan harus lebih dari 0 jam.")
            return
        print(f"Menggunakan Laptop selama {jam} jam.")
        self.energi_tersisa -= 10 * jam
        if self.energi_tersisa < 0:
            self.energi_tersisa = 0
            print("Baterai habis!")
        self.status()

class Kulkas(PerangkatElektronik):
    def __init__(self):
        super().__init__("Kulkas")

    def nyalakan(self):
        print("Kulkas dinyalakan.")

    def matikan(self):
        print("Kulkas dimatikan.")

    def gunakan(self, jam: int):
        if jam <= 0:
            print("Waktu penggunaan harus lebih dari 0 jam.")
            return
        print(f"Menggunakan Kulkas selama {jam} jam.")
        self.energi_tersisa -= 5 * jam
        if self.energi_tersisa < 20:
            print("Energi rendah, kulkas butuh daya tambahan!")
        if self.energi_tersisa < 0:
            self.energi_tersisa = 0
        self.status()

# === UJI COBA ===

print("=== UJI COBA LAPTOP ===")
laptop = Laptop()
laptop.nyalakan()
laptop.gunakan(2) 
laptop.gunakan(5) 
laptop.matikan()

print("\n=== UJI COBA KULKAS ===")
kulkas = Kulkas()
kulkas.nyalakan()
kulkas.gunakan(2) 
kulkas.gunakan(3)   
kulkas.matikan()