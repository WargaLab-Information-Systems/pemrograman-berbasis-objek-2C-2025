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
        print("-----------")

    def isi_daya(self, jumlah: int):
        self.energi_tersisa += jumlah
        print(f"Perangkat diisi daya sebesar {jumlah}%. Energi sekarang: {self.energi_tersisa}%")

class Laptop(PerangkatElektronik):
    def nyalakan(self):
        print("Laptop menyala. Selamat bekerja!")

    def matikan(self):
        print("Laptop dimatikan. Sampai jumpa!")

    def gunakan(self, jam: int):
        self.energi_tersisa -= 10 * jam
        if self.energi_tersisa < 0:
            self.energi_tersisa = 0
            print("Baterai laptop habis! Segera isi daya.")

class Kulkas(PerangkatElektronik):
    def nyalakan(self):
        print("Kulkas dinyalakan. Pendinginan dimulai.")

    def matikan(self):
        print("Kulkas dimatikan. Jangan terlalu lama ya!")

    def gunakan(self, jam: int):
        self.energi_tersisa -= 5 * jam
        if self.energi_tersisa < 0:
            self.energi_tersisa = 0
        if self.energi_tersisa < 20:
            print("Energi rendah, kulkas butuh daya tambahan!")

def uji_perangkat(perangkat: PerangkatElektronik, jam: int):
    perangkat.nyalakan()
    perangkat.gunakan(jam)
    perangkat.status()

    isi = input("Ingin mengisi daya perangkat ini? (y/n): ")
    if isi.lower() == 'y':
        while True:
            try:
                jumlah = int(input("Masukkan jumlah energi yang ingin ditambahkan (%): "))
                if jumlah < 0:
                    print("Jumlah tidak boleh negatif.")
                    continue
                if perangkat.energi_tersisa + jumlah > 100:
                    print("Pengisian melebihi kapasitas 100%. Coba lagi.")
                else:
                    perangkat.isi_daya(jumlah)
                    perangkat.status()
                    break
            except ValueError:
                print("Input tidak valid. Harus berupa angka.")

    perangkat.matikan()
    print("===========\n")

nama1 = input("Masukkan tipe perangkat pertama (Laptop/Kulkas): ")
jam1 = int(input("Masukkan durasi pemakaian (jam): "))
if nama1.lower() == "laptop":
    uji_perangkat(Laptop(), jam1)
elif nama1.lower() == "kulkas":
    uji_perangkat(Kulkas(), jam1)
else:
    print("Tipe perangkat tidak dikenal.")

nama2 = input("Masukkan tipe perangkat kedua (Laptop/Kulkas): ")
jam2 = int(input("Masukkan durasi pemakaian (jam): "))
if nama2.lower() == "laptop":
    uji_perangkat(Laptop(), jam2)
elif nama2.lower() == "kulkas":
    uji_perangkat(Kulkas(), jam2)
else:
    print("Tipe perangkat tidak dikenal.")