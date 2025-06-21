from abc import ABC, abstractmethod

class Perangkat_eletronik(ABC):
    def __init__(self):
        self.energi_tersisa = 100

    @abstractmethod
    def nyalakan(self):
        pass
    @abstractmethod
    def matikan(self):
        pass
    @abstractmethod
    def gunakan(self,jam: int):
        pass
    def status(self):
        print(f"Tipe perangkat :{self.__class__.__name__}")
        print(f"Energi tersisa : {self.energi_tersisa}%")

class Laptop(Perangkat_eletronik):
    def nyalakan(self):
        print ("laptop dinyalakan") 
    def matikan(self):
        print("laptop dimatikan")
    def gunakan(self,jam : int):
        print(f"laptop digunakan selama {jam}jam.")
        self.energi_tersisa -= 10* jam
        if self.energi_tersisa <0:
            self.energi_tersisa = 0
            print("Baterai habis!")

class Kulkas(Perangkat_eletronik):
    def nyalakan(self):
        print ("kulkas dinyalakan") 
    def matikan(self):
        print("kulkas dimatikan")
    def gunakan (self,jam:int):
        print(f"kulkas digunakan selama {jam}jam.")
        self.energi_tersisa -= 5* jam
        if self.energi_tersisa < 20:
            print("Energi rendah, kulkas butuh daya tambahan!")
        
laptop = Laptop()
laptop.nyalakan()
laptop.gunakan(8) 
laptop.status()
laptop.matikan()
laptop.gunakan(1) 
laptop.status()


kulkas = Kulkas()
kulkas.nyalakan()
kulkas.gunakan(10)  
kulkas.status()
kulkas.matikan()
kulkas.gunakan(2)
kulkas.status()