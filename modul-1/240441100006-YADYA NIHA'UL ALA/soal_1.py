class Manusia:
    def __init__(self, nama, umur, alamat):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat

    def berlari(self):
        print(f"Peserta atas nama", self.nama, "umur", self.umur, "dari", self.alamat, "telah berlari sejauh 18 km")
    
    def berjalan(self):
        print(f"Peserta atas nama", self.nama, "umur", self.umur, "dari", self.alamat, "telah berjalan sejauh 9 km")

data1 = Manusia("Yadya", 17, "Bojonegoro")
data2 = Manusia("Adep", 19, "Semarang")
data3 = Manusia("Ala", 19, "Bojonegoro")
data4 = Manusia("Ifa", 21, "Natlan")
data5 = Manusia("Ayato", 24, "Inazuma")

data3.berlari()
data1.berlari()
data2.berjalan()
data4.berjalan()
data5.berjalan()