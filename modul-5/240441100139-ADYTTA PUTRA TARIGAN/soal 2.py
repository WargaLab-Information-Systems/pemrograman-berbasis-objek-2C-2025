from abc import ABC, abstractmethod

class PerangkatElektronik(ABC):
    def __init__(self, tipe: str):  # <-- perbaikan: __init__ bukan _init_
        self.tipe = tipe
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
        print(f"Tipe perangkat: {self.tipe}")
        print(f"Energi tersisa: {self.energi_tersisa}%")

class Perangkat(PerangkatElektronik):
    def __init__(self, tipe: str):
        super().__init__(tipe)

    def nyalakan(self):
        print(f"{self.tipe} dinyalakan.")

    def matikan(self):
        print(f"{self.tipe} dimatikan.")

    def gunakan(self, jam: int):
        if self.tipe == "Laptop":
            pemakaian = 10 * jam
            self.energi_tersisa -= pemakaian
            if self.energi_tersisa <= 0:
                self.energi_tersisa = 0
                print("Baterai habis. Laptop mati.")
            else:
                print(f"Laptop digunakan selama {jam} jam.")
        elif self.tipe == "Kulkas":
            pemakaian = 5 * jam
            self.energi_tersisa -= pemakaian
            if self.energi_tersisa <= 0:
                self.energi_tersisa = 0
                print("Energi habis. Kulkas mati.")
            elif self.energi_tersisa < 20:
                print("Energi rendah, kulkas butuh daya tambahan!")
            print(f"Kulkas beroperasi selama {jam} jam.")
        else:
            print("Tipe perangkat tidak dikenali.")

def main():
    print("Pilih tipe perangkat:")
    print("1. Laptop")
    print("2. Kulkas")
    pilihan = input("Masukkan pilihan (1/2): ")

    if pilihan == "1":
        tipe = "Laptop"
    elif pilihan == "2":
        tipe = "Kulkas"
    else:
        print("Pilihan tidak valid. Harus 1 atau 2.")
        return

    perangkat = Perangkat(tipe)
    perangkat.nyalakan()

    jam_str = input("Berapa jam penggunaan? ")
    if not jam_str.isdigit():
        print("Jam harus berupa angka.")
        return

    jam = int(jam_str)
    perangkat.gunakan(jam)
    perangkat.status()
    perangkat.matikan()

if __name__ == "__main__":
    main()
