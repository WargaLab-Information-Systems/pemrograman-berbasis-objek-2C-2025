class manusia:
    def __init__(self, nama, umur, alamat, aktivitas):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat
        self.aktivitas = aktivitas

    def display(self):
        print("=== DATA MANUSIA ===")
        print("Nama : ", self.nama)
        print("Umur : ", self.umur)
        print("Alamat : ", self.alamat)
        print("Aktivitas : ", self.aktivitas)
        print(" ")
        
manusia1 = manusia("Alief", 19, "Jl. Keputran", "Sedang Berjalan")
manusia2 = manusia("Amin", 20, "Jl. Sencaki", "Sedang Berlari")
manusia3 = manusia("Yoga", 19, "Jl. Tuban", "Sedang Berlari")
manusia4 = manusia("Bryan", 20, "Jl. Nganjuk", "Sedang Berjalan")
manusia5 = manusia("Sahrul", 21, "Jl. Jombang", "Sedang Berjalan")

manusia1.display()
manusia2.display()
manusia3.display()
manusia4.display()
manusia5.display()