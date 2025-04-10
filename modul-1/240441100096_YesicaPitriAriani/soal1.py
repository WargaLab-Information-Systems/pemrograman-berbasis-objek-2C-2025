class manusia:
    def __init__(self, nama, umur, alamat):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat
        
    def berjalan(self):
        print(f"{self.nama} sedang berjalan")
    
    def berlari(self):
        print(f"{self.nama} sedang berlari")

manusia1 = manusia("yesica", 19, "bojonegoro")
manusia2 = manusia("windy", 20, "bojonegoro")
manusia3 = manusia("yeyen", 21, "kalimantan")
manusia4 = manusia("naisa", 18, "madura")
manusia5 = manusia("eka", 19, "cepu")

manusia1.berjalan()
manusia2.berjalan()
manusia3.berjalan()
manusia4.berlari()
manusia5.berlari()

