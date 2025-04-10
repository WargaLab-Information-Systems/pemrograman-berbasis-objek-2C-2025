class manusia:
    def __init__(self, nama, umur, alamat):
        self.nama   = nama
        self.umur   = umur
        self.alamat = alamat
    
    def berlari(self):
        print(f"Nama    : ", self.nama)
        print(f"Umur    : ", self.umur)
        print(f"Alamat  : ", self.alamat)
        print("Sedang Berlari...")
        print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    def berjalan(self):
        print(f"Nama    : ", self.nama)
        print(f"Umur    : ", self.umur)
        print(f"Alamat  : ", self.alamat)
        print("Sedang Berjalan...")
        print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


manusia1 = manusia("Harisa", "20", "Jl. Jokotole")
manusia2 = manusia("Laila", "17", "Jl. Kemuning")
manusia3 = manusia("Isti", "18", "Jl. Melati")
manusia4 = manusia("Nia", "20", "Jl. Veteran")
manusia5 = manusia("septi", "15", "Jl. Balige")

manusia1.berlari()
manusia3.berlari()
manusia2.berjalan()
manusia4.berjalan()
manusia5.berjalan()