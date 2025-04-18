class Manusia:
    def __init__(self, nama, umur, alamat):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat

    def berjalan(self):
        print(f"{self.nama}, yang berumur {self.umur}, dan yang beralamat {self.alamat} sedang berjalan")

    def berlari(self):
        print(f"{self.nama}, yang berumur {self.umur}, dan yang beralamat {self.alamat} sedang berlari")

manusia1 = Manusia("Revan", 19, "Kediri")
manusia2 = Manusia("Salmon", 20, "Lamongan")
manusia3 = Manusia("Dhani", 19, "Lamongan")
manusia4 = Manusia("Jois", 20, "Gresik")
manusia5 = Manusia("Khapi", 19, "Gresik")

manusia1.berlari()
manusia2.berlari()
manusia3.berlari()
manusia4.berjalan()
manusia5.berjalan()