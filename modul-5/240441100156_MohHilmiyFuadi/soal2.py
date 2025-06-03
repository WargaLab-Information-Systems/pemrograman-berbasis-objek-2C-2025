from abc import ABC, abstractmethod

class PerangkatElektronik (ABC):
    @abstractmethod
    def nyalakan(self):
        pass

    @abstractmethod
    def matikan(self):
        pass

    @abstractmethod
    def gunakan(self, jam: int):
        pass

    def __init__(self, nama):
        self.nama = nama
        self.energi_tersisa = 100

    def status(self):
        print(f"Tipe perangkat : {self.nama}")
        print(f"Energi tersisa : {self.energi_tersisa}%\n")


class Perangkat(PerangkatElektronik):
    def nyalakan(self):
        print(f"-- perangkat dinyalakan --")

    def matikan(self):
        print(f"-- perangkat dimatikan --")

    def gunakan(self, jam: int):
        if nama == "kulkas":
            self.energi_tersisa -= 5 * jam
            print(f"-- Kulkas berjalan selama {jam} jam --")
            if self.energi_tersisa < 20:
                print("Energi rendah, kulkas butuh daya tambahan!!!!")
        elif nama == "laptop":
            self.energi_tersisa -= 10 * jam
            if self.energi_tersisa < 0:
                self.energi_tersisa = 0 
                print("-- Baterai habis!!! --")
            else:
                print(f"-- Laptop digunakan selama {jam} jam --")
        else:
            print("-- data tersebut tidak ada --")

        perangkat.status()

while True:
    print("\n=== pilih Perangkat ===")
    print("1. kulkas")
    print("2. laptop")
    nama = input("Nama perangkat : ")
    print()

    perangkat = Perangkat(nama)

    perangkat.nyalakan()
    print()

    jam = int(input(f"Berapa jam {nama} digunakan? "))
    perangkat.gunakan(jam)

    perangkat.matikan()

    ulang = input("\nMau pilih lagi gaa? (y/n) : ")
    if ulang != 'y':
        print("-- Terimakasih --")
        break