class manusia:
    def __init__(self, nama, umur, alamat):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat
    
    def berjalan(self):
        print(f"{self.nama} berumur {self.umur} tahun, yang tinggal di {self.alamat} berjalan menuju Stadion")

    def berlari(self):
        print(f"{self.nama} berumur {self.umur} tahun, yang tinggal di {self.alamat} berlari memutari Stadion")

manusia1 = manusia("Andi", 18, "Jl. Gatot")
manusia2 = manusia("Yanto", 20, "Jl. Sudirman")
manusia3 = manusia("Firman", 25, "Jl. Prabowo")
manusia4 = manusia("Suraji", 65, "Jl. Agung")
manusia5 = manusia("Fatimah", 50, "Jl. Kemuning")

print("-----" * 17)
manusia1.berjalan()
print("-----" * 17)
manusia2.berjalan()
print("-----" * 17)
manusia3.berlari()
print("-----" * 17)
manusia4.berjalan()
print("-----" * 17)
manusia5.berlari()
print("-----" * 17)

