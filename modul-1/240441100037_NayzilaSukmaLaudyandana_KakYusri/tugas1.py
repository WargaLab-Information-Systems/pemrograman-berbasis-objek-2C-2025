class Manusia:
    def __init__(self, nama, umur, alamat):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat

    def berjalan(self):
        print(f"{self.nama} sedang berjalan.")

    def berlari(self):
        print(f"{self.nama} sedang berlari.")


manusia1 = Manusia("Andi", 20, "Jakarta")
manusia2 = Manusia("Budi", 22, "Bandung")
manusia3 = Manusia("Citra", 19, "Surabaya")
manusia4 = Manusia("Dewi", 21, "Yogyakarta")
manusia5 = Manusia("Eko", 23, "Medan")

manusia1.berjalan()
manusia2.berlari()
manusia3.berjalan()
manusia4.berlari()
manusia5.berjalan()
