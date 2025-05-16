class Manusia :
    def __init__(self, nama , umur, alamat):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat

    def berjalan(self):
        print(f"Nama  : {self.nama}")
        print(f"Umur  : {self.umur}")
        print(f"Alamat: {self.alamat}")
        print(f"Sedang berjalan")

    def berlari(self):
        print(f"Nama  : {self.nama}")
        print(f"Umur  : {self.umur}")
        print(f"Alamat: {self.alamat}")
        print(f"Sedang berlari")
    
    def renang(self):
        print(f"2")
        print("Sedang berenang")


manusia1 = Manusia("Ana", 17, "Bandung")
manusia2 = Manusia("Dani", 20, "Medan")
manusia3 = Manusia("Loli", 18, "Jakarta")
manusia4 = Manusia("Bulan", 19, "Surabaya")
manusia5 = Manusia("Anya", 21, "Padang Bulan")

manusia1.renang()
print()
manusia2.berlari()
print()
manusia3.berjalan()
print()
manusia4.berlari()
print()
manusia5.berjalan()
