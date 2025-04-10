class manusia:
    def __init__(self, nama, umur, alamat):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat

    def berjalan(self):
        print(f"{self.nama} sedang berjalan.")

    def berlari(self):
        print(f"{self.nama} sedang berlari.")

orang1 = manusia("Adytta", 19, "Jakarta")
orang2 = manusia("Fauzi", 20, "Jakarta")
orang3 = manusia("Abdul", 19, "Jakarta")
orang4 = manusia("Ilham", 20, "Jakarta")
orang5 = manusia("Teddy", 19, "Jakarta")
orang6 = manusia("Rehan", 20, "Jakarta")

orang1.berjalan()
orang2.berlari()
orang3.berjalan()
orang4.berlari()
orang5.berjalan()
orang6.berlari()