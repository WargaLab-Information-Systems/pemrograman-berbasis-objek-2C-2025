class manusia:
    def __init__(self, nama, umur, alamat):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat

    def berjalan(self):
        print(f"{self.nama} sedang berjalan")

    def berlari(self):
        print(f"{self.nama} sedang berlari")

manusia1 = manusia("Fina", 18,"Bandung")
manusia2 = manusia("El", 17,"Semarang")
manusia3 = manusia("Elfina", 16,"Lamongan")
manusia4 = manusia("Lukna", 18,"Bojonegoro")
manusia5 = manusia("Elle", 19,"Malang")

manusia1.berjalan()
manusia2.berlari()
manusia3.berlari()
manusia4.berjalan()
manusia5.berjalan()