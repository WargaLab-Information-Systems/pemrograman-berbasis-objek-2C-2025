class Manusia:
    def __init__(self, nama, umur, alamat):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat
    
    def berjalan(self):
        return f"{self.nama} sedang berjalan"
    
    def berlari(self):
        return f"{self.nama} sedang berlari"

orang1 = Manusia("Reva", 19, "Jalan Panglima sudirman no 07")
orang2 = Manusia("Dita", 25, "Jalan Ahmad Yani no 20")
orang3 = Manusia("Fika", 22, "Jalan Gubernur Suryo no 5")
orang4 = Manusia("Sita", 27, "Jalan Yos Sudarso no 15")
orang5 = Manusia("Lisa", 21, "Jalan Kemayoran no 30")

print(orang1.berjalan())
print(orang2.berlari())
print(orang3.berjalan())
print(orang4.berlari())
print(orang5.berjalan())
