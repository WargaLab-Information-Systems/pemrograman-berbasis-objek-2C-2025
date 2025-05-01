class manusia:
    def __init__(self, nama, umur, alamat):
        self.nama = nama 
        self.umur = umur
        self.alamat = alamat

    def berjalan(self):
        print(f"{self.nama} sedang berjalan jalan di trotoar jalanan")

    def berlari(self):
        print(f"{self.nama} sedang belari di arena berlari di lapangan ")

    def renang(self):
        print(" 2 ")

manusia1 = manusia ("windy", 18, "jl.cemara indah")
manusia2 = manusia ("erika", 20, "jl.yang penting jalan")
manusia3 = manusia ("saskia", 19, "jl.gapenting")
manusia4 = manusia ("yesi", 22, "ji.cempaka aja")
manusia5 = manusia ("nisa", 25, "jl.gatau juga")
manusia6 = manusia("sina", 25, "jl.bojonegoro")


manusia1.berjalan()
manusia2.berlari()
manusia3.berjalan()
manusia4.berlari()
manusia5.berlari() 
manusia6.berjalan()
manusia1.renang()