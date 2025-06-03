from abc import ABC, abstractmethod

class Perangkat_Elektronik(ABC):
    def __init__(self):
        self.energi_tersisa = 100
    @abstractmethod
    def nyalakan(self):
        pass
    def matikan(self):
        pass
    def gunakan(self, jam):
        pass

class Perangkat(Perangkat_Elektronik):
    def __init__(self):
        super().__init__()
        self.nama = ""  
    def nyalakan(self):
        print(f"{self.nama} sudah menyala")
    def matikan(self):
        print(f"{self.nama} sudah dimatikan")
    def gunakan(self, jam):
        if self.nama == 1:
            self.energi_tersisa -= 10 * jam
            if self.energi_tersisa <= 0:
                self.energi_tersisa = 0
                print(f"Baterai habis. {self.nama} mati.")
            else:
                print(f"{self.nama} digunakan selama {jam} jam.")
                print(f"Energi tersisa: {self.energi_tersisa}%")
        elif self.nama == 2:
            self.energi_tersisa -= 5 * jam
            if self.energi_tersisa <= 20:
                print(f"{self.nama} butuh daya tambahan")
            else:
                print(f"{self.nama} digunakan selama {jam} jam.")
            print(f"Energi tersisa: {self.energi_tersisa}%")
        else:
            print("Jenis perangkat tidak dikenali.")

print("\nSELAMAT MENGGUNAKAN LAYANAN ELEKTRONIK")
print("1. Laptop")
print("2. Kulkas")
nama = int(input("nama alat: "))
energi = int(input("energi tersisa: "))
jam = int(input("durasi penggunaan: "))

if nama == 1:
    perangkat = Perangkat()
elif nama == 2:
    perangkat = Perangkat()
else:
    print("tidak valid")
    exit()  

perangkat.nama = nama
perangkat.energi_tersisa = energi
perangkat.nyalakan()
perangkat.matikan()
perangkat.gunakan(jam)

#intinya class digabung dengan menggunakan if jika dia nge input 1. laptop dia akan mengeluarkan dari gunakan_laptop begitu sebaliknya untuk yang kulkas