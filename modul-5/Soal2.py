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
        print(f"Jenis Perangkat : {self.__class__.__name__}")
        print(f"Energi Tersisa  : {self.energi_tersisa}%")
        print()

class Laptop(PerangkatElektronik):
    def nyalakan(self):
        print("Laptop Telah Dinyalakan")
        
    def matikan(self):
        print("Laptop Telah Dimatikan")
        
    def gunakan(self, jam: int):
        pengurangan = 10 * jam
        self.energi_tersisa -= pengurangan
        if self.energi_tersisa < 0:
            self.energi_tersisa = 0
            print("Baterai Melemah")
        else:
            print(f"Kulkas Digunakan Selama {jam} jam.")
    
class Kulkas(PerangkatElektronik):
    def nyalakan(self):
        print("Kulkas Telah Dinyalakan")
        
    def matikan(self):
        print("Kulkas Telah Dimatikan")
        
    def gunakan(self, jam: int):
        pengurangan = 5 * jam
        self.energi_tersisa -= pengurangan
        print(f"Kulkas Digunakan Selama {jam} jam.")
        if self.energi_tersisa < 20:
            print("Energi Terlalu Lemah")
        if self.energi_tersisa < 0:
            self.energi_tersisa = 0
            
print("==== Laptop ====")
Laptop = Laptop()
Laptop.nyalakan()
Laptop.gunakan(3)
Laptop.matikan()
Laptop.status()

print("\n==== Kulkas ====")
Kulkas = Kulkas()
Kulkas.nyalakan()
Kulkas.gunakan(10)
Kulkas.matikan()
Kulkas.status()