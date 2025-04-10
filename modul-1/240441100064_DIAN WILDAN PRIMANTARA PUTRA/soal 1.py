class Manusia:
    def __init__(self, nama, umur, alamat):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat

    def berjalan(self):
        return f"{self.nama} sedang berjalan."

    def berlari(self):
        return f"{self.nama} sedang berlari."

manusia1 = Manusia("Diann", 18, "Pamekasan")
manusia2 = Manusia("Jefri", 19, "Sumenep")
manusia3 = Manusia("Hilmiy", 20, "Bangkalan")
manusia4 = Manusia("Rendi", 21, "Sumenep")
manusia5 = Manusia("primantaraputra", 16, "Surabaya")

print(manusia1.berjalan())
print(manusia2.berlari())
print(manusia3.berjalan())
print(manusia4.berlari())
print(manusia5.berjalan())