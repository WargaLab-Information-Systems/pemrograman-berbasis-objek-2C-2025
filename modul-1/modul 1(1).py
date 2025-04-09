class manusia:
    def __init__(self, nama, umur, alamat):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat

    def berjalan(self):
        return f"{self.nama} umur {self.umur} dengan alamat {self.alamat} sedang berjalan"
    
    def berlari(self):
        return f"{self.nama} umur {self.umur} dengan alamat {self.alamat} sedang berlari"
    
manusia1 = manusia ("alfi", 19, "ngasem")
manusia2 = manusia ("yaya", 20, "ndander")
manusia3 = manusia ("fida", 20, "bakalan")
manusia4 = manusia ("nurpa", 19, "cepu")
manusia5 = manusia ("anila", 19, "bandar")

for m in [manusia1, manusia2, manusia3, manusia4, manusia5]:
    print("-"*50)
    print(m.berjalan())
    print(m.berlari())