class manusia:
    def __init__(self, nama, umur, alamat):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat
        pass

    def berjalan(self):
        return f"{self.nama} sedang berjalan"
    
    def berlari(self):
        return f"{self.nama} sedang berlari"
    
manusia1 = manusia("Rendi", 19, "sumenep")
print(f"nama: {manusia1.nama},umur: {manusia1.umur}, alamat: {manusia1.alamat}")
manusia2 = manusia("alfariza", 20, "sumenep")
print(f"nama: {manusia2.nama},umur: {manusia2.umur}, alamat: {manusia2.alamat}")
manusia3 = manusia("syilmi", 30, "bangkalan")
print(f"nama: {manusia3.nama},umur: {manusia3.umur}, alamat: {manusia3.alamat}")
manusia4 = manusia("yaya", 50, "sampang")
print(f"nama: {manusia4.nama},umur: {manusia4.umur}, alamat: {manusia4.alamat}")
manusia5 = manusia("wanda", 28, "surabaya")
print(f"nama: {manusia5.nama},umur: {manusia5.umur}, alamat: {manusia5.alamat}")

print(manusia1.berjalan())
print(manusia2.berjalan())
print(manusia3.berlari())
print(manusia4.berlari())
print(manusia5.berlari())
