class Manusia:
    def __init__(self, nama, umur, alamat):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat

    def berlari(self):
        return f"Nama: {self.nama}, Umur: {self.umur}, Alamat: {self.alamat}, sedang berlari"
    
    def berjalan(self):
        return f"Nama: {self.nama}, Umur: {self.umur}, Alamat: {self.alamat}, sedang berjalan"
    
manusia1 = Manusia("Faisal", 19, "Bojonegoro")
manusia2 = Manusia("Yoga", 17, "Ngawi selatan")
manusia3 = Manusia("Ambaki", 23, "Porong")
manusia4 = Manusia("Adit", 18, "Jaksel")
manusia5 = Manusia("Wahyu", 19, "Pamekasan")

print(manusia1.berjalan())
print(manusia2.berjalan())
print(manusia3.berjalan())
print(manusia4.berlari())
print(manusia5.berlari())