class Manusia:
    def __init__(self, nama, umur, alamat):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat

    def berjalan(self):
        print(f"{self.nama} sedang berjalan.")

    def berlari(self):
        print(f"{self.nama} sedang berlari.")
        print("----------------------------------------")

    def tampilkan_info(self):
        print(f"Nama   : {self.nama}")
        print(f"Umur   : {self.umur} tahun")
        print(f"Alamat : {self.alamat}")


manusia1 = Manusia("Rena", 20, "Surabaya")
manusia2 = Manusia("Ken", 19, "Bandung")
manusia3 = Manusia("Yona", 18, "Blitar")
manusia4 = Manusia("Reino", 21, "Yogyakarta")
manusia5 = Manusia("Sera", 19, "Medan")


print("========== DATA MANUSIA ==========")
manusia1.tampilkan_info()
manusia1.berjalan()
manusia1.berlari()

manusia2.tampilkan_info()
manusia2.berjalan()
manusia2.berlari()

manusia3.tampilkan_info()
manusia3.berjalan()
manusia3.berlari()

manusia4.tampilkan_info()
manusia4.berjalan()
manusia4.berlari()

manusia5.tampilkan_info()
manusia5.berjalan()
manusia5.berlari()
print("==================================")
