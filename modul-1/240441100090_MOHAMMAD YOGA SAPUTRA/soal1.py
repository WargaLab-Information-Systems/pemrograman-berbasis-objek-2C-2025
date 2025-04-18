class Manusia:
    def __init__(self, nama, umur, alamat):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat

    def berlari(self):
        print("==========================")
        print(f"Nama   : {self.nama}")
        print(f"Umur   : {self.umur}")
        print(f"Alamat : {self.alamat}")
        print("Sedang berlari")
        print("==========================")

    def berjalan(self):
        print("==========================")
        print(f"Nama   : {self.nama}")
        print(f"Umur   : {self.umur}")
        print(f"Alamat : {self.alamat}")
        print("Sedang berjalan")
        print("==========================")

manusia1 = Manusia("Dimas", "20", "Surabaya")
manusia2 = Manusia("Rina", "22", "Malang")
manusia3 = Manusia("Siti", "21", "Bandung")
manusia4 = Manusia("Budi", "23", "Jakarta")
manusia5 = Manusia("Andi", "24", "Yogyakarta")
manusia6 = Manusia("Yoga", "19", "Tuban")

manusia1.berjalan()
manusia2.berjalan()
manusia3.berjalan()
manusia4.berlari()
manusia5.berlari()
manusia6.berlari()