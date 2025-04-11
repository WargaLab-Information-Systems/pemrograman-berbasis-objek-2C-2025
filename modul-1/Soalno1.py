class Manusia:
    def __init__(self, nama, nim, umur, alamat):
        self.nama = nama
        self.nim = nim
        self.umur = umur
        self.alamat = alamat

    def berjalan(self):
        print(f"{self.nama} sedang berjalan")

    def berlari(self):
        print(f"{self.nama} sedang berlari")


manusia1 = Manusia("Eka Rohmawati", "016", "19", "surabaya")
manusia2 = Manusia("Yesica Pitri Ariani", "96", "19", "surabaya")
manusia3 = Manusia("Windy Naila Askanah", "104", "18", "bali")
manusia4 = Manusia("Kholifatun Naisa", "144", "18", "jakarta")
manusia5 = Manusia("Dian Wildan", "64", "20", "bali")

manusia1.berjalan()
manusia2.berlari()
manusia3.berlari()
manusia4.berjalan()
manusia5.berjalan()

