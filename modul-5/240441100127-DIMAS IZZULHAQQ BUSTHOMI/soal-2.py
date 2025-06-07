from abc import ABC, abstractmethod

class PerangkatElektronik(ABC):
    def __init__(self, tipe):
        self.type = tipe
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
        print(f"Tipe perangkat : {self.type}")
        print(f"Energi tersisa : {self.energi_tersisa}%")

class Perangkat(PerangkatElektronik):
    def __init__(self, tipe):
        super().__init__(tipe)

    def nyalakan(self):
        print(f"{self.type} dinyalakan.")

    def matikan(self):
        print(f"{self.type} Leptop dimatikan.")
    
    def gunakan(self, jam):
        if self.type == "Leptop":
            terpakai = 10 * jam
            self.energi_tersisa -= terpakai
            
            if self.energi_tersisa < 0:
                self.energi_tersisa = 0
                print("Baterai habis dan Laptop mati total.")
            else:
                print(f"Leptop dipakai selama {jam} jam.")
        elif self.type == "Kulkas":
            terpakai = 5 * jam
            self.energi_tersisa -= terpakai
            if self.energi_tersisa < 20:
                print("“Energi rendah, kulkas butuh daya tambahan!")
            if self.energi_tersisa < 0:
                self.energi_tersisa = 0

        else:
            print("Perangkat tidak ada.")

while True:
    print("1. Leptop")
    print("2. Kulkas")
    print("3. Keluar")
    print("-----" * 8)
    pilih = input("Pilih menu : ")
    print("-----" * 8)
    if pilih == "1":
        tipe = "Leptop"
    elif pilih == "2":
        tipe = "Kulkas"
    else:
        print("Pilihan tidak valid")

    p = Perangkat(tipe)
    p.nyalakan()

    jam = input("Jam pemakaian : ")

    jam = int(jam)
    p.gunakan(jam)
    p.status()
    p.matikan()