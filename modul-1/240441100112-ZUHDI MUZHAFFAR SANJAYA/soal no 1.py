class Manusia:
    def __init__(self, nama, umur, alamat):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat

    def berjalan(self):
        print(f"{self.nama} sedang berjalan")

    def berlari(self):
        print(f"{self.nama} sedang berlari")


manusia1 = Manusia("Rudi", 30, "Gresik")
manusia2 = Manusia("Haikal", 25, "Sampang")
manusia3 = Manusia("Ledi", 20, "Sidoarjo")
manusia4 = Manusia("Tika", 26, "Malang")
manusia5 = Manusia("Wafi", 18, "Aceh")


manusia1.berjalan()
manusia2.berlari()
manusia3.berjalan()
manusia4.berlari()
manusia5.berjalan()