class Manusia:
    def __init__(self, nama, umur, alamat):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat
    
    def berjalan(self):
        print(f"{self.nama} sedang berjalan.")
    
    def berlari(self):
        print(f"{self.nama} sedang berlari.")

manusia1 = Manusia("Ali", 25, "Jakarta")
manusia2 = Manusia("Budi", 30, "Bandung")
manusia3 = Manusia("Citra", 22, "Surabaya")
manusia4 = Manusia("Dewi", 27, "Yogyakarta")
manusia5 = Manusia("Eko", 35, "Semarang")


manusia1.berjalan()
manusia2.berlari()
manusia3.berjalan()
manusia4.berjalan()
manusia5.berlari()