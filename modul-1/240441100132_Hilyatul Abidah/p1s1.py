class Manusia:
    def __init__(self, nama, umur, alamat):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat

    def berjalan(self):
        print(f"Seseorang yang bernama {self.nama} berumur {self.umur} sedang berjalan di sekitar taman yang berada di {self.alamat}.")

    def berlari(self):
        print(f"Seseorang yang bernama {self.nama} berumur {self.umur} sedang berlari di sekitar Gor yang berada di {self.alamat} dengan semangat!")

m1 = Manusia("hilya", 20, "Surabaya")
m2 = Manusia("Roni", 22, "Sidoarjo")
m3 = Manusia("kanin", 19, "Malang")
m4 = Manusia("erni", 21, "Mojokerto")
m5 = Manusia("Gilang", 23, "Gresik")

m1.berjalan()
m2.berlari()
m3.berjalan()
m4.berlari()
m5.berjalan()
