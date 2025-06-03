# 1. Class Manusia
class Manusia:
    def __init__(self, nama, umur, alamat):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat
    
    def berjalan(self):
        print(f"{self.nama} sedang berjalan.")
    
    def berlari(self):
        print(f"{self.nama} sedang berlari.")

manusia1 = Manusia("Jansed Rivaldo", 19, "Medan")
manusia2 = Manusia("Riri Manik", 19, "Bandung")
manusia3 = Manusia("Agung Purba", 21, "Bogor")
manusia4 = Manusia("Chelsy Sinaga", 17, "Medan")
manusia5 = Manusia("Tamara Nainggolan", 18, "Medan")

manusia1.berjalan()
manusia3.berjalan()
manusia2.berlari()
manusia4. berlari ()
manusia5.berjalan()