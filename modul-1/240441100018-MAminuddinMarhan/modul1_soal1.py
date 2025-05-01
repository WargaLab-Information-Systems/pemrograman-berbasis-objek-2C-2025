class manusia:
    def __init__(self, nama, umur, alamat):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat
    def tampilkan(self):
        print("---DATA ORANG---")
        print("Nama  :", self.nama)
        print("Usia  :", self.umur, "Tahun")
        print("Alamat:", self.alamat)
        print()
    def berjalan(self):
        print(f"{self.nama} sedang berjalan dengan kecepatan 5km/jam.")
    def berlari(self):
        print(f"{self.nama} sedang berlari dengan kecepatan 20km/jam")
manusia1 = manusia("Amin", 19, "Pakis")
manusia2 = manusia("Matt", 30, "Ngawi")
manusia3 = manusia("Foggy", 28, "Bogor")
manusia4 = manusia("Karen", 15, "Nganjuk")
manusia5 = manusia("Wilson", 45, "Surabaya")
manusia1.tampilkan()
manusia2.tampilkan()
manusia3.tampilkan()
manusia4.tampilkan()
manusia5.tampilkan()
manusia1.berjalan()
manusia2.berlari()
manusia3.berlari()
manusia4.berjalan()
manusia5.berlari()