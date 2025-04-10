class manusia:
    def __init__(self, nama, umur, alamat):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat

    def berlari(self):
        print("==========================")
        print(f"Nama   :", self.nama)
        print(f"Umur   :", self.umur)
        print(f"Alamat :", self.alamat)
        print("Sedang berlari")
        print("==========================")
    def berjalan(self):
        print("==========================")
        print(f"Nama   :", self.nama)
        print(f"Umur   :", self.umur)
        print(f"Alamat :", self.alamat)
        print("Sedang berjalan")
        print("==========================")

manusia1 = manusia("Wahyu", "19", "Tamberu")
manusia2 = manusia("Angga", "19", "Ngawi")
manusia3 = manusia("Bolang", "19", "Tuban")
manusia4 = manusia("Rusdi", "19", "Sukolilo")
manusia5 = manusia("Andre", "19", "Jember")

manusia1.berjalan()
manusia2.berlari()
manusia3.berjalan()
manusia4.berlari()
manusia5.berjalan()